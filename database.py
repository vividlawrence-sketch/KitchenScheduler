import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join("database", "scheduler.db")

def connect():
    os.makedirs("database", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def card_exists(fingerprint):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT 1 FROM scanned_cards WHERE fingerprint=?",
        (fingerprint,)
    )

    result = cur.fetchone()

    conn.close()

    return result is not None


def remember_card(fingerprint):

    now = datetime.now().isoformat()

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT OR REPLACE INTO scanned_cards(
            fingerprint,
            first_seen,
            last_seen
        )
        VALUES(
            ?,
            COALESCE(
                (SELECT first_seen
                 FROM scanned_cards
                 WHERE fingerprint=?),
                 ?
            ),
            ?
        )
    """,(fingerprint,fingerprint,now,now))

    conn.commit()
    conn.close()    

def initialize():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        uuid TEXT PRIMARY KEY,
        fingerprint TEXT UNIQUE,
        queue_number TEXT,
        queue_timer TEXT,
        printed_time TEXT,
        slot_time TEXT,
        priority INTEGER,
        status TEXT,
        first_seen TEXT,
        completed_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS order_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_uuid TEXT,
        source TEXT,
        pizza_name TEXT,
        quantity INTEGER,
        FOREIGN KEY(order_uuid) REFERENCES orders(uuid)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS sync_queue(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_uuid TEXT,
        action TEXT,
        synced INTEGER DEFAULT 0
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS kitchen_capacity(
        hour TEXT PRIMARY KEY,
        staff INTEGER,
        pizzas_per_hour INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS scanned_cards(
        fingerprint TEXT PRIMARY KEY,
        first_seen TEXT,
        last_seen TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database Ready")
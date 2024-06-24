# view_db.py
import sqlite3
import argparse

def connect_db():
    return sqlite3.connect('test.db')

def view_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(f"- {table[0]}")

def view_items(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    if not items:
        print("No items found in the database.")
    else:
        print("ID | Name | Description | Owner ID")
        print("-" * 40)
        for item in items:
            print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}")

def view_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()
    if not users:
        print("No users found in the database.")
    else:
        print("ID | Username")
        print("-" * 20)
        for user in users:
            print(f"{user[0]} | {user[1]}")

def view_user_items(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE owner_id = ?", (user_id,))
    items = cursor.fetchall()
    if not items:
        print(f"No items found for user with ID {user_id}.")
    else:
        print(f"Items for user with ID {user_id}:")
        print("ID | Name | Description")
        print("-" * 30)
        for item in items:
            print(f"{item[0]} | {item[1]} | {item[2]}")

def main():
    parser = argparse.ArgumentParser(description="View database content")
    parser.add_argument("action", choices=["tables", "items", "users", "user_items"],
                        help="Action to perform")
    parser.add_argument("--user_id", type=int, help="User ID for user_items action")

    args = parser.parse_args()

    conn = connect_db()

    try:
        if args.action == "tables":
            view_tables(conn)
        elif args.action == "items":
            view_items(conn)
        elif args.action == "users":
            view_users(conn)
        elif args.action == "user_items":
            if args.user_id is None:
                print("Error: --user_id is required for user_items action")
            else:
                view_user_items(conn, args.user_id)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
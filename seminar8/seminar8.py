import sqlite3


def connect(dbfile):
    return sqlite3.connect(dbfile)


# Create a SQLite database and name it users.db
conn = connect("users.db")

# Create cursor object
cur = conn.cursor()

# Create a table “users” with the following fields: id, username, first_name, last_name,
# email, password, created_at, last_updated_at, last_signed_in
cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INT PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        created_at TEXT,
        last_updated_at TEXT,
        last_signed_in TEXT
    );
""")
conn.commit()


def get_users():
    """return all users in the users table or an empty list if no users exist in  the database"""

    cur.execute("SELECT * FROM users;")

    all_users = cur.fetchall()

    print(all_users)
    # [print(row) for row in all_users]


def get_user_by_username(username):
    """
    :param username:
    :return the username and password if the user with the desired username exists in the database
            and an empty list otherwise:
    """
    cur.execute(f"SELECT * FROM users WHERE username='{username}';")
    found_user = cur.fetchone()

    print(found_user)


def create_user(conn, user_details):
    """
    :param conn:
    :param user_details:
    :return insert a new user in the database:
    """
    cur.executemany("INSERT OR IGNORE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", user_details)
    conn.commit()


def delete_user(conn, username):
    """
    :param conn:
    :param username:
    :return delete user with the specified username if it exists:
    """
    cur.execute(f"DELETE FROM users WHERE username='{username}';")
    conn.commit()


def edit_user(conn, username, details):
    """
    :param conn:
    :param username:
    :param details:
    :return update the user with the specified username. Make sure you only
            change the details provided in the details dictionary.:
    """
    cur.execute(f"""
        UPDATE users
        SET '{details}'
        WHERE username='{username}'; 
    """)


users = [
    ('00001', 'JonSnow', 'Jon', 'Snow', 'jonsnow@wall.com', 'jonsnow123', '24/11/21', None, None),
    ('00002', 'LouiseLane', 'Louise', 'Lane', 'Louiselane23@crypto.com', 'll2345', '24/11/21', None, None),
    ('00003', 'user_to_delete', 'fname', 'lname', 'email@email.com', 'pass', '24/11/21', None, None),
]

create_user(conn, users)
get_user_by_username('JonSnow')
get_users()
delete_user(conn, 'user_to_delete')
get_users()
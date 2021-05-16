import sqlite3
import os

table_query = """
            create table tag (
            path text not null,
            tag text not null,
            primary key (path, tag)
            );
        """


def check_db_exists():
    if not os.path.isfile("data.db"):
        open("data.db", "a").close()
        conn = sqlite3.connect('data.db')
        conn.execute(table_query)
        return conn
    return sqlite3.connect('data.db')


def clear_database(conn):
    try:
        conn.execute("drop table tag;")
        conn.execute(table_query)
    except sqlite3.OperationalError:
        pass


def add_tag(conn, path, tag):
    query = f"insert into tag (path, tag) values ('{path}', '{tag}');"
    conn.execute(query)
    conn.commit()


def get_tag(conn, tag):
    query = f"select path from tag where tag = '{tag}'"
    result = conn.execute(query)
    return list(map(lambda x: x[0], result))


conn = check_db_exists()
clear_database(conn)
add_tag(conn, "image.png", "stationary")
add_tag(conn, "image2.png", "stationary")
add_tag(conn, "blah.png", "food")
print(get_tag(conn, "stationary"))
conn.close()


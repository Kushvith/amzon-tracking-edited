import sqlite3


def connect():
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (email text)")
    con.commit()
    con.close()


def insert(email):
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES(?)", (email,))
    con.commit()
    con.close()


def view():
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows


def search(email=""):
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE email=?", (email,))
    rows = cur.fetchall()
    con.close()
    return rows


def delete(email):
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE email=?", (email,))
    con.commit()
    con.close()


def update(email):
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET email=? ", (email,))
    con.commit()
    con.close()


connect()


# insert("kushvith@gmail.com")
# delete('')
# search("kushvithchinna900@gmail.com")
# print(view())
def convertTuple(tup):
    str = ''.join(tup)
    return str


def searchings(view):
    for email in view:
        converted = convertTuple(email)
        return converted

# searching(view())

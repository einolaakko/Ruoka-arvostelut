import db

def add_item(title, description, tähdet, user_id):
    sql = """INSER INTO items (title, description, Tähdet1-5, user_id) VALUES(?,?,?,?)"""
    db.execute(sql, [title,description, tähdet, user_id])

def get_items():
    sql = "SELECT id, title FROM items ORDER BY id DESC"
    return db.query(sql)

def get_items(item_id):
    sql = """SELECT items.id, items.title, items.description, items.tähdet, users.id user_id, users.username FROM items, users WHERE items.user_id = users.id AND items.id = ?"""
    return db.query(sql, [item_id])[0]

# vim-fileencoding=utf-8


def create_objects_table(conn):
    """Creates (if non-existent) the object table in database."""
    c = conn.cursor()

    c.execute('''CREATE TABLE objects (id integer primary key,
                excelid integer, engname text, engnotes text, engmaterials text,
                engwp text, itawp text, gruppo integer)
                ''')
    conn.commit()


def save_data(conn, p_data):
    """Creates new class for user."""

    c = conn.cursor()
    c.execute("INSERT INTO objects VALUES ( NULL, ?, ?, ?, ?, ?, ?, ?)",
            (int(p_data["xcID"]), p_data["engName"], p_data["engNotes"],
                p_data["engMaterials"], p_data["engWPrinc"], p_data["itaWPrinc"],
                int(p_data["gruppo"])))
    last_id = c.lastrowid
    conn.commit()

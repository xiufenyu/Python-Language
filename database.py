import sqlite3
import logging
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file, isolation_level=None)
        logging.debug(f'Create {db_file} Successfully')
    except Error as e:
        logging.error(e)

    return conn


# merge databases
def attach_databases(db_names):
    # enter sub database directory
    conn = sqlite3.connect("res.db")
    cursor = conn.cursor()
    base_dir = "./"
    for c in db_names:
        attach_sql = f"ATTACH '{base_dir + c}' AS 'db_{c}'"
        print(attach_sql)
        cursor.execute(attach_sql)
        conn.commit()

        # insert values
        for t in TABLE_PARAMS_DICTS:
            params = TABLE_PARAMS_DICTS[t]
            insert_sql = f"INSERT INTO {t} ({params}) SELECT {params} FROM 'db_{c}'.{t}"
            print(insert_sql)
            cursor.execute(insert_sql)
            conn.commit()



'''
Question:  "NOT IN (SUBQUERY)" is not working as expected?
    The normal reason for problems with not in is the presence of NULL values. NOT IN always fails when the list has NULL because NULL comparisons cannot be true.
Solution: 
#  I prefer to use NOT EXISTS, because it has the semantics that you expect:
   SELECT COUNT(DISTINCT WIDGET_ID) FROM A WHERE NOT EXISTS (SELECT WIDGET_ID FROM B WHERE B.WIDGET_ID = A.WIDGET_ID)
''' 

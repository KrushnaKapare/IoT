from utils.dbConnection import get_db_connection

def execute_query(query):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    
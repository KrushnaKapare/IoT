from utils.dbConnection import get_db_connection

def execute_select_query(query):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    return data
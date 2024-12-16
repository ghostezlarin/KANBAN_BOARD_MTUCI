import psycopg2
from connection_db_const import user, password, host, port, database
from SQL_SCRIPTS import kanban_select
import json


def select_kanban(project_id: int):
    connection = 0
    error_code = 0
    error_desc = ""
    kanban_board = 0
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        print(connection)
        print("Connection is successful")

    except Exception as e:
        error_code = -1
        error_desc = e.__str__()
        print("a96b1466-3629-4139-a669-d344bbd3141e")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = kanban_select
            cursor.execute(insert_query, (project_id,))
            kanban_board = cursor.fetchall()
            connection.commit()
            connection.close()
            print("Insert was successful")
        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print(error_code, error_desc)
            print("b25a9822-7412-48e6-9b18-47db1834de2e")

    return {"kanban_board": kanban_board,
            "error_code": error_code,
            "error_desc": error_desc}


# print(select_kanban(1))

# r = json.dumps(select_kanban(1))
# print(r)

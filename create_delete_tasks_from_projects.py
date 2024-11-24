import psycopg2
from connection_db_const import user, password, host, port, database


def create_tasks_in_projects(task_id: int, project_id: int):
    connection = 0
    error_code: int = 0
    error_desc: str = ""
    project_tasks_id: int = 0
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
        print("85ac55f8-1219-4aae-8482-cef32f0d08d0")
        print(error_code, error_desc)

    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """INSERT INTO t_projects_tasks(task_id, project_id) VALUES(%s, %s) returning id"""
            record_to_insert = (task_id, project_id)
            cursor.execute(insert_query, record_to_insert)
            project_tasks_id = cursor.fetchone()[0]
            connection.commit()
            connection.close()

        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print("4a3ca72d-d43a-4c88-ab42-447ef004d0a5")
            print(error_code, error_desc)
    return {project_tasks_id, error_code, error_desc}


def delete_tasks_in_project(task_id, project_id):
    connection = 0
    error_code: int = 0
    error_desc: str = ""
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
        print("382b7c57-38b7-40d1-a537-d6cc2075e673")
        print(error_code, error_desc)

    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """UPDATE public.t_projects_tasks SET status = -1 WHERE (task_id = %s AND project_id = %s)"""
            record_to_insert = (task_id, project_id)
            cursor.execute(insert_query, record_to_insert)
            connection.commit()
            connection.close()

        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print("a144df19-336d-4ee5-98c8-4e24eef800ab")
            print(error_code, error_desc)
    return {error_code, error_desc}
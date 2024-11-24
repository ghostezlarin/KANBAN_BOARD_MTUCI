import psycopg2
from connection_db_const import user, password, host, port, database


def create_users_in_projects(user_id: int, project_id: int):
    connection = 0
    error_code: int = 0
    error_desc: str = ""
    users_projects_id: int = 0
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
        print("e707ee11-afe1-4127-9e08-8f07f74928c5")
        print(error_code, error_desc)

    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """INSERT INTO t_users_projects(user_id, project_id) VALUES(%s, %s) returning id"""
            record_to_insert = (user_id, project_id)
            cursor.execute(insert_query, record_to_insert)
            users_projects_id = cursor.fetchone()[0]
            connection.commit()
            connection.close()

        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print("efed3ee8-c151-454d-a712-3c12f431d8d6")
            print(error_code, error_desc)
    return {users_projects_id, error_code, error_desc}


def delete_users_in_project(user_id, project_id):
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
        print("867485d5-77fb-4613-b93c-ba1c65da1ed2")
        print(error_code, error_desc)

    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """UPDATE public.t_users_projects SET status = -1 WHERE (user_id = %s AND project_id = %s)"""
            record_to_insert = (user_id, project_id)
            cursor.execute(insert_query, record_to_insert)
            connection.commit()
            connection.close()

        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print("2711caed-56b2-42ff-b322-896187a939ec")
            print(error_code, error_desc)
    return {error_code, error_desc}

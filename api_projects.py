import psycopg2
from connection_db_const import user, password, host, port, database


def select_project(name: str):
    project_name = ""
    connection = 0
    error_code = 0
    error_desc = ""

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
        print("84cd278c-e19c-40f3-9797-fbad8b48062b")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """SELECT name FROM public.v_projects_active WHERE name=%s;"""
            # insert_query = """SELECT name FROM v_users_active"""
            # record_to_insert = name
            cursor.execute(insert_query, (name,))
            project_name = cursor.fetchone()[0]
            print(project_name)
            print(type(project_name))
            connection.commit()
            connection.close()
            print("Insert was successful")
        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print(error_code, error_desc)
            print("77cf6150-727a-479c-a0fd-ac9c577a496e")

    return {"project_name": project_name,
            "error_code": error_code,
            "error_desc": error_desc}


def list_of_active_projects():
    project_list = ""
    connection = 0
    error_code = 0
    error_desc = ""

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
        print("ac2dbf10-2b5a-4e76-9bd8-c76f34c80546")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """SELECT name FROM v_projects_active"""
            cursor.execute(insert_query)
            project_list = [r[0] for r in cursor.fetchall()]
            print(project_list)
            print(type(project_list))
            connection.commit()
            connection.close()
            print("Insert was successful")
        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print(error_code, error_desc)
            print("64b74e27-c627-46ed-8679-979187fd742d")

    return {"project_list": project_list,
            "error_code": error_code,
            "error_desc": error_desc}

#
# print(select_project("KANBAN BOARD"))

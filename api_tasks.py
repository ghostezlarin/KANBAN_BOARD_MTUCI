import json

import psycopg2
from connection_db_const import user, password, host, port, database
from SQL_SCRIPTS import tasks_by_users, tasks_in_projects, test


def list_of_active_tasks():
    task_list = ""
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
        print("a96b1466-3629-4139-a669-d344bbd3141e")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """SELECT name FROM v_tasks_active"""
            cursor.execute(insert_query)
            task_list = [r[0] for r in cursor.fetchall()]
            print(task_list)
            print(type(task_list))
            connection.commit()
            connection.close()
            print("Insert was successful")
        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print(error_code, error_desc)
            print("b25a9822-7412-48e6-9b18-47db1834de2e")

    return {"task_list": task_list,
            "error_code": error_code,
            "error_desc": error_desc}


def select_task(name: str):
    task_name = ""
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
        print("addd4ea0-918d-4e01-ab69-cb9f01018eeb")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            print(name + "kgrtgkrtg")
            cursor = connection.cursor()
            insert_query = "SELECT name FROM v_tasks_active WHERE name=%s"
            # insert_query = """SELECT name FROM v_users_active"""
            cursor.execute(insert_query, (name,))
            print("execute succesfull")
            task_name = cursor.fetchone()[0]
            print("fetchone succesfull")
            print(task_name)
            print(type(task_name))
            connection.commit()
            connection.close()
            print("Insert was successful")
        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print(error_code, error_desc)
            print("898d17c6-6897-4623-b3e3-a8528de11bf4")

    return {"task_name": task_name,
            "error_code": error_code,
            "error_desc": error_desc}


def tasks_by_users_func(user_id: int):
    connection = 0
    error_code = 0
    error_desc = ""
    r = 0
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
        print("addd4ea0-918d-4e01-ab69-cb9f01018eeb")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = tasks_by_users
            cursor.execute(insert_query, (user_id,))
            r = cursor.fetchall()[0][0]
            print(r)
            connection.commit()
            connection.close()
            print("Select was successful")
        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print(error_code, error_desc)
            print("898d17c6-6897-4623-b3e3-a8528de11bf4")

    return {"r": r,
            "error_code": error_code,
            "error_desc": error_desc}


def tasks_in_project_func(project_id: int):
    connection = 0
    error_code = 0
    error_desc = ""
    r = 0
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
        print("addd4ea0-918d-4e01-ab69-cb9f01018eeb")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = tasks_in_projects
            cursor.execute(insert_query, (project_id,))
            r = cursor.fetchall()[0][0]
            print(r)
            connection.commit()
            connection.close()
            print("Select was successful")
        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print(error_code, error_desc)
            print("898d17c6-6897-4623-b3e3-a8528de11bf4")

    return {"r": r,
            "error_code": error_code,
            "error_desc": error_desc}


def select_from_logs(task_id):
    connection = 0
    error_code = 0
    error_desc = ""
    r = 0
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
        print("addd4ea0-918d-4e01-ab69-cb9f01018eeb")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """SELECT json_agg(Q.*) FROM (SELECT * FROM public.t_tasks_log WHERE task_id=%s) Q;"""
            cursor.execute(insert_query, (task_id,))
            r = cursor.fetchall()[0][0]
            print(r)
            connection.commit()
            connection.close()
            print("Select was successful")
        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print(error_code, error_desc)
            print("898d17c6-6897-4623-b3e3-a8528de11bf4")

    return {"r": r,
            "error_code": error_code,
            "error_desc": error_desc}


# print(select_from_logs(3))

# print(tasks_in_project_func(1))
# # print(select_from_users_active_view())
# # r = json.dumps(select_from_users_active_view())
# # print(r)
# # print(select_user("Pavlas Protopas"))
# # r = json.dumps(select_user("Pavlas Protopas"))
# # print(r)
#
# j = tasks_by_users_func(1)
# print(j)

# j = json.dumps(tasks_by_users_func(1))
# print(j)
# print(tasks_by_users_func(1))

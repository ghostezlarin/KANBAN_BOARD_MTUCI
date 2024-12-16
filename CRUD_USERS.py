import psycopg2
from connection_db_const import user, password, host, port, database


def create_user(name: str):
    connection = 0
    client_id: int = -1
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
            insert_query = """INSERT INTO t_users (name, status) VALUES (%s, %s) RETURNING id"""
            record_to_insert = (name, "1")
            cursor.execute(insert_query, record_to_insert)
            client_id = cursor.fetchone()[0]
            connection.commit()
            connection.close()
            print("Insert was successful")
        except Exception as e:
            error_code = -2
            error_desc = e.__str__()
            print(error_code, error_desc)
            print("b25a9822-7412-48e6-9b18-47db1834de2e")

    return {"client_id": client_id,
            "error_code": error_code,
            "error_desc": error_desc}


def read_user(id: int):
    connection = 0
    name: str = ""
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
        error_code = -3
        error_desc = e.__str__()
        print("7a040160-bf17-443e-b3e1-034139631da0")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """SELECT name FROM public.t_users WHERE id = %s AND status = 1 ORDER BY id;"""  # поправить статус
            cursor.execute(insert_query, (id,))
            name = cursor.fetchone()[0]
            cursor.close()
            connection.commit()
            connection.close()
            print(name)

        except Exception as e:
            error_code = -4
            error_desc = e.__str__()
            print("7c687a3d-0a66-4763-92cf-893dd2e95b5b")
            print(error_code, error_desc)

    return {"name": name,
            "error_code": error_code,
            "error_desc": error_desc}


def update_user(id: int, name: str):
    connection = 0
    t = 0
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
        error_code = -5
        error_desc = e.__str__()
        print("b65163d4-ad61-4567-b877-06e7d251503e")
        print(error_code, error_desc)

    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """UPDATE public.t_users SET name = %s WHERE id = %s"""
            record_to_insert = (name, id)
            cursor.execute(insert_query, record_to_insert)
            # t = cursor.fetchone()[0]
            cursor.close()
            connection.commit()
            connection.close()
            print(t)

        except Exception as e:
            error_code = -6
            error_desc = e.__str__()
            print("8c231aee-65c4-491c-a061-58a390e95746")
            print(error_code, error_desc)

    return {#"t": t,
            "error_code": error_code,
            "error_desc": error_desc}


def delete_user(id: int):
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
        error_code = -7
        error_desc = e.__str__()
        print("1249e8db-9f21-42c8-9885-920dae5b22db")
        print(error_code, error_desc)
    if error_code == 0:
        try:
            cursor = connection.cursor()
            insert_query = """UPDATE public.t_users SET status = -1 WHERE id = %s"""
            record_to_query = (id,)
            cursor.execute(insert_query, record_to_query)
            cursor.close()
            connection.commit()
            connection.close()

        except Exception as e:
            error_code = -8
            error_desc = e.__str__()
            print("526c0cae-6d7e-4e1a-a7e0-7e8b8a7f542b")
            print(error_code, error_desc)
    return {"error_code": error_code,
            "error_desc": error_desc}

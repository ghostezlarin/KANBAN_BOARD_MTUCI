kanban_select = """
SELECT
	C.ID AS column_id,
	C.NAME AS column_name,
	T.ID AS task_id,
	T.NAME AS task_name,
	U.ID AS user_id,
	U.NAME AS user_name
FROM
	PUBLIC.T_COLUMNS C,
	PUBLIC.V_TASKS_ACTIVE T,
	PUBLIC.V_USERS_ACTIVE U
WHERE
	T.COLUMN_ID = C.ID
	AND T.USER_ID = U.ID
	AND T.PROJECT_ID = %s
ORDER BY
	C.ID,
	U.NAME,
	T.NAME;
"""

tasks_by_users = """
SELECT json_agg(Q.*) FROM (SELECT
	T.id AS t_id,
	T.name AS t_name,
	T.insert_date AS t_insert_date,
	T.status AS t_status,
	T.column_id AS t_column_id,
	T.project_id AS t_project_id,
	T.user_id AS t_user_id,
	P.id AS p_id,
	P.id AS p_name,
	P.id AS p_insert_date,
	P.id AS p_status
FROM
	V_TASKS_ACTIVE T,
	V_PROJECTS_ACTIVE P
WHERE
	T.USER_ID = %s
	AND T.PROJECT_ID = P.ID) Q;
"""

tasks_in_projects = """
SELECT json_agg(Q.*) FROM (SELECT
	T.id AS t_id,
	T.name AS t_name,
	T.insert_date AS t_insert_date,
	T.status AS t_status,
	T.column_id AS t_column_id,
	T.project_id AS t_project_id,
	T.user_id AS t_user_id,
	U.id AS u_user_id,
	U.name AS u_name,
	U.insert_date AS u_insert_date,
	U.status AS u_status
FROM
	V_TASKS_ACTIVE T,
	V_USERS_ACTIVE U
WHERE
	T.PROJECT_ID = %s
	AND T.USER_ID = U.ID) Q;
"""

test = """
SELECT row_to_json(t)
FROM t_users t;
"""
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

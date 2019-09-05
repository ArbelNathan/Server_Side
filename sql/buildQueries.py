# create new:
from sql.sqlHandler import commend, request_user

table = "mytable"
def create_user(values: dict, user_id):
    if bool(values):
        query_col = ""
        query_val = ""
        for v in values:
            query_col += f"{v['key']},"
            query_val += f"'{v['value']}',"
        query_val = query_val[:len(query_val) - 1]
        query_col = query_col[:len(query_col) - 1]
        query = f"({query_col}) VALUES ({query_val})"
        updt_query = f"INSERT INTO table {query};"
        return commend(updt_query)


def update_user(values, user_id):
    if bool(values):
        query = ""
        for v in values:
                query += f"{v['key']} = '{v['value']}',"
        query = query[:len(query) - 1]
        updt_query = f"UPDATE table SET {query} " \
                     f"WHERE table.id = '{user_id}';"
        return commend(updt_query)


def get_user(user_id):
    query = f"SELECT * FROM table WHERE id = '{user_id}'"
    return request_user(query)


def get_user_by_email(user_email):
    query = f"SELECT * FROM table WHERE email = '{user_email}'"
    return request_user(query)


def delete_user(user_id):
    query = f"UPDATE table SET activated = 0 where  table.id = '{user_id}' "
    return commend(query)


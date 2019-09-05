import mysql.connector
import datetime


def commend(sql_req):
    my_db = mysql.connector.connect(
        user="myusername",
        password="mypassword",
        host="myhost",
        database="mydatabaseName"
    )
    sql = my_db.cursor()
    try:
        sql.execute(str(sql_req))
        my_db.commit()
        my_db.close()
        return True
    except Exception as e:
        print(e)
        return False


def request_user(sql_req):
    my_db = mysql.connector.connect(
        user="myusername",
        password="mypassword",
        host="myhost",
        database="mydatabaseName"
    )
    sql = my_db.cursor(prepared=True)
    try:
        print(sql_req)
        sql.execute(str(sql_req))
        col = sql.column_names
        rows = list()
        i = 0
        temprow = sql.fetchone()
        while temprow is not None:

            rows.append(temprow)
            i += 1
            temprow = sql.fetchone()
        my_db.close()
        rows = [list(x) for x in rows]
        for i in range(0, len(rows)):
            for t in range(0, len(rows[i])):
                if isinstance(rows[i][t], bytearray):
                    rows[i][t] = rows[i][t].decode()
                if isinstance(rows[i][t], datetime.date):
                    rows[i][t] = str(rows[i][t].now())[:19]
            rows[i] = dict(zip(col, rows[i]))
        return rows
    except Exception as e:
        print(e)
        return None


def request_helper(sql_req):
    my_db = mysql.connector.connect(
        user="myusername",
        password="mypassword",
        host="myhost",
        database="mydatabaseName"
    )
    sql = my_db.cursor(prepared=True)
    try:
        sql.execute(str(sql_req))
        temprow = sql.fetchone()
        return temprow[0].decode()
    except Exception as e:
        print(e)
        return None


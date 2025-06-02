# query_executor.py

import pymysql

# Function to execute SQL query
def execute_query(conn, sql_query):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        conn.commit()
        return "✅ Query executed successfully!"
    except pymysql.MySQLError as e:
        return f" MySQL Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"

# app.py

import streamlit as st
import pymysql

from connection import get_connection
from query_executor import execute_query
from query_generator import generate_sql

# Streamlit UI
st.title(" AI SQL ENGINE ")

conn = get_connection()
if not conn:
    st.stop()

st.success("✅ Connected to MySQL successfully!")

cursor = conn.cursor()
cursor.execute("SHOW DATABASES;")
databases = [db[0] for db in cursor.fetchall()]

selected_db = st.selectbox("📂 Select an existing database", databases)
new_db = st.text_input("📦 Or enter a new database name to create and use it:")

if new_db:
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{new_db}`;")
        cursor.execute(f"USE `{new_db}`;")
        st.success(f"✅ Created and switched to new database: `{new_db}`")
    except pymysql.MySQLError as e:
        st.error(f"❌ Error creating or switching to new database: {e}")
elif selected_db:
    try:
        cursor.execute(f"USE `{selected_db}`;")
        st.success(f"✅ Switched to database: `{selected_db}`")
    except pymysql.MySQLError as e:
        st.error(f"❌ Error selecting database: {e}")

# State to store the generated SQL
if "generated_sql" not in st.session_state:
    st.session_state.generated_sql = ""

natural_language_query = st.text_area("💬 Enter your natural language query", "")

# Generate Button
if st.button("🛠️ Generate SQL"):
    if natural_language_query.strip():
        sql_query = generate_sql(natural_language_query)
        st.session_state.generated_sql = sql_query
        st.subheader("📝 Generated SQL:")
        st.code(sql_query)
    else:
        st.warning("⚠️ Please enter a natural language query.")

# Show Execute button only if SQL is generated
if st.session_state.generated_sql:
    st.subheader("▶️ Generated SQL Query Ready to Execute")
    st.code(st.session_state.generated_sql)

    if st.button("🚀 Execute SQL"):
        result = execute_query(conn, st.session_state.generated_sql)
        st.write(result)

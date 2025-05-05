# connection.py

import pymysql
import streamlit as st

# Function to get MySQL connection
def get_connection():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='Vignesh@2004',
            port=3306
        )
        return conn
    except pymysql.MySQLError as e:
        st.error(f"Connection Error: {e}")
        return None

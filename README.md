# 📊 AI SQL Assistant - Documentation

AI SQL Assistant is a user-friendly web application that converts natural language queries into SQL statements using an AI language model and executes them on a MySQL database. This tool helps both technical and non-technical users interact with databases easily using plain English.

--

## 🚀 Features
- Convert natural language into SQL queries
- Execute SQL statements on a MySQL database
- AI-powered query generation using OpenAI or Gemini
- Support for SELECT, INSERT, UPDATE, DELETE and more
- Clean, minimal web interface with Streamlit
--
## 🛠️ Technologies Used
- Python: Backend logic
- Streamlit: Web interface
- PyMySQL: Connect and interact with MySQL
- Pandas: Display SQL results in tables
- OpenAI API / Gemini API: Generate SQL from natural language
--
## 📁 Project Structure

```bash
AI_SQL_QUERY/
├── app.py                  # Main Streamlit web application
├── query_generator.py      # AI-powered SQL query generation
├── query_executor.py       # Database connection & query execution
├── requirements.txt        # Python dependencies
      
└── README.md               # Project documentation


## 📦 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ai-sql-assistant.git
    cd ai-sql-assistant
    ```

2. (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # or source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    streamlit run app.py
    ```

## ⚙️ Configuration
Ensure MySQL credentials are set in `app.py`:
```python
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='your_mysql_password',
    port=3306
)

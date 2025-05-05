# 📊 AI SQL ENGINE

AI SQL Assistant is a user-friendly web application that converts natural language queries into SQL statements using an AI language model and executes them on a MySQL database. This tool helps both technical and non-technical users interact with databases easily using plain English.
--

## 🚀 Features
- Convert natural language into SQL queries
- Execute SQL statements on a MySQL database
- AI-powered query generation using Gemini
- Support for SELECT, INSERT, UPDATE, DELETE and more
- Clean, minimal web interface with Streamlit
--
## 🛠️ Technologies Used
- Python: Backend logic
- Streamlit: Web interface
- PyMySQL: Connect and interact with MySQL
- Pandas: Display SQL results in tables
-  Gemini API: Generate SQL from natural language
--
## 💡 How It Works

### 🔄 Workflow Overview

1. **User Input**  
   Enter natural language questions like:  
   `"Show all customers who placed an order in January"`

2. **AI Processing**  
   `query_generator.py`:
   - Connects to Gemini API
   - Converts natural language to SQL:  
     ```sql
     SELECT c.* 
     FROM customers c
     JOIN orders o ON c.id = o.customer_id 
     WHERE MONTH(o.order_date) = 1
     ```

3. **User Review**  
   - Generated SQL is displayed
   - Option to edit before execution

4. **Execution & Results**  
   `query_executor.py`:
   - Connects to MySQL database
   - Executes the SQL query
   - Displays results as pandas DataFrame:
     
     | customer_id | name  | email               | order_date |
     |------------|-------|---------------------|------------|
     | 101        | John  | john@example.com    | 2024-01-15 |
     | 204        | Sarah | sarah@example.com   | 2024-01-22 |

### 🔧 Technical Flow
1``bash
graph TD
    A[User Input] --> B(query_generator.py)
    B --> C[AI API]
    C --> D[SQL Output]
    D --> E[User Approval]
    E --> F(query_executor.py)
    F --> G[MySQL Database]
    G --> H[Pandas DataFrame]
    H --> I[Streamlit Display]
--
## ✅ Use Cases

### 🏢 For Business Teams
| Use Case               | Benefits                                                                 |
|------------------------|--------------------------------------------------------------------------|
| **Business Analysts**  | Query databases without SQL knowledge using natural language             |
| **Product Managers**   | Quickly pull metrics and user analytics without engineering help         |
| **Marketing Teams**    | Extract customer segments and campaign performance data instantly        |

### 🎓 For Education
| Use Case               | Benefits                                                                 |
|------------------------|--------------------------------------------------------------------------|
| **SQL Students**       | Learn SQL syntax by seeing AI-generated translations of natural language |
| **Educators**          | Create teaching examples and exercises automatically                    |
| **Data Science Learners** | Understand database query patterns through real-world examples         |

### 🔍 For Data Exploration
| Use Case               | Benefits                                                                 |
|------------------------|--------------------------------------------------------------------------|
| **Quick Insights**     | Get immediate answers from large datasets without complex queries        |
| **Prototyping**        | Test hypotheses by querying data with simple English questions           |
| **Data Validation**    | Verify data quality and relationships through natural questions          |

### Example Scenarios:
```python
# Marketing Team Example:
"Show me customers from California who purchased in Q1 but haven't ordered since"

# Product Team Example:  
"What percentage of users complete onboarding within 7 days?"

# Student Example:
"Display all students with GPA above 3.5 and their course enrollments"
--
## ✨ Key Features

### 🚀 **Accessible to Everyone**
- Works with **plain English** - no SQL knowledge needed
- Intuitive natural language processing understands:  
  `"Show me the 10 highest revenue customers last month"`
- Perfect for **non-technical team members**

### ⚡ **Blazing Fast Results**
- **Skip the query writing process** - from question to results in seconds
- **No debugging required** - AI generates production-ready SQL
- **Direct database connection** - no manual exporting needed

### 🧠 **Powerful Learning Tool**
| What You Ask | What You Learn |
|--------------|---------------|
| `"Customers who ordered >$100"` | ```sql SELECT * FROM customers WHERE order_value > 100``` |
| `"Total sales by region"` | ```sql SELECT region, SUM(sales) FROM orders GROUP BY region``` |
| `"Duplicate email addresses"` | ```sql SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1``` |

### 🔄 **Seamless Workflow**
1. Ask in English
2. Review generated SQL
3. Execute with one click
4. Get pandas DataFrame results

### 🛡️ **Safe Execution**
- All queries require **manual approval** before execution
- **Read-only mode** available for beginners
- **Query validation** to prevent harmful operations

  

--
## 📁 Project Structure
 ```bash
AI_SQL_QUERY/
├── app.py                  # Main Streamlit web application
├── query_generator.py      # AI-powered SQL query generation
├── query_executor.py       # Database connection & query execution
├── requirements.txt        # Python dependencies
      
└── README.md               # Project documentation

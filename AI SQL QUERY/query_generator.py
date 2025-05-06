# query_generator.py

import os
import json
import requests

# Set Gemini API Key
os.environ["GEMINI_API_KEY"] = "your_api_key"

# Function to generate SQL from natural language
def generate_sql(natural_language_query):
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Convert this natural language query to a valid SQL query. "
                                f"Only return the SQL code with complete syntax. "
                                f"No comments, no markdown, no explanation, no ```sql. "
                                f"Just the SQL code. Query: {natural_language_query}"
                    }
                ]
            }
        ]
    }

    response = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
        headers=headers,
        data=json.dumps(data),
        params={"key": os.environ["GEMINI_API_KEY"]},
    )

    try:
        raw_sql = response.json()['candidates'][0]['content']['parts'][0]['text']
        lines = raw_sql.strip().splitlines()
        lines = [line for line in lines if not line.strip().startswith("--")]
        return "\n".join(lines).strip()
    except (KeyError, IndexError):
        return "❌ Failed to generate SQL. Please try again."

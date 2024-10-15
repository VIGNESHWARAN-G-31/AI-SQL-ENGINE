import streamlit as st
import google.generativeai as genai

# Configure your Google API key
GOOGLE_API_KEY = "AIzaSyB0gjW4oLXUYD_AzCKKBiZ6OicXpQE5b6Q"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    # Set up the page config
    st.set_page_config(page_title="AI SQL ENGINE", page_icon=":robot:")

    # Add CSS to set the background color
    st.markdown(
        """
        <style>
            body {
                background-color: #e6f7ff;
            }
            .container {
                text-align: center;
                margin-top: 50px;
            }
            h1 {
                color: #0c2461;
                font-size: 3em;
            }
            h3, h4 {
                color: #1e3799;
            }
            p {
                color: #4a69bd;
            }
            textarea {
                background-color: #f0f8ff;
            }
            .stButton>button {
                background-color: #1e3799;
                color: white;
                border-radius: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # HTML for the title and description
    st.markdown(
        """
        <div class="container">
            <h1>AI SQL ENGINE</h1>
            <h3>I can Generate SQL queries for you!</h3>
            <h4>With explanation as well!!!</h4>
            <p>This tool is a simple tool that allows you to generate SQL queries based on your queries.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Text area for user input
    text_input = st.text_area("Enter your Query here...")

    # Button to trigger the SQL query generation
    submit = st.button("Generate SQL Query")

    if submit:
        with st.spinner("Generating SQL Query"):
            template = """
                create a SQL Query snippet using the below text:

                {text_input}

                I just want a SQL Query.
            """
            formatted_template = template.format(text_input=text_input)

            st.write(formatted_template)
            response = model.generate_content(formatted_template)
            sql_query = response.text.strip().lstrip("sql").rstrip("")

            expected_output = """
                what would be the expected response of this SQL query snippet:
                        
                {sql_query}
                
                Provide sample tabular Response with no explanation:
            """
            expected_output_formatted = expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_output_formatted).text

            explanation = """
                Explain this SQL Query:
                        
                {sql_query}
                
                Please provide the simplest explanation:
            """
            explanation_formatted = explanation.format(sql_query=sql_query)
            explanation = model.generate_content(explanation_formatted).text

            # Display the results
            with st.container():
                st.success("SQL Query Generated Successfully! Here is your Query Below:")
                st.code(sql_query, language="sql")

                st.success("Expected output of this SQL Query will be:")
                st.markdown(eoutput)

                st.success("Explanation of this SQL Query:")
                st.markdown(explanation)

# Run the main function
main()

import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Vijay Laptop Sales SQL Helper")

question = st.text_input("Question: ")

if question:
    # Build chain with intermediate steps returned
    chain = get_few_shot_db_chain()

    # Run the query
    response = chain.invoke({"query": question})

    # Show verbose trace
    st.subheader("Verbose Trace")

    sql_query = response["intermediate_steps"][1].split("SQLQuery:")[1].strip()
    sql_result = response["intermediate_steps"][3] 
    # Print formatted output
    st.text(f"Question: {response.get('query','')}\n"
            f"SQLQuery: {sql_query}\n"
            f"SQLResult: {sql_result}\n"
            f"Answer: {response.get('result','')}")

    # Show final answer
    st.subheader("Answer")
    st.write(response["result"])

from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from sqlalchemy import create_engine
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType

def create_mysql_db_tool(username, password, host, port, database_name, model_name="gpt-3.5-turbo", query="Describe the database"):
    connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}"
    engine = create_engine(connection_string)
    db = SQLDatabase(engine)
    llm = ChatOpenAI(temperature=0, model_name=model_name)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

    def mysql_db_query(query: str) -> str:
        try:
            response = db_chain.invoke(query)
            return response
        except Exception as e:
            return f"An error occurred: {str(e)}"

    mysql_tool = Tool(
        name="mysql_db_query",
        description="Useful for querying a MySQL database using natural language. Input should be a natural language query about the database.",
        func=mysql_db_query
    )

    tools = [mysql_tool]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    response = agent.invoke({"input": query})

    return response

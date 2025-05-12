from db_tool import create_mysql_db_tool
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# You can change query string here
response = create_mysql_db_tool(
    username="root",
    password="1234",
    host="localhost",
    port="3306",
    database_name="test_agent",
    model_name="gpt-3.5-turbo",
    query="Tell me about the database"
)

print("🧠 Response:\n", response)

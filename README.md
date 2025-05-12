# 🧠 Natural Language MySQL Query Agent using LangChain

This project allows users to interact with a MySQL database using natural language queries. It leverages LangChain, OpenAI LLMs (like `gpt-3.5-turbo`), and SQLDatabaseChain to translate human language into SQL queries and return results.

---

## 🚀 Features

- 🔍 Query MySQL databases using plain English
- 🤖 Built on top of LangChain's `SQLDatabaseChain`
- 🧠 Powered by OpenAI's `gpt-3.5-turbo`
- 🧪 Automatically translates natural language into SQL

---

## 🧰 Requirements

- Python 3.9+
- MySQL running locally or remotely
- OpenAI API key

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/langchain-mysql-agent.git
cd langchain-mysql-agent

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

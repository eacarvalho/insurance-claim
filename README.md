## 🏥 AI Powered Insurance Claim Assistant

This project is an AI-driven insurance claim assistant that guides users through the process of submitting a medical claim.  
It leverages modern tools such as **LangChain**, **LangGraph**, **LLMs**, **Embeddings**, and **Chainlit** to create a conversational and intelligent experience.

---

### 🚀 Features

- Conversational UI powered by **Chainlit**
- Intelligent flow handling with **LangGraph**
- Natural language processing via **OpenAI LLMs**
- Vector-based memory using **Embeddings**
- Optional observability with **LangSmith**

---

### ⚙️ Installation

#### 1. Set up Environment Variables

Create a `.env` file at the root of the project and add your OpenAI API key:

```env
OPENAI_API_KEY=your-api-key-here
```

#### 2. Install Dependencies
```env
pip install -r requirements.txt
```

---

### 🧪 How to Run

Start the application with:

```env
docker compose up
chainlit run app.py
```
Then access it in your browser at:

👉 http://localhost:8000/

You can test it using the example data provided in the `test data.txt` file.

---

### 🔍 Observability
To enable tracing with LangSmith:
- Create an account and obtain your API key.
- Add the following to your .env file:

```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=your-project-name
```
Once configured, you can view traces at:

👉 [LangSmith Dashboard] (https://smith.langchain.com)

---

### 📁 Project Structure

```text
.
├── app.py
├── requirements.txt
├── .env
├── docker-compose.yml
└── test data.txt
```
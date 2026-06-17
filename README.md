# 📚 Enterprise Knowledge Assistant

An AI-powered Enterprise Knowledge Management System built using **RAG (Retrieval-Augmented Generation)**, **Google Gemini**, **FAISS**, **Streamlit**, and **MySQL**.

The application enables employees to ask questions from company documents and receive accurate AI-generated answers instantly.

---

## 🚀 Features

### 👨‍💼 Admin Portal

- Dashboard with system statistics
- Upload PDF documents
- Build and manage knowledge base
- Manage users (Admin & Employee)
- View analytics and system status
- Test AI Chat functionality

### 👨‍💻 Employee Portal

- Ask questions from company documents
- AI-powered document search
- View chat history
- Clear previous chat history

---

## 🧠 RAG Workflow

```text
User Question
      ↓
Generate Embedding
      ↓
FAISS Similarity Search
      ↓
Retrieve Relevant Chunks
      ↓
Google Gemini
      ↓
AI Generated Answer
```

---

## 🏗️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Database
- MySQL

### Vector Database
- FAISS

### AI/LLM
- Google Gemini

### Embeddings
- Sentence Transformers

### Document Processing
- PyPDF2

---

## 📂 Project Structure

```text
enterprise_knowledge_assistant/

├── app.py
├── authentication/
├── database/
├── components/
├── rag/
├── pages/
├── uploads/
├── vector_db/
├── requirements.txt
└── .env
```

---

## 🔐 User Roles

### Admin

- Dashboard
- Upload Documents
- Manage Users
- Analytics
- AI Chat
- Chat History

### Employee

- AI Chat
- Chat History

---

## 💬 Example Questions

- How many annual leaves do employees receive?
- What is the password policy?
- What benefits are available for employees?
- What is the onboarding process?
- Is MFA mandatory?

---

## ✨ Key Highlights

- Built a complete RAG pipeline from scratch
- Implemented role-based authentication
- Integrated Google Gemini for AI responses
- Used FAISS for semantic document retrieval
- Developed Admin and Employee dashboards
- Stored chat history in MySQL
- Created scalable enterprise document search system

---

## 🔮 Future Improvements

- DOCX & Excel Support
- Multi-document citations
- Feedback system
- Docker deployment
- Cloud deployment (AWS/Azure/GCP)
- Hybrid search (Keyword + Semantic)

---

## Admin Dashboard 
<img width="537" height="273" alt="Screenshot 2024-04-15 221931" src="https://github.com/user-attachments/assets/cc9db634-ae89-46ec-8d76-509b17225e6f" />

---

## Employee Dashboard 
<img width="272" height="39" alt="Screenshot 2024-04-15 215209" src="https://github.com/user-attachments/assets/df99566f-be7c-4b19-99f9-d3cec95e52f8" />

---

## 👩‍💻 Author
**Angana Biswas**

**LinkedIn:**  
https://linkedin.com/in/angana-biswas-data-science




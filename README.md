
# 🏥 Medical Chatbot - AI-Powered Healthcare Assistant

An intelligent medical information chatbot powered by Retrieval-Augmented Generation (RAG) that provides accurate medical information sourced from The GALE Encyclopedia of Medicine.

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://medical-chatbot-c363.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌐 Live Demo

**[Try the Medical Chatbot →](https://medical-chatbot-c363.onrender.com)**

> ⚠️ **Disclaimer:** This chatbot is for informational purposes only. Always consult healthcare professionals for medical advice.

---

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Deployment](#-deployment)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Performance](#-performance)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- 🤖 **AI-Powered Responses**: Utilizes Llama 3.3 70B model via Groq API for accurate medical information
- 📚 **Knowledge Base**: Trained on The GALE Encyclopedia of Medicine for reliable medical content
- 🔍 **Semantic Search**: Vector database (Pinecone) for intelligent document retrieval
- ⚡ **Fast Response**: Average response time of 2-5 seconds after initial load
- 🎨 **User-Friendly Interface**: Clean, intuitive chat interface
- 🔒 **Privacy-Focused**: No user data storage, all queries processed in real-time
- 🌐 **24/7 Availability**: Cloud-hosted for continuous access

---

## 🛠️ Technology Stack

### **Backend**
- **Framework**: Flask 2.3.3
- **LLM**: Llama 3.3 70B (via Groq API)
- **Embeddings**: HuggingFace Sentence Transformers (all-MiniLM-L6-v2)
- **Vector Database**: Pinecone
- **Orchestration**: LangChain 0.3.10

### **Frontend**
- HTML5, CSS3, JavaScript
- Responsive design

### **Infrastructure**
- **Deployment**: Render (Docker)
- **Server**: Gunicorn
- **Environment**: Python 3.10

### **Key Libraries**
```
langchain==0.3.10
sentence-transformers==2.6.0
pinecone==7.3.0
torch==2.9.1 (CPU-optimized)
Flask==2.3.3
```

---

## 🏗️ Architecture

```
┌─────────────────┐
│   User Query    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│   Flask Web Application     │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  Sentence Transformers      │
│  (Query Embedding)          │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   Pinecone Vector DB        │
│   (Similarity Search)       │
│   Returns: Top 3 docs       │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   Groq API (Llama 3.3 70B)  │
│   Context + Query → Answer  │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────┐
│  User Response  │
└─────────────────┘
```

### **RAG Pipeline**
1. **Query Processing**: User question embedded using Sentence Transformers
2. **Document Retrieval**: Top 3 relevant chunks retrieved from Pinecone (k=3)
3. **Context Enhancement**: Retrieved documents used as context
4. **Response Generation**: Llama 3.3 70B generates answer based on context
5. **Output Delivery**: Formatted response returned to user

---

## 📦 Installation

### **Prerequisites**
- Python 3.10+
- pip
- Git

### **Local Setup**

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/Medical-Chatbot.git
cd Medical-Chatbot
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file:
```env
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

Get your API keys:
- **Pinecone**: [console.pinecone.io](https://console.pinecone.io)
- **Groq**: [console.groq.com/keys](https://console.groq.com/keys)

5. **Run the application**
```bash
python app_render.py
```

Visit: `http://localhost:8080`

---

## 🚀 Deployment

### **Deploy on Render**

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Create Render Account**
- Sign up at [render.com](https://render.com)
- Connect your GitHub account

3. **Create New Web Service**
- Select your repository
- Runtime: **Docker**
- Instance Type: **Free**

4. **Add Environment Variables**
```
PINECONE_API_KEY = your_key_here
GROQ_API_KEY = your_key_here
```

5. **Deploy**
- Render will automatically build and deploy
- Build time: ~10 minutes
- Your app will be live at: `https://your-app.onrender.com`

---

## 💡 Usage

### **Example Queries**

1. **General Medical Questions**
   - "What is diabetes?"
   - "What are the symptoms of hypertension?"

2. **Treatment Information**
   - "How is asthma treated?"
   - "What medications are used for depression?"

3. **Symptom Analysis**
   - "What could cause persistent headaches?"
   - "What are the signs of dehydration?"

### **Best Practices**
- Be specific with your questions
- One question at a time for best results
- First query may take 20-30 seconds (model loading)
- Subsequent queries: 2-5 seconds

---

## 📁 Project Structure

```
Medical-Chatbot/
│
├── app_render.py              # Main Flask application
├── Dockerfile                 # Docker configuration
├── requirements_render.txt    # Production dependencies
├── requirements.txt           # Development dependencies
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation
│
├── src/
│   └── helper.py             # Utility functions (embeddings, text splitting)
│
├── templates/
│   └── chat.html             # Chat interface
│
├── static/                   # CSS, JS, images
│
└── Data/                     # Medical documents (not in repo)
    └── *.pdf                 # GALE Encyclopedia PDFs
```

---

## ⚡ Performance

### **Response Times**
- **First Request**: 20-30 seconds (embedding model loading)
- **Subsequent Requests**: 2-5 seconds
- **Vector Search**: <1 second
- **LLM Generation**: 1-3 seconds

### **Scalability**
- **Free Tier Limits**:
  - Groq: 14,400 requests/day
  - Render: 750 hours/month
  - Pinecone: Based on index size

### **Memory Optimization**
- Lazy loading of embeddings (reduces startup time)
- CPU-optimized PyTorch (saves ~2GB RAM)
- Single Gunicorn worker (optimized for free tier)

---

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Voice input/output
- [ ] User authentication and history
- [ ] Medical image analysis
- [ ] Integration with telemedicine platforms
- [ ] Fine-tuned medical LLM
- [ ] Symptom checker with decision trees
- [ ] Drug interaction checker
- [ ] Appointment scheduling integration

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Your Name**  
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com
- Portfolio: [your-portfolio.com](https://your-portfolio.com)

---

## 🙏 Acknowledgments

- **The GALE Encyclopedia of Medicine** for providing comprehensive medical knowledge base
- **Groq** for fast LLM inference
- **Pinecone** for vector database services
- **HuggingFace** for embedding models
- **LangChain** for RAG orchestration

---

## 📊 Statistics

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/Medical-Chatbot)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/Medical-Chatbot)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/Medical-Chatbot)

---

⭐ **If you find this project helpful, please give it a star!** ⭐

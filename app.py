from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Initialize components
embeddings = download_hugging_face_embeddings()
docsearch = PineconeVectorStore.from_existing_index(
    index_name="medical-chatbot",
    embedding=embeddings
)

def get_medical_answer(question):
    try:
        # Get relevant documents from Pinecone
        docs = docsearch.similarity_search(question, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        
        # Call LM Studio
        response = requests.post(
            "http://localhost:1234/v1/chat/completions",
            json={
                "model": "llama-2-7b-chat",
                "messages": [
                    {
                        "role": "system", 
                        "content": "You are a helpful medical assistant. Use the context to answer questions accurately and always remind to consult doctors."
                    },
                    {
                        "role": "system",
                        "content": f"Medical Context: {context}"
                    },
                    {
                        "role": "user", 
                        "content": question
                    }
                ],
                "temperature": 0.3,
                "max_tokens": 500
            },
            timeout=45
        )
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"I apologize, but I'm having trouble processing your question. Please try again."

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    user_question = request.form["msg"]
    print(f"Question: {user_question}")
    
    answer = get_medical_answer(user_question)
    print(f"Answer: {answer}")
    
    return answer

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
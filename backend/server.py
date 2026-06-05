from flask import Flask, request, jsonify
from flask_cors import CORS

from src.rag_pipeline import get_rag_response
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return {
        "message": "GATE CSE RAG Assistant API Running"
    }
    
@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    question = data.get(
        "question"
    )

    if not question:

        return jsonify(
            {
                "error":"Question is required"
            }
        ),400
    answer = get_rag_response(
        question
    )
    return jsonify(
        {
            "answer": answer
        }
    )
if __name__ == "__main__":

    app.run(
        debug=True
    )
from flask import Flask, jsonify, request
from rag.chatbot import get_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/response', methods=['GET'])
def response():
    data = request.get_json()
    query = data.get('query')
    print("Query:", query)
    response = get_response(query)

    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)

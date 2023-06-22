from function import generate_chat_response 
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['POST'])
@cross_origin()
def get_chat_response():
    prompt = request.json.get('prompt')
    print(prompt + " PROMPT")
    if prompt:
        response = generate_chat_response(prompt)
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'No prompt provided.'}), 400
 
if __name__ == '__main__': 
    app.run(host='localhost', port=8080)

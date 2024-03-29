import os
from flask import Flask, render_template, request, send_from_directory
import os
from src.cffi_loader import demonstrate_mitigation, demonstrate_vulnerability

app = Flask(__name__)
GRAPHS_DIR = os.path.join(app.root_path, 'graphs')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Placeholder for authentication logic
    # WARNING: This example does not include secure authentication practices
    if username == "admin" and password == "password":
        return "Login Successful"
    else:
        return "Login Failed", 401

@app.route('/trigger-vulnerability')
def trigger_vulnerability():
    result = demonstrate_vulnerability()
    return f"Vulnerability Result: {result}"

@app.route('/trigger-mitigation')
def trigger_mitigation():
    result = demonstrate_mitigation()
    return f"Mitigation Result: {result}"

@app.route('/graphs/<filename>')
def serve_graph(filename):
    """
    Serve a graph image from the graphs directory.
    """
    return send_from_directory(GRAPHS_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

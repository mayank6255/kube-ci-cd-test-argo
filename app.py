from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Install dependencies listed in requirements.txt
    import os
    os.system('pip install -r requirements.txt')
    
    app.run(host='0.0.0.0', port=8080)

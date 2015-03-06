from flask import Flask
import requests 
app = Flask(__name__)

@app.route("/")
def hello():
    return "doh"

@app.route("/myip")
def myip():
    return requests.get ('http://eth0.me').content 
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    
from flask import Flask
app = Flask(__name__) #this feeds the name of the file to Flask 

@app.route("/")
def hello():
	return "Hello World!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
	

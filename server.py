from flask import Flask, render_template
app = Flask(__name__) #this feeds the name of the file to Flask 

@app.route("/")
def hello():
	return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)


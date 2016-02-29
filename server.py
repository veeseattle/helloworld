from flask import Flask, render_template
app = Flask(__name__) #this feeds the name of the file to Flask 

@app.route("/")
def hello():
	return render_template('template.html', my_string="Task Manager", my_list=["Memory Free","Compressed Mem","Ports","PID","User"])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)


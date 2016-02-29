from flask import Flask, render_template
import csv

app = Flask(__name__) #this feeds the name of the file to Flask 

@app.route("/")
def hello():
	with open('data.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		fieldnames = ('total', 'used', 'free', 'shared', 'buffers')
		return render_template('template.html', my_string=csvreader, my_list=["Memory Free","Compressed Mem","Ports","PID","User"])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)



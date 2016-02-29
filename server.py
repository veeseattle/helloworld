from flask import Flask, render_template, csv
app = Flask(__name__) #this feeds the name of the file to Flask 

@app.route("/")
def hello():
	with open('data.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in csvreader:
			print ', '.join(row)
	return render_template('template.html', my_string="My Data", my_list=["Memory Free","Compressed Mem","Ports","PID","User"])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)



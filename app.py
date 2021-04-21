from flask import Flask, render_template, redirect, url_for,request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
	return render_template("index.html")

@app.route('/home')
def red_home():
	return redirect('/')

@app.route('/predictor')
def predictor():

	#prediction = model.predict(feature_inputs)
	#print(prediction)
	return render_template("predictor.html")

@app.route('/result',methods=['POST'])
def result():
	feature_inputs=[]
	if request.method == 'POST':
		values = request.form.to_dict(flat=False)
		for k in values.items():
			key = k[0]
			if key == 'status' or key == 'dataplan':
				op = int(k[1][0])
				feature_inputs.append(op)
			else:
				op = float(k[1][0])
				feature_inputs.append(op)
		feature_inputs = np.array([feature_inputs])
		prediction = model.predict(feature_inputs)

		if prediction[0] == 1:
			return render_template("Yes.html")
		else:
			return render_template("No.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

if __name__ == '__main__':
	app.run(debug=True)

import pickle
lr = pickle.load(open("lr_c38.pkl","rb"))

import numpy as np
from flask import Flask,request,render_template

app =Flask(__name__)


@app.route("/")
def homepage():
	return render_template("index.html")
	####################################################################

@app.route("/salary_preiction",methods=['POST'])
def predict():
    pre_sal = lr.predict([[int(x) for x in request.form.values()]])
    return render_template("index.html",prediction_text = "Dsc37 Salary is "+str(pre_sal[0]))
    
    
    
    
if __name__=="__main__":
    app.run(port=5000,debug=True)
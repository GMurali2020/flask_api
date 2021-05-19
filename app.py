from flask import Flask,request
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/predict')
def banknotes_authen_predict():
    varience=request.args.get('varience')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[varience,skewness,curtosis,entropy]])
    return 'the answer is '+str(prediction)


@app.route('/predict_file',methods=['POST'])
def predict_file():
    data=request.files.get('file')
    test=pd.read_csv(data)
    prediction=classifier.predict(test)
    return str(list(prediction))





if __name__ == '__main__':
    app.run(debug=True)

import numpy as np
import pandas as pd
#import sklearn.linear_model.base
from flask import Flask, request, jsonify, render_template
#import pickle

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')
@app.route('/read-tuple')
def read_tuple():
    '''
    For rendering results on HTML GUI
    '''
    headings = ('sepal-length','sepal-width','petal-length','petal-width','class')
    data = (
        ('5.1','3.5','1.4','0.2','Iris-setosa'),
        ('4.9','3.0','1.4','0.2','Iris-setosa')
    )
    
    return render_template('tuple.html', headings = headings, data = data)#, prediction_text=f'The species is Iris:{output}',data=prediction)#.format(output))

@app.route('/read-dict')
def read_dict():

    df = pd.read_csv('dataset\iris.data')

    #print(type(df))

    data_dict = df.to_dict()
    for key,value in data_dict.items():
        print()
    l = len(data_dict[key])
    # print(data_dict)
    
    return render_template('dict.html', data_dict = data_dict, l= l)

@app.route('/read-df')
def read_df():

    df = pd.read_csv('dataset\iris.data')

    #print(type(df))
    headings = list(df[:0])
    data = list(df.to_records(index=False))



    # print(data_dict)

    return render_template('tuple.html', headings=headings, data=data)



if __name__ == "__main__":
    app.run(debug=True)
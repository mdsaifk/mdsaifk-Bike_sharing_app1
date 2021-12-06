
# importing the necessary dependencies
from flask_cors import CORS,cross_origin
from sklearn.ensemble import RandomForestRegressor
#import sklearn.linear_model.LinearRegression
from flask import Flask, request, jsonify,render_template
import os
from wsgiref import simple_server
from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
        
            #  reading the inputs given by the user
            season=float(request.form['season'])
            holiday = float(request.form['holiday'])
            workingday = float(request.form['workingday'])
            weather = float(request.form['weather'])
            temp = float(request.form['temp'])
            atemp = float(request.form['atemp'])
            humidity = float(request.form['humidity'])
            windspeed = float(request.form['windspeed'])
            casual = float(request.form['casual'])
            registered = float(request.form['registered'])
            hour = float(request.form['hour'])
            #is_research = request.form['research']
            #if(is_research=='yes'):
                #research=1
            #else:
                #research=0
            filename = 'finalized_new_bike_model.pickle'
            RF1 = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            #prediction=loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            prediction=RF1.predict([[season,holiday,workingday,weather,temp,atemp,humidity,windspeed,casual,registered,hour]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            #return render_template('results.html')
            return render_template('results.html',prediction=np.round(prediction))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    #clApp = ClientApp()
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host,port=port, app=app)
    httpd.serve_forever()
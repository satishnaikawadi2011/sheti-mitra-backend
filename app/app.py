from flask import Flask,request,Response, jsonify
import numpy as np
import pandas as pd
import pickle


from utils.validate_inputs import validate_recommend_crop_inputs

# Loading crop recommendation model

crop_recommendation_model_path = 'models/crop_recommendation_model.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))




app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!!!'

@app.route('/recommend_crop',methods=['POST'])
def recommend_crop():
    request_data = request.get_json();
    validation_res = validate_recommend_crop_inputs(request_data)
    print(validation_res)
    if(validation_res['is_valid']==False):
        return Response(validation_res['message'],status=400,mimetype='application/json')


    N = int(request_data['nitrogen'])
    P = int(request_data['phosphorous'])
    K = int(request_data['pottasium'])
    ph = float(request_data['ph'])
    rainfall = float(request_data['rainfall'])
    humidity = float(request_data['humidity'])
    temperature = float(request_data['temperature'])

    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = crop_recommendation_model.predict(data)
    res = int(prediction[0])
    return jsonify({'crop':res})


if __name__ == '__main__':
    app.run(debug=True)
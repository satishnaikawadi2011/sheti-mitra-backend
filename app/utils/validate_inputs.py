

def validate_recommend_crop_inputs(data):
    res = {'is_valid':True,'message':''}
    if 'nitrogen' not in data.keys():
        res['is_valid'] = False
        res['message'] = 'Please provide the ratio of nitrogen content in the soil!'
    if 'phosphorous' not in data.keys():
        res['is_valid'] = False
        res['message'] = 'Please provide the ratio of phosphorous content in the soil!'
    if 'pottasium' not in data.keys():
        res['is_valid'] = False
        res['message'] = 'Please provide the ratio of pottasium content in the soil!'
    if 'temperature' not in data.keys():
        res['is_valid'] = False
        res['message'] = 'Please provide the temperature in degree Celcius!'
    if 'humidity' not in data.keys():
        res['is_valid'] = False
        res['message'] = 'Please provide the relative humidity percentage!'
    if 'ph' not in data.keys():
        res['is_valid'] = False
        res['message'] = 'Please provide the ph value of the soil!'
    if 'rainfall' not in data.keys():
        res['is_valid'] = False
        res['message'] = 'Please provide the rainfall in mm!'

    return res
import json
import numpy as np
import joblib
from azureml.core.model import Model

def init():
    global model
    # Load the model from the registered path
    model_path = Model.get_model_path('iris_model')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        # Parse the input data
        data = np.array(json.loads(raw_data)['data'])
        # Make prediction
        prediction = model.predict(data)
        return json.dumps({'result': prediction.tolist()})
    except Exception as e:
        return json.dumps({'error': str(e)})

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
model._make_predict_function()

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = np.array([int(x) for x in request.form.values()]).reshape(1,-1)
    # print(int_features)
    final_features = [np.array(int_features)]
    # model
    prediction = model.predict(int_features)

    output = round(prediction[0], 2)
    # output = int_features = np.array([int(x) for x in request.form.values()]).reshape(1,-1)

    return render_template('main.html', output=output)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
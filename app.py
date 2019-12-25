import numpy as np
from operator import itemgetter
from flask import Flask, request, jsonify, render_template, redirect
import pickle
from flask_pymongo import PyMongo
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='yoursecretkey'))
# db connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/project"
mongo = PyMongo(app)
user_id = 3

@app.route('/projects', methods = ['POST']) 
def createProject():
    form = request.form
    
    project = {'title':form['title'], 'info':form['info'], 'place':form['place'], 'deadline':form['deadline'], 'place':form['place'],'created_date': datetime.now().isoformat()}
    projects_amount = len(mongo.db.gtd.find({'user_id':user_id})[0]['warehouse']['projects'])
    print(f'UPDATING {user_id} with {project}, projects amount:{projects_amount}')
    mongo.db.gtd.update_one(
        {"user_id": user_id},
        {"$set":
            {f"warehouse.projects.{projects_amount}": project}
        }
    )
    return redirect('/')

@app.route('/projects', methods = ['PUT']) 
def updateProject():
    values = request.form.values()
    print(request.form['title'])
    form = request.form
    
    project = {'title':form['title'], 'info':form['info'], 'place':form['place'], 'deadline':form['deadline'], 'place':form['place'],'created_date': datetime.now().isoformat()}
    projects_amount = len(mongo.db.gtd.find({'user_id':user_id})[0]['warehouse']['projects'])
    print(f'UPDATING {user_id} with {project}, projects amount:{projects_amount}')
    mongo.db.gtd.update_one(
        {"user_id": user_id},
        {"$set":
            {f"warehouse.projects.{projects_amount}": project}
        }
    )
    return redirect('/')

@app.route('/projects/<title>', methods=['DELETE'])
def deleteProject(title):
	mongo.db.gtd.deleteOne({'user_id':user_id}, {'title': title})
	resp = jsonify('Project deleted successfully!')
	resp.status_code = 200
	return resp

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # int_features = np.array([int(x) for x in request.form.values()]).reshape(1,-1)
    # # print(int_features)
    # final_features = [np.array(int_features)]
    # # model
    # prediction = model.predict(int_features)

    # output = round(prediction[0], 2)*100
    # output = int_features = np.array([int(x) for x in request.form.values()]).reshape(1,-1)

    return render_template('main.html')

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

@app.route('/', methods = ['GET', 'POST'])
def home():
    # read all data
    user_id = 3
    form = request.form
    if int(form.get('id'))>0:
            user_id = int(form['id'])
            print(f'USSEEER ID: {int(form["id"])}')

    docs = mongo.db.gtd.find({'user_id':user_id})[0]['warehouse']['projects']
    projects = []
    for i in docs:
        projects.append(i)
    projects.sort(key=itemgetter('created_date'), reverse=True)
    return render_template('index.html',projects = projects)

if __name__ == "__main__":
    app.run(debug=True)
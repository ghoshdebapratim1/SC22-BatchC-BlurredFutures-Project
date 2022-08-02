# import requirements needed
import sys
import subprocess
import flask
from flask import Flask, render_template
from utils import get_base_url
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sklearn'])
import sklearn
import pickle
import requests


# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12345
base_url = get_base_url(port)

# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

model = pickle.load(open('model.pkl','rb'))


# set up the routes and logic for the webserver
@app.route(f'{base_url}')
def home():
    return render_template('index-TEST.html')

@app.route(f'{base_url}/predict',methods=['POST'])
def predict():
    output = request.form.values()
    return render_template('index.html', prediction_text='Value is {}'.format(output))

    # int_features = [int(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
# 
#     output = round(prediction[0], 2)
# 
#     return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))

# define additional routes here
# for example:
# @app.route(f'{base_url}/team_members')
# def team_members():
#     return render_template('team_members.html') # would need to actually make this page

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc6.ai-camp.dev'
    
    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host = '0.0.0.0', port=port, debug=True)

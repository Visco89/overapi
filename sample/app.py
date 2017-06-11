from flask import Flask, request
import core
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to overapi!"

@app.route('/overapi/v1.0/<name>/<id>/generic_stats', methods=['GET'])
def get_generic_stats(name, id):
    user = name + '-' +id
    resp = {}
    try:
        resp['result'] = core.generic_stats(user);
    except requests.exceptions.HTTPError as err:
        return str({"status" : "KO", "error" : str(err)})
    resp["status"] = "OK";
    return str(resp)

@app.route('/overapi/v1.0/<name>/<id>/featured_stat', methods=['GET'])
def get_featured_stat(name, id):
    user = name + '-' +id
    mode = request.args.get('mode', '')
    resp = {}
    if mode != '' and mode != "competitive" and mode != "quickplay":
        return str({"status" : "KO", "error" : "incorrect mode"})
    try:
        resp['result'] = core.featured_stat(user) if mode == "" else core.featured_stat(user, mode)
    except requests.exceptions.HTTPError as err:
        return str({"status" : "KO", "error" : str(err)})
    if mode=="competitive" and (resp == None or resp == {}):
        return str({"status": "KO", "error": "no competitive data"})
    resp["status"] = "OK";
    return str(resp)

@app.route('/overapi/v1.0/<name>/<id>/top_heroes', methods=['GET'])
def get_top_heroes(name,id):
    user = name + '-' + id
    mode = request.args.get('mode', '')
    category = request.args.get('category', '')
    #TODO

if __name__ == '__main__':
    app.run(debug=True)
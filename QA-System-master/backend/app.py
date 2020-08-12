from flask import Flask, request, jsonify
from flask_cors import CORS
from q_a_transformers import question_answer
from pymongo import MongoClient, errors
import os
import json
import pandas as pd


app = Flask(__name__)
CORS(app)

app.config.from_object("config")

"""
Connect to database and print error
if anything wrong
"""
try:
    db_domain = 'localhost:'
    db_port = 27017
    db_name = 'qa'
    client = MongoClient(
        host=[str(db_domain) + str(db_port)],
        serverSelectionTimeoutMS=3000
        )
except errors.ServerSelectionTimeoutError as err:
    client = None
    print("pymongo ERROR:", err)


@app.route("/answer", methods=["GET"])
def get_answer():
    """
    Return answer with json format after recevied
    domain and question from frontend
    """
    r_data = request.args.to_dict()
    domain_name = r_data["domain"]
    print(f'Domain is {domain_name}')
    question = r_data["question"]
    print(f'Question is {question}')
    print('========================')
    print('Retrieving answer ...')
    answer = question_answer(domain_name, question)
    return jsonify({'answer': answer}), 200


@app.route("/load/data", methods=["GET"])
def load_data():
    """
    Load data from csv files under path files/data
    to database
    """
    files = None
    try:
        files = os.listdir(app.config["DATA_FILES_FOLDER"])
    except FileNotFoundError as err:
        print(err)

    if client is not None and files is not None and files != []:
        db = client[db_name]
        for filename in files:
            coll_name = filename.replace(".csv", "")
            coll = db[coll_name]
            if filename == '.DS_Store':
                continue
            csv_path = os.path.join(app.config["DATA_FILES_FOLDER"], filename)
            print('==================================================')
            print(f'Read and load data from file {filename} to db ...')
            data = pd.read_csv(csv_path)
            payload = json.loads(data.to_json(orient='records'))
            coll.remove()
            coll.insert_many(payload)
        print('=================================================')
        print('Done')
        return "Data is loaded from csv files to database.", 200
    return "ERROR: No database or no data files under files/data", 516


@app.route("/domain", methods=["GET"])
def get_domain():
    """
    Get domain information from database
    which is stored as collection name
    """
    """
    Comment this part and waiting for the team member who owns
    backend to decide how to organize feather file.
    if client is not None:
        collection_names = client['qa'].list_collection_names()
        return json.dumps(collection_names), 200
    """
    return json.dumps(["op"])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

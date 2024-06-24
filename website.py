from flask import Flask, jsonify
import pymongo

app = Flask(__name__)


def get_data_from_mongodb(uri, database_name, collection_name):
    client = pymongo.MongoClient(uri)
    db = client[database_name]
    collection = db[collection_name]
    data = list(collection.find({}, {'_id': 0}))
    client.close()
    return data


@app.route('/api/data')
def get_data():
    data = get_data_from_mongodb('mongodb://localhost:27017/', 'wiki_db', 'wiki_collection')
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
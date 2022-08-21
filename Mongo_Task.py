from flask import Flask,request,jsonify
import pymongo


client = pymongo.MongoClient("mongodb+srv://ineuron:ineuron@cluster0.bgcr20g.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['taskdb']
collection = database['taskcollection']

app = Flask(__name__)


@app.route("/insert/mongo", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("succefully inserted "))

@app.route('/update/mongo',methods=['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        #collection.update_one()
        return jsonify(str("updated successfully"))

if __name__ == '__main__':
    app.run()

import flask
import db

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>API Flask</h1>"


@app.route('/api/personnes', methods=['GET'])
def getPersonnes():
    return db.getPersonnes()


@app.route('/api/add_personnes', methods=['GET', 'POST'])
def postPersonnes():
    return db.postPersonnes()


@app.route('/api/upd_personnes', methods=['PUT'])
def updPersonnes():
    return db.updPersonnes()


@app.route('/api/del_personnes', methods=['DELETE'])
def delPersonnes():
    return db.delPersonnes()


app.run()
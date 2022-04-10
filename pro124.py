from flask import Flask, request, jsonify

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': u'Siamlaz',
        'contact': 1234567890,
        'done': False
    },
    {
        'id': 2,
        'name': u'niamlaz',
        'contact': 1987654320,
        'done': False
    }
]


@app.route("/")
def printdata():
    return jsonify({
        "data": contacts
    })


@app.route("/addcontact", methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "provide the data or this thing will not work!"
        },400)
    contact = {
        'id': contacts[-1]['id']+1,
        'name': request.json['Name'],
        'contact': request.json.get('Contact',""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "the data has been added succesfully, now this thing will work!"
    })


if __name__ == "__main__":
    app.run(debug=True)

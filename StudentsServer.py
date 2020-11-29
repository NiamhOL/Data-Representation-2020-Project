from flask import Flask, jsonify, abort, render_template, request, redirect, url_for, session,flash
from members import members
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='.', template_folder="")
CORS(app)

app.secret_key = 'super secret key'

@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # I have set the username and password here to test
        if request.form['username'] != 'test' or request.form['password'] != 'test':
            # If UN and PW are not true Print
            error = 'Invalid Credentials. Please try again.'
        else:
            # Send to index page of the site if UN and PW = True
            return render_template("/index.html")
    return render_template("login.html", error=error)

@app.route('/membershi', methods=['GET', 'POST'])
def membership():
        return render_template('meducatestudentmembership.html')
#curl "http://127.0.0.1:5000/members"
@app.route('/members')
def getAll():
    #print("in getall")
    results = memberDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/members/2"
@app.route('/members/<int:id>')
def findById(id):
    foundMember = memberDAO.findByID(id)

    return jsonify(foundMember)



@app.route('/members', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    member = {
        "email": request.json['email'],
        "membershipPlan": request.json['membershipPlan'],
        "startDate": request.json['startDate'],
        
    }
    values =(member['email'], member['membershipPlan'], member['startDate'])
    newId = memberDAO.create(values)
    member['id'] = newId
    return jsonify(member)

def update(id):
    foundMember = memberDAO.findByID(id)
    if not foundMember:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    
    if 'email' in reqJson:
        foundMember['email'] = reqJson['email']
    if 'membershipPlan' in reqJson:
        foundMember['membershipPlan'] = reqJson['membershipPlan']
    if 'startDate' in reqJson:
        foundMember['startDate'] = reqJson['startDate']
    
    values = (foundMember['email'], foundMember['membershipPlan'], foundMember['startDate'], foundMember['age'], foundMember['id'])
    memberDAO.update(values)
    return jsonify(foundMember)
        
#  curl -X DELETE http://localhost:5000/members/2
@app.route('/members/<int:id>' , methods=['DELETE'])
def delete(id):
    memberDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)

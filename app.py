from flask import Flask, render_template, url_for, request, jsonify
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('form.html')
 
@app.route('/process', methods=['POST'])
def process():
 
    email = request.form['email']
    name = request.form['name']
     
    if name and email:
        newName = name
 
        return jsonify({'name' : newName})
 
    return jsonify({'error' : 'Missing data!'})
     
@app.route('/mus')
def index1():
    return render_template('form1.html')

    
@app.route('/process1', methods=['POST'])
def process1():
 
    email = request.form['email']
    name = request.form['name']
     
    if email and name:
        newName = int(name) + int(email)
 
        return jsonify({'sum' : newName})
 
    return jsonify({'error' : 'hado machi number!'})

if __name__ == '__main__':
    app.run(debug=True)
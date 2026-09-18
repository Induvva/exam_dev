from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/') 
def hello_world():
    return "<center>Hello!<br><a href='/register'>Register</a></center>"
@app.route('/success/<name>/<roll_no>')
def success(name, roll_no):
    return render_template('success.html', name=name, roll_no=roll_no)
@app.route('/register', methods=['GET'])
def register_get():
    return render_template('register.html')
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    roll_no = request.form['roll_no']
    email = request.form['email']
    year = request.form['year']
    return redirect(url_for('success', name=name, roll_no=roll_no))
if __name__ == '__main__':
    app.run(debug=True)
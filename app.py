from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
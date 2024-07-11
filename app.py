from flask import Flask, render_template,request
import mysql.connector as sql



app = Flask(__name__)

con = sql.connect(host="localhost", user="root", password="Narenguru2007", database="new_project")

cur = con.cursor()
cur.execute('select tid,tpass from teacher')
tdata = cur.fetchall()


tids = [str(i[0]) for i in tdata]
tpass = [i[1] for i in tdata]

cur.execute('select sid,spass from studentbio')
sdata = cur.fetchall()
sids = [str(i[0]) for i in sdata]
spass = [i[1] for i in sdata]


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('pass')
        if id and password:
            if id.lower()=='admin' and password.lower()=='admin':
                return render_template('admin.html')
            elif id in tids:
                tpassindex = tids.index(id)
                if password.lower() == tpass[tpassindex]:
                    return render_template('teacher.html')
                else:
                    return "<h1 style='text-align:center'>Invalid password </h1>"
            elif id in sids:
                spassindex = sids.index(id)
                if password.lower() == spass[spassindex]:
                    return render_template('student.html')
                else:
                    return "<h1 style='text-align:center'>Invalid password </h1>"
            else:
                return "<h1 style='text-align:center'>Invalid Id </h1>"
        else:
            return "<h1 style='text-align:center'>Id or Password is not entered </h1>"

@app.route('/studentdata')
def studentdata():
    return render_template('admin_studentdata.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

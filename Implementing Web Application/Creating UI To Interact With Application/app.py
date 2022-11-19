from flask import Flask,redirect,url_for,render_template,request,make_response
import ibm_db


conn = ibm_db.connect('DATABASE=bludb;'
                     'HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;'
                     'PORT=32328;'
                     'PROTOCOL=TCPIP;'
                     'SECURITY=SSL;'
                     'SSLServerCertificate=DigiCertGlobalRootCA.crt;'
                     'UID=bmb02607;'
                     'PWD=9qglrICwkM11bGTw;', '', ''
)
print("connection successful...")
app = Flask(__name__)




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        sql = "select * from login where username=? and pass=?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt, 2, password)
        ibm_db.execute(stmt)
        dic = ibm_db.fetch_assoc(stmt)
        print(dic)
        if dic:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

    elif request.method=='GET':
        return render_template('login.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        roll_no = request.form['roll_no']
        sex = request.form['sex']
        age = request.form['age']
        address = request.form['address']
        blood_group = request.form['blood_group']
        sql = "insert into signup values(?,?,?,?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(prep_stmt,1,username)
        ibm_db.bind_param(prep_stmt,2,email)
        ibm_db.bind_param(prep_stmt,3,password)
        ibm_db.bind_param(prep_stmt,4,roll_no)
        ibm_db.bind_param(prep_stmt,5,sex)
        ibm_db.bind_param(prep_stmt,6, age)
        #ibm_db.bind_param(prep_stmt,7, "USER")
        ibm_db.bind_param(prep_stmt,7, address)
        ibm_db.bind_param(prep_stmt,8, blood_group)
        ibm_db.execute(prep_stmt)
        #db post operation
        return redirect(url_for('login'))
    elif request.method=='GET':
        return render_template('signup.html')


if __name__=='__main__':
    app.run(debug = True)

from flask import Flask, render_template,request,redirect,url_for,session
import ibm_db
import sendgrid
import os
from sendgrid.helpers.mail import *
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=gkl74127;PWD=FcoL07shOWN7YIem",'','')

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register',methods=['GET', 'POST'])
def register():
    session['msg']=""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phno = request.form['phno']
        dob = request.form['dob']
        gender = request.form['gender']
        bloodgroup = request.form['bloodgroup']
        weight = request.form['weight']
        password = request.form['newpassword']
        
        sql = "SELECT * FROM Members WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        
        if account:
            session['msg']= 'Account already exists'
            return redirect(url_for("login"))  
        else:
            insert_sql = ("INSERT INTO Members (NAME,EMAIL,PHNO,DOB,GENDER,BLOODGROUP,WEIGHT,PASSWORD)VALUES (?,?,?,?,?,?,?,?)")
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, phno)
            ibm_db.bind_param(prep_stmt, 4, dob)
            ibm_db.bind_param(prep_stmt, 5, gender)
            ibm_db.bind_param(prep_stmt, 6, bloodgroup)
            ibm_db.bind_param(prep_stmt, 7, weight)
            ibm_db.bind_param(prep_stmt, 8, password)
            ibm_db.execute(prep_stmt)
            session['msg']= 'Account created Successfully '
            sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
            from_email = Email("910019106033@student.autmdu.in")
            to_email = To(email)
            subject = "Plasma Donor App"
            content = Content("text/plain", "You are successfully registered to Plasma Donor App")
            mail = Mail(from_email, to_email, subject, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return redirect(url_for("login"))
     
    
    return render_template('register.html') 


@app.route('/login',methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['newpassword']
        
        
        sql = "SELECT * FROM Members WHERE Email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_both(stmt)
        
        accounts=account
        
        
        if (account):
            if  (password == accounts['PASSWORD'] ):
                return render_template('accounts.html',name=account['NAME'])
            else :
                return render_template('login.html',msg='wrong Password')
        else :
            return render_template('login.html',msg='wrong credentials')

            
    else:
        return  render_template('login.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')   

@app.route('/view2')
def view2():
    return render_template('view2.html')   

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/request1',methods=['GET', 'POST'])
def request1():
    session['msg']=""
    if request.method == 'POST':
        patientname = request.form['patientname']
        bloodgroupneeded = request.form['bloodgroupneeded']
        reasonforneed = request.form['reasonforneed']
        hospitalname = request.form['hospitalname']
        hospitaladdress = request.form['hospitaladdress']
        hospitalno = request.form['hospitalno']
        patientgender = request.form['patientgender']
        contactno = request.form['contactno']
        email = request.form['email']
        insert_sql = "INSERT INTO Requesters VALUES (?,?,?,?,?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, patientname)
        ibm_db.bind_param(prep_stmt, 2, bloodgroupneeded)
        ibm_db.bind_param(prep_stmt, 3, reasonforneed)
        ibm_db.bind_param(prep_stmt, 4, hospitalname)
        ibm_db.bind_param(prep_stmt, 5, hospitaladdress)
        ibm_db.bind_param(prep_stmt, 6, hospitalno)
        ibm_db.bind_param(prep_stmt, 7, patientgender)
        ibm_db.bind_param(prep_stmt, 8, contactno)
        ibm_db.bind_param(prep_stmt, 9, email)
        ibm_db.execute(prep_stmt)
        session['msg']= 'Request Placed Successfully '
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("910019106033@student.autmdu.in")
        to_email = To(email)
        subject = "Plasma Donor App-Request"
        content = Content("text/plain", "Your Request is under review")
        mail = Mail(from_email, to_email, subject, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)

    return render_template('request.html')
           
@app.route('/donate')
def donate():
    session['msg']=""
    if request.method == 'POST':
        fitness = request.form['fitness']
        disease = request.form['disease']
        vaccination = request.form['vaccination']
        agreement = request.form['agreement']
        sharecontact = request.form['sharecontact']
        insert_sql = "INSERT INTO Donors VALUES (?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, fitness)
        ibm_db.bind_param(prep_stmt, 2, disease)
        ibm_db.bind_param(prep_stmt, 3, vaccination)
        ibm_db.bind_param(prep_stmt, 4, agreement)
        ibm_db.bind_param(prep_stmt, 5, sharecontact)
        session['msg']= 'Your Donorship is under review '
    return render_template('readytodonate.html')   

@app.route('/readytodonate')
def readytodonate():
    return render_template('readytodonate.html')                    

@app.route('/profile')
def profile():
    return render_template('profile.html') 

@app.route('/about')
def about():
    return render_template('about.html')    
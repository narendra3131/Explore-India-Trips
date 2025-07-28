from flask import Flask,render_template,request,redirect,session
from pymongo import MongoClient

client=MongoClient('127.0.0.1',27017)
db=client['Jagu']
collection=db['Temples']
collection=db['Sports']
collection=db['Historical']
collection=db['Beaches']
collection=db['National_Parks']
collection=db['Mountains']

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('main.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/piligrim')
def piligrim():
   return render_template('piligrim.html') 

@app.route('/sports')
def sports():
   return render_template('sports.html')

@app.route('/hist')
def historical():
   return render_template('history.html') 

@app.route('/beach')
def beach():
   return render_template('beach.html') 

@app.route('/nat')
def national():
   return render_template('parks.html') 

@app.route('/mount')
def mount():
   return render_template('mountain.html') 

@app.route('/pay')
def pay():
    return render_template('hi.html')
@app.route('/piligrim',methods=['POST'])
def td():
    fname=request.form['fname']
    lname=request.form['lname']
    aad=request.form['aad']
    gender=request.form['gender']
    phone=request.form['phone']
    email=request.form['email']
    address=request.form['address']
    totalno=request.form['totalno']
    booking=request.form['booking']
    visit=request.form['visit']
    package=request.form['package']
    print(fname,lname,aad,gender,phone,email,address,totalno,booking,visit,package)
    
    
    # for i in collection.find():
    #     if i['rollno']==rollno:
    #         return render_template('home.html', error='you have already registered')
    k={}
    k['fname']=fname
    k['lname']=lname
    k['aad']=aad
    k['gender']=gender
    k['phone']=phone
    k['email']=email
    k['address']=address
    k['totalno']=totalno
    k['booking']=booking
    k['visit']=visit
    k['package']=package
    db.Temples.insert_one(k)
    print("Inserted Sucessfully")
    return render_template('hi.html',result='you have registered successfully')
    # return "hello"
    
@app.route('/sports',methods=['POST'])
def sd():
    fname=request.form['fname']
    lname=request.form['lname']
    aad=request.form['aad']
    gender=request.form['gender']
    phone=request.form['phone']
    email=request.form['email']
    address=request.form['address']
    totalno=request.form['totalno']
    booking=request.form['booking']
    visit=request.form['visit']
    package=request.form['package']
    print(fname,lname,aad,gender,phone,email,address,totalno,booking,visit,package)
    
    k={}
    k['fname']=fname
    k['lname']=lname
    k['aad']=aad
    k['gender']=gender
    k['phone']=phone
    k['email']=email
    k['address']=address
    k['totalno']=totalno
    k['booking']=booking
    k['visit']=visit
    k['package']=package
    db.Sports.insert_one(k)
    print("Inserted Sucessfully")
    return render_template('hi.html',result='you have registered successfully')

@app.route('/hist',methods=['POST'])
def hd():
    fname=request.form['fname']
    lname=request.form['lname']
    aad=request.form['aad']
    gender=request.form['gender']
    phone=request.form['phone']
    email=request.form['email']
    address=request.form['address']
    totalno=request.form['totalno']
    booking=request.form['booking']
    visit=request.form['visit']
    package=request.form['package']
    print(fname,lname,aad,gender,phone,email,address,totalno,booking,visit,package)
    
    k={}
    k['fname']=fname
    k['lname']=lname
    k['aad']=aad
    k['gender']=gender
    k['phone']=phone
    k['email']=email
    k['address']=address
    k['totalno']=totalno
    k['booking']=booking
    k['visit']=visit
    k['package']=package
    db.Historical.insert_one(k)
    print("Inserted Sucessfully")
    return render_template('hi.html',result='you have registered successfully')

@app.route('/beach',methods=['POST'])
def bd():
    fname=request.form['fname']
    lname=request.form['lname']
    aad=request.form['aad']
    gender=request.form['gender']
    phone=request.form['phone']
    email=request.form['email']
    address=request.form['address']
    totalno=request.form['totalno']
    booking=request.form['booking']
    visit=request.form['visit']
    package=request.form['package']
    print(fname,lname,aad,gender,phone,email,address,totalno,booking,visit,package)
    
    k={}
    k['fname']=fname
    k['lname']=lname
    k['aad']=aad
    k['gender']=gender
    k['phone']=phone
    k['email']=email
    k['address']=address
    k['totalno']=totalno
    k['booking']=booking
    k['visit']=visit
    k['package']=package
    db.Beaches.insert_one(k)
    print("Inserted Sucessfully")
    return render_template('hi.html',result='you have registered successfully')

@app.route('/nat',methods=['POST'])
def nd():
    fname=request.form['fname']
    lname=request.form['lname']
    aad=request.form['aad']
    gender=request.form['gender']
    phone=request.form['phone']
    email=request.form['email']
    address=request.form['address']
    totalno=request.form['totalno']
    booking=request.form['booking']
    visit=request.form['visit']
    package=request.form['package']
    print(fname,lname,aad,gender,phone,email,address,totalno,booking,visit,package)
    
    k={}
    k['fname']=fname
    k['lname']=lname
    k['aad']=aad
    k['gender']=gender
    k['phone']=phone
    k['email']=email
    k['address']=address
    k['totalno']=totalno
    k['booking']=booking
    k['visit']=visit
    k['package']=package
    db.National_Parks.insert_one(k)
    print("Inserted Sucessfully")
    return render_template('hi.html',result='you have registered successfully')
    
@app.route('/mount',methods=['POST'])
def md():
    fname=request.form['fname']
    lname=request.form['lname']
    aad=request.form['aad']
    gender=request.form['gender']
    phone=request.form['phone']
    email=request.form['email']
    address=request.form['address']
    totalno=request.form['totalno']
    booking=request.form['booking']
    visit=request.form['visit']
    package=request.form['package']
    print(fname,lname,aad,gender,phone,email,address,totalno,booking,visit,package)
    
    k={}
    k['fname']=fname
    k['lname']=lname
    k['aad']=aad
    k['gender']=gender
    k['phone']=phone
    k['email']=email
    k['address']=address
    k['totalno']=totalno
    k['booking']=booking
    k['visit']=visit
    k['package']=package
    db.Mountains.insert_one(k)
    print("Inserted Sucessfully")
    return render_template('hi.html',result='you have registered successfully')
# @app.route('/login', methods=['POST'])
# def logindata():
#     rollno=request.form['rollno']
#     password=request.form['password']
#     print(rollno,password)
#     for i in collection.find():
#         if (i['rollno']==rollno) and (i['password']==password):
            # session['username']=rollno
#             return render_template('dash.html')
        
#     return render_template('login.html',er='you have entered incorrect password')

# @app.route('/logout')
# def logout():
    # session['username']=None
    # return redirect('/login')

# @app.route('/homepage')
# def homepage():
#     return redirect('/dash')


# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/feedback')
# def feed():
#     return render_template('feedback.html')
            


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5001,debug=False)

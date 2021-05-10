from flask import Flask,render_template,url_for,request,redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from Mailing_list import mailing

app = Flask(__name__)

@app.route('/part_register', methods = ['POST','GET'])
def index():
    return render_template("part_register.html")


@app.route('/frosthack')
def do():
    if request.method=="POST":

        part_name = request.form['pName']
        email = request.form['pmail']
        cont = request.form['pcontact']
        e_name = request.form['eName']
        ev_id = request.form['e_id']
    else:
        return render_template("frosthack.html")


@app.route('/submit', methods = ['POST','GET'])
def sub():
    if request.method=="POST":

        part_name = request.form['pName']
        email = request.form['pmail']
        cont = request.form['pcontact']
        e_name = request.form['eName']
        ev_id = request.form['e_id']
        
        return redirect('/frosthack')

    part = mailing()
    part.mail_part_reg(part_name,e_name,"12/7/21","12:30","567",ev_id,"goldenrings.2020@gmail.com",email,"Snigdha")



if __name__=="__main__":
    app.run(debug=True, port=5000)
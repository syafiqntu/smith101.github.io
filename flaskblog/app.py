from flask import Flask, render_template, request,redirect
from flask_bootstrap import Bootstrap
from flask_wtf import Form,FlaskForm
from wtforms import validators,StringField,SubmitField

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "123456789"


class loginform(FlaskForm):
    team_name = StringField("Team Name",validators=[validators.DataRequired()])
    contact = StringField("Contact",validators=[validators.DataRequired(),validators.Length(10,10,message="Invalid")])


name=""
contact=""
code_question1 = '''
#include<iostream>
using namespace std;
int main()
{
    cout<<"Hello world";
}
'''

questions = {1:"On a 32 bit processor, what is the size of int ?",
2:'Find the output'+code_question1,
3:'2+2 is ?'}
choices = {1:['2 bytes','3 bytes','4 bytes','5 bytes'],2:['Hello world','No hellos','Error','Bye world'],3:['2','3','4','5','6']}
answers = {1:'4 bytes',2:'Hello world',3:'4'}

@app.route("/")
def welcome():
    form = loginform(request.form)
    return render_template("index.html",form = form)

@app.route("/login",methods=["POST"])
def login():
    form = loginform(request.form)
    if request.method=="POST":
        global name
        name = form.team_name.data
        global contact
        contact = form.contact.data
    return redirect("/questions")

@app.route("/questions")
def quiz():
    return render_template("Questions.html",q = questions,c = choices)

@app.route('/quiz', methods=['POST'])
def quiz_answers():
 correct = 0
 for key,value in request.form.items():
    if value == answers[int(key)]:
        correct = correct + 1
 print(correct)
 return render_template("result.html",teamname=name,contact=contact,score = correct)

if __name__ == '__main__':
 app.run(debug=True)
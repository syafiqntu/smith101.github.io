from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
        
        'title': 'What is a Smith Chart?',

        'content': 'A Smith chart is a circular plot with a lot of interlaced circles on it.' 
                   ' When used correctly, matching impedances, with apparent complicated structures,' 
                   ' can be made without any computation. The only effort required is the reading and' 
                   ' following of values along the circles.',

        'content2': 'The Smith Chart is a fantastic tool for visualizing the impedance of a transmission line' 
                    ' and antenna system as a function of frequency. Smith Charts can be used to increase understanding'
                    ' of transmission lines and how they behave from an impedance viewpoint. Smith Charts are also extremely'
                    ' helpful for impedance matching, as we will see. The Smith Chart is used to display an actual (physical)' 
                    ' antenna impedance when measured on a Vector Network Analyzer (VNA).',

        
    
    }
]

posts2 = [
    {
        

        'title': 'Plotting a smith chart:',

        'content': 'Find normalized source and load impedance',

        'content2':'Plot circles of constant resistance (z) and conductance (y) that pass through the source impedance.',

        'content3':'Plot circles of constant resistance and conductance that pass through the complex conjugate of the load impedance.',

        'content4':'The number of the intersection points between the circles in steps 2 an 3 determines the number of possible L-section matching network.', 

        'content5':'Find the values of normalized reactances and susceptances of the inductors and capacitors by tracing a path along the circles from the source impedance to the intersection point and then to the complex conjugate of the load.',
        
        'content6':'Find the actual inductor and capacitor at the frequency.',

        
    
    }
]


posts4 = [
    {
        
    
    }
]

posts5 = [
    {
      

        
    
    }
]

posts6 = [
    {
      

        
    
    }
]

posts3 = [
    {
        'author': 'Admin (Syafiq)',

        'title': 'External Links',

        'content': 'Smith Chart 101',

        'date_posted': 'April 20, 2018'
    
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, posts2=posts2)


@app.route("/Tutorial")
def quiz():
    return render_template('tutorial.html', title='Tutorial', posts4=posts4, posts5=posts5, posts6=posts6)

@app.route("/external")
def external():
    return render_template('external.html', title='External Links', posts3=posts3)



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)




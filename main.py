
from flask import Config, Flask,render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy


myapp=Flask(__name__)
myapp.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ply.sqlite3"
myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy()
db.init_app(myapp)

class Customer(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    mobile=db.Column(db.Integer)
    city= db.Column (db.String)
    wp=db.Column(db.Boolean)

    def __str__(self):
        return self.name


@myapp.route("/")
def home():
    return render_template("home.html")

@myapp.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=="POST":
        uname=request.form['name']
        umobile=request.form['mobile']
        ucity=request.form['city']
        uwp=request.form['wp']
        if uwp=='on':
            uwp=True
            c=Customer(name=uname,mobile=umobile,city=ucity,wp=uwp)
            db.session.add(c)
            db.session.commit()
            return redirect("/")
        else:
            uwp=False
            c=Customer(name=uname,mobile=umobile,city=ucity,wp=uwp)
            db.session.add(c)
            db.session.commit()
            return redirect("/")
    return render_template("contact.html")

@myapp.route("/projects")
def projects():
    return render_template("projects.html")

@myapp.route("/Pune")
def pune():
    return render_template("pune.html")

@myapp.route("/Mumbai")
def mumbai():
    return render_template("mumbai.html")

@myapp.route("/Nashik")
def nashik():
    return render_template("nashik.html")

@myapp.route("/about")
def about():
    return render_template("about.html")

@myapp.route("/Estimate")
def estimate():
    return render_template("estimate.html")    

if __name__ == "__main__":
    myapp.app_context( ).push()
    db.create_all()
    myapp.run(debug=True)    
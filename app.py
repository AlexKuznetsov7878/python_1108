from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hobby = db.Column(db.String(100), unique=False, nullable=True)
    def __str__(self):
        return f"Name:{self.first_name}, Age:{self.age}"

@app.route("/profiles/")
def profiles():
    my_profiles = Profile.query.all()
    print(my_profiles)
    return render_template("profiles.html",
                           profiles=my_profiles)

@app.route("/signup/", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        age = request.form.get("age")
        hobby = request.form.get("hobby")
        profile = Profile(first_name=fname,
                          last_name=lname, age=age,
                          hobby=hobby)
        db.session.add(profile)
        db.session.commit()
        return redirect("/profiles/")
    else:
        return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)


import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for,)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home_page():
    """
    Home page route.
    """
    return render_template("home.html")


@app.before_request
def make_session_permanent():
    """
    Makes session
    """
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)


@app.route("/get_service_info")
def get_service_info():

    """
    Service info route.
    """

    service_history = list(mongo.db.service_history.find(
        filter={"created_by": session["user"]}))

    return render_template("service_info.html",
                           service_history=service_history)


@app.route("/login", methods=["GET", "POST"])
def login():

    """
    Login function.
    """

    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "get_service_info", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():

    """
    Log out funtion.
    """

    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():

    """
    Register funtion.
    """

    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_service_info", username=session["user"]))

    return render_template("register.html")


@app.route("/add_service", methods=["GET", "POST"])
def add_service():

    """
    Add Service History
    """

    if request.method == "POST":
        service = {
            "registration": request.form.get("vehicle_registration"),
            "service_no": request.form.get("service_number"),
            "mileage": request.form.get("mileage"),
            "work_completed": request.form.get("work_carried_out"),
            "date_of_service": request.form.get("date_of_service"),
            "garage": request.form.get("garage"),
            "created_by": session["user"]
        }

        mongo.db.service_history.insert_one(service)
        flash("Service Successfully Added")
        return redirect(url_for("get_service_info"))

    return render_template("add_service.html")


@app.route("/edit_service/<service_id>", methods=["GET", "POST"])
def edit_service(service_id):

    """
    Edit Service History
    """

    service = mongo.db.service_history.find_one({"_id": ObjectId(service_id)})
    return render_template("edit_service.html", service_info=service)


@app.route("/update_service/<service_id>", methods=["GET", "POST"])
def update_service(service_id):

    """
    Update Service History
    """

    service = mongo.db.service_history.find_one({"_id": ObjectId(service_id)})

    if request.method == "POST":

        service['registration'] = request.form.get("vehicle_registration")
        service['service_no'] = request.form.get("service_number")
        service['mileage'] = request.form.get("mileage")
        service['work_completed'] = request.form.get("work_carried_out")
        service['date_of_service'] = request.form.get("date_of_service")
        service['garage'] = request.form.get("garage")

        mongo.db.service_history.save(service)
        flash("Service Successfully updated")
        return redirect(url_for("get_service_info"))

    return render_template("edit_service.html", service_info=service)


@app.route("/delete_service/<service_id>")
def delete_service(service_id):

    """
    Delete Service History
    """

    mongo.db.service_history.remove({"_id": ObjectId(service_id)})
    flash("Service Deleted")
    return redirect(url_for("get_service_info"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

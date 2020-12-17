import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Home ---------------------------------------------------


@app.route("/")
def home_page():
    return render_template("home.html")

# End Home ---------------------------------------------------


# Service Info ---------------------------------------------------


@app.route("/get_service_info")
def get_service_info():
    service_history = list(mongo.db.service_history.find())
    return render_template("service_info.html",
            service_history=service_history)

# End Service Info ---------------------------------------------------


# Login ---------------------------------------------------


@app.route("/login", methods=["GET", "POST"])
def login():
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

# End Login ---------------------------------------------------


# Log Out ---------------------------------------------------


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# End Log Out ---------------------------------------------------


# Register ---------------------------------------------------


@app.route("/register", methods=["GET", "POST"])
def register():

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

# End Register ---------------------------------------------------

# Add Service ---------------------------------------------------


@app.route("/add_service", methods=["GET", "POST"])
def add_service():
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

# Add Service ---------------------------------------------------


# Edit Task ---------------------------------------------------

@app.route("/edit_service/<service_id>", methods=["GET", "POST"])
def edit_service(service_id):
    service = mongo.db.service_history.find_one({"_id": ObjectId(service_id)})
    return render_template("edit_service.html", service_info=service)

# End Edit Task ---------------------------------------------------

# Delete Task ---------------------------------------------------


@app.route("/delete_service/<service_id>")
def delete_service(service_id):
    mongo.db.service_history.remove({"_id": ObjectId(service_id)})
    flash("Service Deleted")
    return redirect(url_for("get_service_info"))

# End Delete Task ---------------------------------------------------




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


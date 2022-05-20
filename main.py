from flask import Flask, render_template, request
import flask_wtf
from flask_bootstrap import Bootstrap
from form import MyForm

app = Flask(__name__)

app.secret_key = 'adkfjalsdjf'

# for some reason you can't use Flask-Bootstrap without this
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    # WTF won't do it's own validation without this line
    login_form.validate_on_submit()
    # check if field is a "post" request.  only "post" requests are submitted.  "get" are not.  so if form validates, then field is "post"
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    else:
        return render_template('login1.html', myform=login_form)

@app.route("/success")
def rick():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
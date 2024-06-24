from flask import Flask, render, render_template

application = Flask(__name__)

@application.route('/')
def hello():
    return render_template('index.html')

if__name__=="__main__":
    application.run()

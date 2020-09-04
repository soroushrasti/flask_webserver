from flask import Flask, render_template

app=Flask( __name__ )

@app.route('/welcome')
def hello():
    return 'welcome to my website'


@app.route('/')
def first():
    return render_template('index.html' )



# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask  run

from flask import Flask

app=Flask( __name__ )

@app.route('/')
def hello():
    return 'welcome to my website'





# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask  run

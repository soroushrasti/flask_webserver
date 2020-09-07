from flask import Flask, render_template, request

app=Flask( __name__ )

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
       data=request.form.to_dict()
       return data




# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask  run

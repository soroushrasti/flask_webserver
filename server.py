from flask import Flask, render_template, request,redirect
import csv
app=Flask( __name__ )

@app.route('/')
def home_html():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('./Thankyou.html')
        except:
            return 'I problem in database'    

def write_to_csv(data):
     with open('database.csv', newline='',mode='a') as file_csv:
         email=data['email']
         subject=data['subject']
         message=data['message']
         csv_writer=csv.writer(file_csv)
         csv_writer.writerow([email,subject,message])

  






# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask  run

from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
@app.route('/<string:page>')
def render_page(page=None):
    rendered_page = 'index.html' if page is None else page
    return render_template(f'./{rendered_page}')

def write_to_file(data):
    with open('database.txt', 'a') as user_data:
        user_data.write(str(data) + '\n')

def write_to_csv(data):
    with open('database.csv', 'a') as user_data:
        csv_writer = csv.writer(user_data, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['email'], data['subject'], data['message']])

@app.route('/submit_form', methods= ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Error saving data in database'
    else:
        return 'Something went wrong. Try Again!!!'
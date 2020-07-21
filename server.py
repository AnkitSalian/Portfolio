from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
@app.route('/<string:page>')
def render_page(page=None):
    rendered_page = 'index.html' if page is None else page
    return render_template(f'./{rendered_page}')

def write_to_file(data):
    with open('database.txt', 'a') as user_data:
        user_data.write(str(data) + '\n')

@app.route('/submit_form', methods= ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try Again!!!'
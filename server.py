from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<string:page>')
@app.route('/')
def render_page(page=None):
    rendered_page = 'index.html' if page is None else page
    return render_template(f'./{rendered_page}')
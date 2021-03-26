from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate', methods=['GET'])
def estimate():
    return render_template('estimate.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        radius = int(request.form['radius'])
        height = int(request.form['height'])
        area_top = 3.14 * (radius * radius)
        print(area_top)
    return render_template('estimate.html', myValue = area_top)

if __name__ == '__main__':
    app.run(debug=True)
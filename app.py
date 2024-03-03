from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

keywords = {
    "data mining techniques": 16.4,
    "honey bees": 14.1,
    "processors": 11.3,
    "large data sets": 10.7,
    "evolutionary game theory": 10.1,
    "human immunodeficiency virus": 7.98,
    "computers": 7.54,
    "desktop": 7.2,
    "digital": 6.87,
    "complex data": 5.65
}

@app.route('/')
def dashboard():
    return render_template('./dashboard.html', keywords=keywords)

if __name__ == '__main__':
    app.run(debug=True)

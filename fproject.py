from flask import Flask, render_template
app = Flask(__name__)

from prometheus_metrics import setup_metrics
setup_metrics(app)

@app.route('/')
def run_flask():
    return render_template('index.html')

@app.route('/cloud')
def cloud():
    return render_template('cloud.html')

@app.route('/best')
def best():
    return render_template('best.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

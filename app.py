

from flask import Flask, render_template, redirect, url_for,request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/behind_scenes')
def behind_scenes():
    return redirect ('https://github.com/VrindaNarang/ml-disease-prediction/blob/main/Downloads/test/Thyroid_prediction_final_project.ipynb')

if __name__ == '__main__':
    app.run(debug=True)


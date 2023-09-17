from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK3/data/trinetx/medication_drug.csv')
@app.route('/')
def dataset(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
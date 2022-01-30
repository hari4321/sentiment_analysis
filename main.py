import pickle
from flask import *

model = pickle.load(open('model.pkl', 'rb'))
bag = pickle.load(open('bag.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
@app.route('/home', methods=['POST'])
def home():
    return render_template('analyse.html')


@app.route('/result', methods=['POST'])
def result():
    content = request.form['area']
    data = [content]
    vect = bag.transform(data).toarray()
    prediction = model.predict(vect)  #.reshape(1, -1)
    if prediction == 1:
        return render_template('result.html', predict="Hurray!!!! its a positive review")
    elif prediction == 0:
        return render_template('result.html', predict="Oops!!!! its a negative review")
    else:
        return render_template('result.html', predict="An unexpected occur")


app.run()

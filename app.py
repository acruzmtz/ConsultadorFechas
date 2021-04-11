from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form['name']
        day = request.form['day']
        date = request.form['date']

        print(name, day, date)

        return redirect(url_for('consultation', user=name.lower()))

    return render_template('index.html')


@app.route('/consulta/<user>')
def consultation(user):
    return render_template('consultation.html')


if __name__ == '__main__':
    app.run(debug=True)

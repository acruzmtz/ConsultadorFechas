from flask import Flask, render_template, request, redirect, url_for, session, flash
from rest_days import RestDays

app = Flask(__name__)

app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form['name']
        day = request.form['day']
        date = request.form['date']

        rest_day = RestDays(name, day, date)
        rest_day.get_actual_date()

        if not rest_day.get_other_date():
            flash('Por favor ingresa una fecha correcta')
            return redirect(url_for('home'))

        if rest_day.get_free_days():
            rest = 'Descansas'
        else:
            rest = 'NO descansas'

        session['data'] = (name.lower(), day, date, rest)

        return redirect(url_for('consultation', user=name.lower()))

    return render_template('index.html')


@app.route('/consulta/<user>')
def consultation(user):

    if 'data' in session:
        data = session.get('data')
    else:
        return redirect(url_for('home'))

    days = {'1': 'Termina hoy', '2': 'Termina mañana', '3': 'Término ayer', '4': 'Término antier'}
    option = days[data[1]]

    context = {
        'info': data,
        'option': option,
    }

    return render_template('consultation.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

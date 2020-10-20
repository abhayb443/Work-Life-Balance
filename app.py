import re

from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def index():
    return redirect(url_for('timer', num=90*60))


@app.route('/<int:num>s')
@app.route('/<int:num>')
def timer(num):
    return render_template('index.html', num=num)


@app.route('/custom', methods=['GET', 'POST'])
def custom():
    time = request.form.get('time', 180)
    print(time)
    # use re to validate input data
    m = re.match('\d+[smh]?$', time)
    if m is None:
        flash(u'Please enter a valid Time like 30 Minutes or 60 Minutes')
        return redirect(url_for('index'))
    if time[-1] not in 'smh':
        return redirect(url_for('timer', num=int(time)))
    else:
        type = {'s': 'timer', 'm': 'minutes', 'h': 'hours'}
        return redirect(url_for(type[time[-1]], num=int(time[:-1])))


@app.route('/<int:num>m')
def minutes(num):
    return redirect(url_for('timer', num=num*60))


@app.route('/<int:num>h')
def hours(num):
    return redirect(url_for('timer', num=num*3600))


@app.errorhandler(404)
def page_not_found(e):
    flash(u'Wrong Address, try again...')
    return redirect(url_for('timer', num=244))


if __name__ == '__main__':
    app.run()

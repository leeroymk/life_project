from config.config import Config
from flask import Flask
from flask import render_template, redirect, url_for
from forms.forms import ButtonsForm
from project.project import GameOfLife


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ButtonsForm()
    if form.width_form.data and form.height_form.data:
        GameOfLife(int(form.width_form.data), int(form.height_form.data))
        return redirect(url_for('live'))
    return render_template('index.html', form=form)


@app.route('/live/')
def live():
    current_game = GameOfLife()
    if current_game.counter > 0:
        current_game.form_new_generation()
    current_game.counter += 1
    return render_template('live.html', current_game=current_game)

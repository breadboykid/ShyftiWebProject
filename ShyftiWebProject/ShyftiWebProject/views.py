"""
Routes and views for the flask application.
"""

import io
import random
from flask import Response
from datetime import datetime
from flask import render_template
from ShyftiWebProject import app
import ShyftiWebProject.coronavirus
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

posts = [
    {
        'author': 'Leslie Pan',
        'title': 'Shyfti Website',
        'date_posted': 'April 20, 2020'
    },    
    {
        'author': 'Leslie Pan 2',
        'title': 'Shyfti Website2',
        'date_posted': 'April 22, 2020'
    }    
]

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Here are my contact details below'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Just random code upload here.',
        posts=posts
    )

@app.route('/primenumbergenerator')
def primenumbergenerator():
    """Renders the about page."""
    return render_template(
        'primenumbergenerator.html',
        title='Prime number generator',
        year=datetime.now().year,
        message='Nothing here'
    )

@app.route('/coronavirus')
def coronavirus():
    """Renders the about page."""
    return render_template(
        'coronavirus.html',
        title='Coronavirus (Covid-19) Information page',
        year=datetime.now().year,
        message='Useful information surround COVID-19',
        latestFigure=ShyftiWebProject.coronavirus.getCoronaDataArray()[-1]
    )

@app.route('/thankyouforyourservice')
def thankyouforyourservice():
    """Renders the about page."""
    return render_template(
        'maxshrine.html',
        title='Max Mcgregor Appreciation Society',
        year=datetime.now().year,
        message='Clap for Max every 8pm on a Monday...Thank you for your service '
    )

@app.route('/islington')
def islington():
    """Renders the about page."""
    return render_template(
        'jorbae.html',
        title='Jorbae appreciation society',
        year=datetime.now().year,
        message='Thank you for your service.'
    )

@app.route('/ceptin')
def ceptin():
    """Renders the about page."""
    return render_template(
        'ceptin.html',
        title='Thank you for your service',
        year=datetime.now().year,
        message='Let'' clap for Ceptin every Monday at 8pm to thank him for his service'
    )


@app.route('/coronacasesplotlinear.png')
def plotCoronaCasesLinear():
    fig = create_figurelinear()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/coronacasesplotlog.png')
def plotCoronaCasesLog():
    fig = create_figurelog()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figurelinear():
    data = ShyftiWebProject.coronavirus.getCoronaDataArray()
    xs = [i[0] for i in data]
    ys = [i[1] for i in data]

    fig = plt.figure()
    ax= fig.add_subplot(1, 1, 1)
    fig.autofmt_xdate() 

    M = 10
    xticks = ticker.MaxNLocator(M)

    ax.xaxis.set_major_locator(xticks)
    ax.set_title('Linear')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cases')

    plt.plot(xs, ys)
    return fig

def create_figurelog():
    data = ShyftiWebProject.coronavirus.getCoronaDataArray()
    xs = [i[0] for i in data]
    ys = [i[1] for i in data]

    fig = plt.figure()
    ax= fig.add_subplot(1, 1, 1)
    fig.autofmt_xdate()
    fig.suptitle('')

    M = 10
    xticks = ticker.MaxNLocator(M)
    
    ax.xaxis.set_major_locator(xticks)
    ax.set_title('Logarithmic')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cases')
    ax.set_yscale('log')

    plt.plot(xs, ys, color='orange')
    return fig
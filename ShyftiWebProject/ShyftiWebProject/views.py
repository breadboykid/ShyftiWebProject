"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ShyftiWebProject import app
from ShyftiWebProject.coronavirus import CoronaVirusUK
from ShyftiWebProject.graph import PlotType

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
        latestFigure=CoronaVirusUK.getCoronaDataArray()[-1]
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

@app.route('/coronacasesplotlog.png')
def plotCoronaCasesLog():
    corona_virus_data = CoronaVirusUK.getCoronaDataArray()
    corona_class = CoronaVirusUK(corona_virus_data)
    return corona_class.getPlotImage(PlotType.Logarithmic)

@app.route('/coronacasesplotlinear.png')
def plotCoronaCasesLinear():
    corona_virus_data = CoronaVirusUK.getCoronaDataArray()
    corona_class = CoronaVirusUK(corona_virus_data)
    return corona_class.getPlotImage(PlotType.Linear)
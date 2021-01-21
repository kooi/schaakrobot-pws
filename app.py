from flask import Flask, render_template
import serial

app = Flask(__name__)


@app.route('/')
def hello():
    # return '<h1>Hello, World!</h1>'
    return render_template('schaakbord.html')


@app.route('/zet/<x1>/<y1>/<x2>/<y2>')
# def zet(x1, y1, x2, y2):
def zet(x1, y1, x2, y2):
    # seriele_poort = serial.Serial('/dev/ttyUSB0', 9600)
    # seriele_poort.write(x1)
    # seriele_poort.write(y1)
    # seriele_poort.write(x2)
    # seriele_poort.write(y2)
    return "x1="+x1+"y1="+y1+"x2="+x2+"y2="+y2 + "\n Is hopelijk gelukt..."
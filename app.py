from flask import Flask, render_template, request, redirect, url_for
import serial

app = Flask(__name__)


@app.route('/')
def schaakbord():
    # return '<h1>Hello, World!</h1>'
    return render_template('schaakbord.html')


@app.route('/zet') # We gebruiken nu requests dus geen lange endpoint
# def zet(x1, y1, x2, y2):
def zet():
    # Lees de waarden uit het formulier in
    # Als de waarden niet gegeven zijn of 
    # geen getallen zijn maken we er 0 van.
    x1 = request.args.get('x1', default=0, type=int)
    y1 = request.args.get('y1', default=0, type=int)
    x2 = request.args.get('x2', default=0, type=int)
    y2 = request.args.get('y2', default=0, type=int)
    # TODO: Lees vorige zetten ook in

    # Als de waardes incorrect zijn willen we natuurlijk niet dat
    # de robot dit probeert. We controleren dat alle getallen 
    # in de toegestane lijst staan
    valid_range = [1, 2, 3, 4, 5, 6, 7, 8]
    if x1 in valid_range and y1 in valid_range:
        if x2 in valid_range and y2 in valid_range:

            # Maak een verbinding met de schaakrobot (controleer adres)
            # seriele_poort = serial.Serial('/dev/ttyUSB0', 9600)

            # Doe de zet met de schaakrobot (misschien moeten er delays tussen)
            # seriele_poort.write(x1)
            # seriele_poort.write(y1)
            # seriele_poort.write(x2)
            # seriele_poort.write(y2)

            # Als het gelukt is, ga dan terug naar het endpoint voor schaakbord
            # TODO: Geef vorige zetten mee
            return redirect( url_for('schaakbord') ) 

    # Tenminste één van de waardes was niet goed. Reyurn gewoon alle waardes.
    return { 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2 }

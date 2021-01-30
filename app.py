from flask import Flask, render_template, request, redirect, url_for
import serial
import shelve

app = Flask(__name__)
zetten_database = 'zetten.db'


@app.route('/reset')
def init_database():
    db = shelve.open(zetten_database)
    # In principe maken we een lege database
    # db['zetten'] = []
    # Voor testen maken we gebruik van een aantal dummy-zetten
    db['zetten'] = [
        {   "x1": 5, "y1": 2, "x2": 5, "y2": 4 }, # e2e4
        {   "x1": 5, "y1": 7, "x2": 5, "y2": 5 }, # e7e5
    ]
    db.close()


@app.route('/')
def schaakbord():
    # Vertaling voor de naam van de x-coordinaat
    # x: A=1 ... H=8
    # y: 1=1 ... 8=8
    vertaling_x = [0, "a", "b", "c", "d", "e", "f", "g", "h"]

    # Lees vorige zetten in uit de database
    db = shelve.open(zetten_database)
    vorige_zetten = db['zetten']
    db.close()
    return render_template('schaakbord.html', zetten=vorige_zetten, key_x=vertaling_x)


# Endpoint voor het uitvoeren van een zet
# deze verwacht 4 parameters, x1, y1, x2 & y2
@app.route('/zet')
def zet():
    # Lees de waarden uit het formulier in
    # Als de waarden niet gegeven zijn of 
    # geen getallen zijn maken we er 0 van.
    x1 = request.args.get('x1', default=0, type=int)
    y1 = request.args.get('y1', default=0, type=int)
    x2 = request.args.get('x2', default=0, type=int)
    y2 = request.args.get('y2', default=0, type=int)

    # Als de waardes incorrect zijn willen we natuurlijk niet dat
    # de robot dit probeert. We controleren dat alle getallen 
    # in de toegestane lijst staan
    # TODO: Controleer beter op valide zetten
    valid_range = [1, 2, 3, 4, 5, 6, 7, 8]
    if x1 in valid_range and y1 in valid_range:
        if x2 in valid_range and y2 in valid_range:

            # Open de shelf (block)
            db = shelve.open(zetten_database)
            zetten = db['zetten']
            zetten.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

            # Maak een verbinding met de schaakrobot (controleer adres)
            # seriele_poort = serial.Serial('/dev/ttyUSB0', 9600)

            # Doe de zet met de schaakrobot (misschien moeten er delays tussen)
            # seriele_poort.write(x1)
            # seriele_poort.write(y1)
            # seriele_poort.write(x2)
            # seriele_poort.write(y2)

            # Sla vorige zetten op en sluit de shelf (unblock)
            db['zetten'] = zetten
            db.close()

            # Ga terug naar het endpoint voor schaakbord
            return redirect( url_for('schaakbord') ) 

    # Tenminste één van de waardes was niet goed. Return gewoon alle waardes.
    return { 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2 }

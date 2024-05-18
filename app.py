from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create")
def create():
    return render_template('/create/index.html')

@app.route("/create/race")
def create_race():
    return render_template('/create/race.html')

@app.route("/create/class")
def create_class():
    return render_template('/create/class.html')

@app.route("/create/abilities")
def create_abilities():
    return render_template('/create/abilities.html')

@app.route("/create/description")
def create_description():
    return render_template('/create/description.html')

@app.route("/create/equipment")
def create_equipment():
    return render_template('/create/equipment.html')

@app.route("/character")
def character():
    return render_template('charactersheet.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=5000, host="0.0.0.0")
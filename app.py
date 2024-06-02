from flask import Flask, render_template, send_file
import requests
import json
import markdown

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create")
def create():
    return render_template('/create/index.html')

@app.route("/create/race")
def create_race():
    with open("races.json", "r", encoding="utf8") as f:
        races = json.load(f)['results']
    return render_template('/create/race.html', races=races)

@app.route("/create/class")
def create_class():
    with open("classes.json", "r", encoding="utf8") as f:
        classes = json.load(f)['results']
    return render_template('/create/class.html', classes=classes)

@app.route("/create/abilities")
def create_abilities():
    return render_template('/create/abilities.html')

@app.route("/create/description")
def create_description():
    with open("backgrounds.json", "r", encoding="utf8") as f:
        backgrounds = json.load(f)['results']
    return render_template('/create/description.html', backgrounds=backgrounds)

@app.route("/create/equipment")
def create_equipment():
    return render_template('/create/equipment.html')

@app.route("/character")
def character():
    f = open('./characters/character.json')
    character_info = json.load(f)
    return render_template('charactersheet.html', character_info=character_info)

@app.route("/backgrounds.json")
def backgrounds():
    return send_file('backgrounds.json')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=5000, host="0.0.0.0")
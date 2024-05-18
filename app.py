from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create")
def create():
    return render_template('/create/index.html')

@app.route("/create/race")
def create_race():
    races = requests.get('https://api.open5e.com/v1/races/?slug__in=&slug__iexact=&slug=&name__iexact=&name=&desc__iexact=&desc=&desc__in=&desc__icontains=&document__slug__iexact=wotc-srd&document__slug=&document__slug__in=&asi_desc__iexact=&asi_desc=&asi_desc__icontains=&age__iexact=&age=&age__icontains=&alignment__iexact=&alignment=&alignment__icontains=&size__iexact=&size=&size__icontains=&speed_desc__iexact=&speed_desc=&speed_desc__icontains=&languages__iexact=&languages=&languages__icontains=&vision__iexact=&vision=&vision__icontains=&traits__iexact=&traits=&traits__icontains=&document__slug__not_in=').json()['results']
    return render_template('/create/race.html', races=races)

@app.route("/create/class")
def create_class():
    classes = requests.get('https://api.open5e.com/v1/classes/?slug__in=&slug__iexact=&slug=&name__iexact=&name=&desc__iexact=&desc=&desc__in=&desc__icontains=&hit_dice__iexact=&hit_dice=&hit_dice__in=&hp_at_1st_level__iexact=&hp_at_1st_level=&hp_at_1st_level__icontains=&hp_at_higher_levels__iexact=&hp_at_higher_levels=&hp_at_higher_levels__icontains=&prof_armor__iexact=&prof_armor=&prof_armor__icontains=&prof_weapons__iexact=&prof_weapons=&prof_weapons__icontains=&prof_tools__iexact=&prof_tools=&prof_tools__icontains=&prof_skills__iexact=&prof_skills=&prof_skills__icontains=&equipment__iexact=&equipment=&equipment__icontains=&spellcasting_ability__iexact=&spellcasting_ability=&spellcasting_ability__icontains=&subtypes_name__iexact=&subtypes_name=&subtypes_name__icontains=&document__slug__iexact=wotc-srd&document__slug=&document__slug__in=&document__slug__not_in=').json()['results']
    return render_template('/create/class.html', classes=classes)

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
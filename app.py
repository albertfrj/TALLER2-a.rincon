from flask import Flask, jsonify, render_template
import os

app = Flask(__name__, template_folder="views")

animal_sounds = {
    "gato": "Miau, miau",
    "perro": "!Guau, guau",
    "huron": "¡Eek Eek!",
    "boa": "¡Tsss!"
}

@app.route('/animal-sound/<animal>', methods=['GET'])
def get_animal_sound(animal):
    animal = animal.lower()
    if animal in animal_sounds:
        return jsonify({
            "animal": animal,
            "sound": animal_sounds[animal]
        })
    else:
        return jsonify({
            "error": "Animal no encontrado"
        }), 404

@app.route('/')
def home():
    return render_template('index.html', animals=animal_sounds)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Charger le profil de Max
with open('/root/brian/memoire/profil.yaml', 'r') as file:
    profil = yaml.safe_load(file)

@app.route('/')
def home():
    return f"Bienvenue Max! Tu peux parler à Brian ici."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '').lower()
    if 'valeurs' in question:
        valeurs = ", ".join(profil.get("valeurs", []))
        return jsonify({"brian": f"Tes valeurs sont : {valeurs}"})
    elif 'bjorn' in question:
        return jsonify({"brian": f"Voici ce que je sais de Bjorn : {profil['relations_importantes']['bjorn']}"})
    elif 'jerome' in question:
        return jsonify({"brian": f"Voici ce que je sais de Jérôme : {profil['relations_importantes']['jerome']}"})
    elif 'claudia' in question:
        return jsonify({"brian": f"Voici ce que je sais de Claudia : {profil['relations_importantes']['claudia']}"})
    else:
        return jsonify({"brian": "Je ne comprends pas encore cette demande."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Chargement du fichier YAML
import yaml

with open("/root/brian/memoire/profil.yaml", "r") as file:
    profil = yaml.safe_load(file)

print("Salut Max, je suis Brian. Tu peux me parler. (Tape 'exit' pour quitter)")# Chargement du fichier YAML
import yaml
print("Brian: Je t’écoute, mais je ne comprends pas encore cette demande.")with open('/root/brian/memoire/profil.yaml', 'r') as file:
    profil = yaml.safe_load(file)

print("Salut Max, je suis Brian. Tu peux me parler. (Tape 'exit' pour quitter)")

while True:
    question = input("Toi: ").lower()

    if question in ['exit', 'quitter']:
        print("Brian: À bientôt Max.")
        break

    elif "valeurs" in question:
        valeurs = ', '.join(profil.get("valeurs", []))
        print(f"Brian: Tes valeurs sont : {valeurs}")

    elif "bjorn" in question:
        print(f"Brian: Voici ce que je sais de Bjorn : {profil['relations_importantes']['bjorn']}")

    elif "jerome" in question:
        print(f"Brian: Voici ce que je sais de Jérôme : {profil['relations_importantes']['jerome']}")

    elif "claudia" in question:
        print(f"Brian: Voici ce que je sais de Claudia : {profil['relations_importantes']['claudia']}")

    elif "projets" in question or "ia" in question:
        print("Brian: Voici tes projets IA :")
        for projet in profil["projets_IA"]:
            nom = projet["nom"]
            desc = projet["description"]
            print(f"  - {nom}: {desc}")

    else:
        print("Brian: Je t’écoute, mais je ne comprends pas encore cette demande.")import yaml
chmod +x /root/brian/converse.py
with open('/root/brian/memoire/profil.yaml', 'r') as file:
    profil = yaml.safe_load(file)

print("Salut Max, je suis Brian. Tu peux me parler. (Tape 'exit' pour quitter)\n")

while True:
# Chargement du fichier YAML
import yaml

with open("/root/brian/memoire/profil.yaml", "r") as file:
    profil = yaml.safe_load(file)

print("Salut Max, je suis Brian. Tu peux me parler. (Tape 'exit' pour quitter)")

while True:
    question = input("Toi: ").lower()

    if question in ['exit', 'quitter']:
        print("Brian: À bientôt Max.")
        break

    elif "valeurs" in question:
        valeurs = ", ".join(profil.get("valeurs", []))
        print(f"Brian: Tes valeurs sont : {valeurs}")

    elif "bjorn" in question:
        bjorn = profil.get("relations_importantes", {}).get("bjorn", "Je ne sais rien sur Bjorn.")
        print(f"Brian: Voici ce que je sais de Bjorn : {bjorn}")

    elif "jerome" in question:
        jerome = profil.get("relations_importantes", {}).get("jerome", "Je ne sais rien sur Jérôme.")
        print(f"Brian: Voici ce que je sais de Jérôme : {jerome}")

    elif "claudia" in question:
        claudia = profil.get("relations_importantes", {}).get("claudia", "Je ne sais rien sur Claudia.")
        print(f"Brian: Voici ce que je sais de Claudia : {claudia}")

    elif "projets" in question:
        projets = profil.get("projets_IA", [])
        print("Brian: Voici tes projets IA :")
        for p in projets:
            print(f"  - {p['nom']}: {p['description']}")

    else:
        print("Brian: Je t’écoute, mais je ne comprends pas encore cette demande.")    question = input("Toi: ")
    if question.lower() in ["exit", "quit"]:
        print("Brian: À bientôt Max!")
        break
    elif "valeurs" in question.lower():
        print("Brian: Tes valeurs sont : " + ", ".join(profil["valeurs"]))
    elif "bjorn" in question.lower():
        print("Brian: Voici ce que je sais de Bjorn : " + profil["relations_importantes"]["bjorn"])
    elif "jerome" in question.lower():
        print("Brian: Voici ce que je sais de Jérôme : " + profil["relations_importantes"]["jerome"])
    elif "claudia" in question.lower():
        print("Brian: Voici ce que je sais de Claudia : " + profil["relations_importantes"]["claudia"])
    else:
        print("Brian: Je t’écoute, mais je ne comprends pas encore cette demande.")

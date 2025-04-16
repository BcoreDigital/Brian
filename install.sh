#!/bin/bash

echo "🧠 Installation de Brian..."

# Mise à jour système
apt update && apt upgrade -y

# Installation des dépendances
apt install -y python3 python3-pip git

# Installation des librairies Python
pip3 install flask openai pyyaml

echo "✅ Installation terminée."
echo "➡️ Pour lancer Brian : python3 webapp.py"

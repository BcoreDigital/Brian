import yaml

# Charger le fichier YAML
def charger_profil():
    try:
        with open('/root/brian/memoire/profil.yaml', 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print("Le fichier profil.yaml n'a pas été trouvé !")
        return None

# Afficher les informations importantes de Max
def afficher_infos(data):
    if data:
        print("\n-- Profil de Max --\n")
        print(f"Alias: {data.get('alias', 'Non défini')}")
        print(f"Valeurs: {', '.join(data.get('valeurs', []))}")
        print("\nRelations importantes:")
        for relation, description in data.get('relations_importantes', {}).items():
            print(f"  - {relation}: {description}")
        print("\nProjets IA:")
        for projet in data.get('projets_IA', []):
            print(f"  - {projet['nom']}: {projet['description']}")
        print(f"\nDernier export: {data.get('dernier_export', 'Non défini')}")
    else:
        print("Aucune donnée à afficher.")

if __name__ == "__main__":
    profil_data = charger_profil()
    afficher_infos(profil_data)

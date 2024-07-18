import os

def generate_invitations(template, attendees):
    # Validation des entrées
    if not isinstance(template, str):
        print("Erreur : Le modèle doit être une chaîne de caractères.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Erreur : Les invités doivent être une liste de dictionnaires.")
        return
    
    # Gérer les entrées vides
    if template.strip() == "":
        print("Le modèle est vide, aucun fichier de sortie généré.")
        return
    
    if not attendees:
        print("Aucune donnée fournie, aucun fichier de sortie généré.")
        return
    
    # Traiter chaque invité et générer des fichiers
    for idx, attendee in enumerate(attendees):
        output_content = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            output_content = output_content.replace(f"{{{{{placeholder}}}}}", value)
        
        output_filename = f"output_{idx + 1}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)
        print(f"Fichier généré : {output_filename}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Lire le modèle à partir d'un fichier
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Liste des invités
    attendees = [
        {"name": "Alice", "event_title": "Conférence Python", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Atelier de Science des Données", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "Sommet de l'IA", "event_date": None, "event_location": "Boston"}
    ]

    # Appeler la fonction avec le modèle et la liste des invités
    generate_invitations(template_content, attendees)


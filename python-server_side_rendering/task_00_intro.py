import os

def generate_invitations(template, attendees):
    # Validation des entrées
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    # Gestion des entrées vides
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Traitement de chaque participant et génération des fichiers
    for idx, attendee in enumerate(attendees):
        output_content = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            # Récupération de la valeur du participant, ou "N/A" si absent
            value = attendee.get(placeholder, "N/A")
            output_content = output_content.replace(f"{{{{{placeholder}}}}}", value)
        
        # Nom du fichier de sortie
        output_filename = f"output_{idx + 1}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)
        print(f"Generated file: {output_filename}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Lecture du template à partir d'un fichier
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Liste des participants
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Appel de la fonction avec le template et la liste des participants
    generate_invitations(template_content, attendees)


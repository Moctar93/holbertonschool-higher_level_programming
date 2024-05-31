import requests
import csv

def fetch_and_print_posts():
    """
    Récupère les publications depuis JSONPlaceholder et imprime leurs titres.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Imprime le code de statut
    print(f"Code de statut : {response.status_code}")

    if response.status_code == 200:
        # Analyse la réponse en JSON
        posts = response.json()
        
        # Imprime les titres des publications
        for post in posts:
            print(post['title'])
    else:
        print("La requête a échoué")

def fetch_and_save_posts():
    """
    Récupère les publications depuis JSONPlaceholder et les sauvegarde dans un fichier CSV.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        # Analyse la réponse en JSON
        posts = response.json()

        # Prépare les données pour le CSV
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Écrit les données dans un fichier CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in posts_data:
                writer.writerow(post)
    else:
        print("La requête a échoué")

# Appelle les fonctions
fetch_and_print_posts()
fetch_and_save_posts()


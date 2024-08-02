# task_02_requests.py
import requests
import csv

def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        
        # Print titles of all posts
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder and saves them to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        
        # Prepare data for CSV
        data_to_write = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Write data to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data_to_write)


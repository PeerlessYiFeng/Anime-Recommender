import requests
import urllib.parse

def fetch_anime_poster(title):
    try:
        query = urllib.parse.quote(title)
        url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data['data'][0]['images']['jpg']['image_url']
    except Exception as e:
        print(f"Failed to fetch poster for {title}: {e}")
        return None

import os
import requests

API_KEY = os.getenv("MY_API_KEY")

if not API_KEY:
    print("API key not found. Set the MY_API_KEY environment variable.")
else:
    url = "https://api.example.com/data"

    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        print(data)

    except requests.exceptions.ConnectionError:
        print("Connection failed. Check your internet connection.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

import requests, os
from dotenv import load_dotenv

load_dotenv()

IG_USER_ID = os.getenv("IG_USER_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def create_media_container(image_url, caption=""):
    url = f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media"
    params = {
        "image_url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }
    r = requests.post(url, params=params)
    print("Create response:", r.json())
    r.raise_for_status()
    return r.json().get("id")

def publish_media(creation_id):
    url = f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media_publish"
    params = {"creation_id": creation_id, "access_token": ACCESS_TOKEN}
    r = requests.post(url, params=params)
    print("Publish response:", r.json())
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    IMAGE_URL = "https://raw.githubusercontent.com/<your-username>/ig-media-test/main/mypost.jpg"
    CAPTION = "Auto-posted from Python with GitHub hosting 🚀"

    creation_id = create_media_container(IMAGE_URL, CAPTION)
    publish_resp = publish_media(creation_id)
    print("Done:", publish_resp)

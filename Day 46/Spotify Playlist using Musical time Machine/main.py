from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
all_songs = soup.find_all("h3", class_="a-no-trucate")
song_list=[]
for song in all_songs:
    song_list.append("".join((song.getText().split())))
# print(song_list)

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id="Your Client ID",
        client_secret="Your Secret Key",
        show_dialog=True,
        cache_path="token.txt"
    )
)


user_id = sp.current_user()["id"]
# print(user_id,"is id")

song_uris = []
year = date.split("-")[0]

#Searching Spotify for songs by title
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pprint(f"{song} doesn't exist in Spotify. Skipped.")

#Creating new playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
import requests
import urllib.parse


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def search_song(self, artist, track):
        # search for artist and track in a single string to yield result
        query = urllib.parse.quote(f'{artist}{track}')
        # specify that we are searching for a track
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"

        # issue the request
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer{self.api_token}"
            }
        )

        response_json = response.json()

        results = response_json['tracks']['items']

        if results:
            # assumes the first track is the one we want and return song id
            return results[0]['id']
        else:
            raise Exception(f"No song found for {artist}={track}")

    def add_song_to_spotify_liked(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"

        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer{self.api_token}"
            }
        )

        return response.ok

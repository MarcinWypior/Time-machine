import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_CLIENT_ID = "cefb1e7b563f44f29ba323f72bd4d4cf"
SPOTIFY_SECRET = "21fe5c8e99d440be8b562166683c7787"
REDIRECT_URI = "http://example.com"  # For example, "http://localhost:8888/callback"
USERNAME = "31g7zz723skvrmdn4zxwrew6dnee"

OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

import spotipy
from spotipy.oauth2 import SpotifyOAuth




# Scopes determine what actions the application can perform on behalf of the user
SCOPE = "playlist-modify-private"  # Allow the app to create private playlists

# Create a Spotify OAuth object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE,
                                               username=USERNAME))


def create_spotify_playlist(playlist_name, track_uris):
    # Create a private playlist
    playlist = sp.user_playlist_create(user=USERNAME, name=playlist_name, public=False)

    # Add tracks to the playlist
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)
    print(f"Playlist '{playlist_name}' created with {len(track_uris)} tracks!")


if __name__ == "__main__":
    # Example usage:
    playlist_name = "playlista z API"
    track_uris = [
        "spotify:track:6mFkJmJqdDVQ1REhVfGgd1",  # Ed Sheeran - Shape of You
        "spotify:track:3Z8FwOEN59mRMxDCtb8N0A",  # Dua Lipa - Levitating
        "spotify:track:3HVWdVOQ0ZA45FuZGSfvns",  # The Weeknd - Blinding Lights

        # Add more track URIs here...
    ]

    create_spotify_playlist(playlist_name, track_uris)
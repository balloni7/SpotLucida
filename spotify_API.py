import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys


def enumerate_playlist(sp_obj, playlist_id, offset=0):
    """Enumerate all tracks by date added, increasing"""
    track_list = sp.playlist_items(playlist_id, fields="items.track.name, items.track.artists.name, items.track.uri",
                                   offset=offset)

    i = 1 + offset
    for track in track_list["items"]:
        print(i, ". ", (track["track"]["name"]), sep="")
        i += 1

    return track_list


# give enumerate_playlist an alias
ep = enumerate_playlist


def clone_remaining_playlist(sp_obj, playlist_id, offset=0, new_name="New_playlist"):
    """Clone remaining palylist"""
    new_track_list = sp_obj.playlist_items(playlist_id, fields="items.track.uri", offset=offset)

    # Create a new playlist
    new_playlist = sp_obj.user_playlist_create(user=sp_obj.me()['id'], name=new_name, public=True)
    # Get track URI
    track_uris = [track["track"]['uri'] for track in new_track_list["items"]]
    # Add those tracks
    sp_obj.playlist_add_items(playlist_id=new_playlist['id'], items=track_uris)

    print(f"https://open.spotify.com/playlist/{new_playlist["id"]}")


# give clone_remaining_playlist an alias
crp = clone_remaining_playlist


def get_song_position(sp_obj, playlist_id, song_name):

if __name__ == '__main__':
    # Your Spotify credentials
    client_id = '0482fd381736449ebb1d9b62f15ec9ca'
    client_secret = 'c1ba26df523c406dbe34ac7a83aa75eb'
    redirect_uri = 'http://localhost:8080'
    playlist_id = 'https://open.spotify.com/playlist/0XnVU5HcKsg5NqCTvaGuua?si=0fab3f5ea2554c32'

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
                                  scope='playlist-modify-public playlist-modify-private'))

    # enumerate_playlist(sp, playlist_id, 0)
    # clone_remaining_playlist(sp, playlist_id, 40)

    # chamar as funçoes pela cmd:
    args = sys.argv
    globals()[args[1]](sp, playlist_id, *args[2:])

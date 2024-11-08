import os
import sys
import time
import threading
import webbrowser
import spotipy
import lyricsgenius as lg
import queue

# environment variables
os.environ['SPOTIPY_CLIENT_ID'] = "713de4cd018d4d438821c28dcdf3a5b0"
os.environ['SPOTIPY_CLIENT_SECRET'] = "addff9e44b3446049801058222fe5faf"
os.environ['SPOTIPY_REDIRECT_URI'] = "https://google.com"
os.environ['GENIUS_ACCESS_TOKEN'] = "mm9FMt5M7FHHvamliRq8X5mg9QlV8Pho8mtIlsyVnvXK1iqkJBOvZBrrJKVWj5bL"

# Function to get input with timeout
def timed_input(prompt, timeout, timeoutmsg):
    q = queue.Queue()
    def input_thread():
        sys.stdout.write(prompt)
        sys.stdout.flush()
        try:
            q.put(input())
        except EOFError:
            pass
    thread = threading.Thread(target=input_thread)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    return q.get() if not q.empty() else None

# Set up Spotify API
spotifyOAuth = spotipy.SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                    client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                    redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
                                    scope="user-read-currently-playing")
token = spotifyOAuth.get_access_token()
spotifyObject = spotipy.Spotify(auth=token['access_token'])

# Set up Genius API
genius = lg.Genius(os.environ['GENIUS_ACCESS_TOKEN'], timeout=10)

# Sleep helper
def sleeping(duration):
    time.sleep(duration)

while True:
    print("\n>> Updating current track...")
    current = spotifyObject.currently_playing()
    if not current:
        print(">> No song is currently playing.")
        time.sleep(5)
        continue

    track = current['item']
    artist = track['artists'][0]['name']
    title = track['name']
    duration = int((track['duration_ms'] - current['progress_ms']) / 1000)

    print(f"Now playing: {artist} - {title}")
    search_query = f"{artist} {title}"

    try:
        song = genius.search_song(title=title, artist=artist)
        if song:
            print("\nLyrics:\n", song.lyrics)
            url = song.url
        else:
            print(">> Lyrics not found.")
    except Exception as e:
        print(f">> Error fetching lyrics: {e}")

    # Wait for user input or song to finish
    thread = threading.Thread(target=sleeping, args=(duration,))
    thread.start()
    print(f"\n>> Enter 0 to open browser, 1 for artist info, or hit enter to continue:")
    
    user_input = timed_input(">> ", duration, "Moving on to next track...")
    if user_input == "0":
        print(f">> Opening browser for: {url}")
        webbrowser.open(url, new=0, autoraise=False)
    elif user_input == "1":
        artist_info = spotifyObject.artist(track['artists'][0]['id'])
        print(f"Artist: {artist_info['name']}")
        print(f"Genres: {', '.join(artist_info['genres'])}")
        print(f"Popularity: {artist_info['popularity']}")
        print(f"Spotify URL: {artist_info['external_urls']['spotify']}")
    
    # Sleep until next track or user input
    thread.join()

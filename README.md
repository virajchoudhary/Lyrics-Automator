# Lyrics-Automator
**Fetch Lyrics & Artist Info for the Currently Playing Song**

This Python script automatically fetches lyrics and provides artist information for the currently playing song on Spotify. It integrates with both the Spotify API and Genius API, allowing you to:
- Get real-time lyrics for the song currently playing on Spotify.
- Fetch artist information from Spotify.
- Open a browser with the Genius lyrics page for the song.


## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Error Handling](#error-handling)
- [License](#license)
- [Contributing](#contributing)
- [Example Output](#example-output)


## Installation

### Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/lyrics-automator.git
cd lyrics-automator
```
Set Up Virtual Environment (Optional, but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

## Install Dependencies

Install the required dependencies via pip:
```
pip install -r requirements.txt
```

### Get API Credentials

You need API keys for both Spotify and Genius:
    - Spotify: You can get your credentials by creating an app on the Spotify Developer Dashboard.
    - Genius: Get your access token by registering on Genius API.

After obtaining these keys, set them in your environment variables:
```
export SPOTIPY_CLIENT_ID="your_spotify_client_id"
export SPOTIPY_CLIENT_SECRET="your_spotify_client_secret"
export SPOTIPY_REDIRECT_URI="your_spotify_redirect_uri"
export GENIUS_ACCESS_TOKEN="your_genius_access_token"
```
Alternatively, you can set them directly in the script (automate_lyrics.py).


## Configuration

Before running the script, ensure you have your Spotify and Genius API credentials set up (as shown in the "Installation" section). Additionally, make sure you have a working Python environment with the required libraries installed.


## Usage

Run the script directly from your terminal:
```
python automate_lyrics.py
```
### How It Works

   - The script checks the currently playing song on Spotify.
   - If the song is playing, it fetches the lyrics from Genius and prints them to the console.
   - It also gives the option to open the Genius lyrics page in the browser or fetch artist info.
   - The script keeps running in a loop, waiting for the next song to play.

### Available Options

While the lyrics are being displayed, the user is prompted to:

   - Enter 0: Open the lyrics page in the browser.
   - Enter 1: Get information about the artist.
   - Enter nothing: Continue to the next song after a set timeout.

You can exit the script at any time by pressing Ctrl+C.


## Features

   - Fetches real-time lyrics for the currently playing song on Spotify.
   - Option to open the Genius lyrics page in the browser.
   - Fetches artist information such as name, genre, popularity, and Spotify URL.
   - Handles timeouts when the Genius API request takes too long.
   - Continuous loop for fetching lyrics of the currently playing song.


## Dependencies

The script uses the following Python libraries:

   - spotipy: For interacting with the Spotify API to get the currently playing song.
   - lyricsgenius: For fetching lyrics from the Genius API.
   - requests: For handling HTTP requests to external APIs.
   - webbrowser: For opening the lyrics page in the browser.
   - threading: For managing concurrent tasks (e.g., waiting for user input without blocking the main thread).
   - queue: For handling asynchronous input.

You can install all dependencies at once with:
```
pip install -r requirements.txt
```
The requirements.txt file should contain:

- spotipy
- lyricsgenius
- requests


## Error Handling

The script includes basic error handling for:

   - Timeouts: If the Genius API request times out, a message will be displayed.
   - API Errors: If there's any issue fetching data from either API, the error will be logged.
   - Keyboard Interrupt: If you press Ctrl+C, the script will exit gracefully.
   - No Lyrics Found: If the lyrics aren't found for the song, the script will display a message.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contributing

If you'd like to contribute, feel free to fork the repository, make your changes, and create a pull request.


## Example Output
```
>> updating current track [1]

Song: "Blinding Lights" by The Weeknd
Fetching lyrics...

Lyrics:
I've been tryna call
I've been on my own for long enough
Maybe you can show me how to love, maybe...
...
[more lyrics]

>> Enter 0 to open browser
>> Enter 1 for artist info
>> Enter nothing to continue
>> Ctrl+C to exit

>> Enter 0
>> Opening Genius lyrics in the browser...

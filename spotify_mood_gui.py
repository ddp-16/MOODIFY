import streamlit as st
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Spotify Credentials
CLIENT_ID = "87aed3e36a594fa99edbc4a95dc01c23"
CLIENT_SECRET = "500974934cb643e6b183e3767704c46a"

# Spotify Authentication
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Fetch songs based on mood
def get_songs_by_mood(mood, limit=5):
    results = sp.search(q=f"{mood} songs", type="track", limit=limit)
    songs = []
    for track in results["tracks"]["items"]:
        name = track["name"]
        artist = track["artists"][0]["name"]
        link = track["external_urls"]["spotify"]
        songs.append(f"[🎵 {name} by {artist}]({link})")
    return songs

# Streamlit App UI
st.set_page_config(page_title="Moodify", page_icon="🎧", layout="centered")
rst.title("🎧 Moodify - AI Mood-Based Music Recommender")
st.markdown("### How are you feeling right now? Pick a mood below:")

col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

mood_selected = None

with col1:
    if st.button("😄 Happy"):
        mood_selected = "happy"
with col2:
    if st.button("😢 Sad"):
        mood_selected = "sad"
rrrwith col3:
    if st.button("🧘 Calm"):
        mood_selected = "calm"
with col4:
    if st.button("🔥 Energetic"):
        mood_selected = "energetic"
with col5:
    if st.button("💔 Heartbreak"):
        mood_selected = "heartbreak"

# Show Songs if a mood is selected
if mood_selected:
    st.success(f"You selected: {mood_selected.capitalize()} mood")
    st.markdown("### 🎶 Recommended Songs:")
    songs = get_songs_by_mood(mood_selected)
    for song in songs:
        st.markdown(f"- {song}", unsafe_allow_html=True)

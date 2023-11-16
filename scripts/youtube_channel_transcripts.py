from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import os
import re

# Set your API key here
api_key = ""

# Create a YouTube client
youtube = build("youtube", "v3", developerKey=api_key)


def remove_emojis(text):
    # Regex to filter out emojis
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", text)


def get_playlists(channel_id):
    playlists = []
    request = youtube.playlists().list(
        part="snippet", channelId=channel_id, maxResults=50
    )

    while request is not None:
        response = request.execute()
        playlists += [
            (item["id"], item["snippet"]["title"]) for item in response.get("items", [])
        ]
        request = youtube.playlists().list_next(request, response)

    return playlists


def get_videos_from_playlist(playlist_id):
    videos = []
    request = youtube.playlistItems().list(
        part="snippet", playlistId=playlist_id, maxResults=50
    )

    while request is not None:
        response = request.execute()
        videos += [
            (item["snippet"]["resourceId"]["videoId"], item["snippet"]["title"])
            for item in response.get("items", [])
        ]
        request = youtube.playlistItems().list_next(request, response)

    return videos


def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(
            video_id, languages=["en"]
        )
        return " ".join([item["text"] for item in transcript_list])
    except:
        return None


def main():
    channel_id = "UCSp-OaMpsO8K0KkOqyBl7_w"  # Replace with the channel ID
    playlists = get_playlists(channel_id)

    with open("lets_get_rusty_all_transcripts.md", "w") as file:
        for playlist_id, playlist_title in playlists:
            file.write(f"# {playlist_title}\n\n")
            videos = get_videos_from_playlist(playlist_id)
            for video_id, video_title in videos:
                clean_title = remove_emojis(video_title)
                transcript = get_transcript(video_id)
                if transcript:
                    file.write(f"## {clean_title}\n\n{transcript}\n\n")


if __name__ == "__main__":
    main()

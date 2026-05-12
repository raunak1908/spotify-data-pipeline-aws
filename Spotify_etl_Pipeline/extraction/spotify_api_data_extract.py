import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from datetime import datetime
import boto3
import os

def lambda_handler(event, context):

    client_id = os.environ['client_id']
    client_secret = os.environ['client_secret']
    redirect_uri = os.environ['redirect_uri']

    #  Correct OAuth object
    sp_oauth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri
    )

    #  Refresh token
    token_info = sp_oauth.refresh_access_token(
        os.environ['refresh_token']
    )

    access_token = token_info['access_token']

    #  Spotify client
    sp = spotipy.Spotify(auth=access_token)

    #  Fetch data
    results = sp.current_user_recently_played(limit=20)

    songs = []

    for item in results['items']:
        track = item['track']

        songs.append({
            "song_name": track['name'],
            "artist": track['artists'][0]['name'],
            "album": track['album']['name'],
            "played_at": item['played_at'],   
            "date": datetime.now().date()
        })

    df = pd.DataFrame(songs)

    s3 = boto3.client('s3')

    bucket = "spotify-etl-raunak"

    file_name = f"raw/to_processed/spotify_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    
    s3.put_object(
        Bucket=bucket,
        Key=file_name,
        Body=df.to_csv(index=False)
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
import json
import boto3
import pandas as pd

def lambda_handler(event, context):

    s3 = boto3.client('s3')
    bucket = "spotify-etl-raunak"

    #  Get latest processed file
    response = s3.list_objects_v2(
        Bucket=bucket,
        Prefix="raw/to_processed/"
    )

    latest_file = sorted(
        response['Contents'],
        key=lambda x: x['LastModified'],
        reverse=True
    )[0]['Key']

    #  Read file
    obj = s3.get_object(Bucket=bucket, Key=latest_file)
    df = pd.read_csv(obj['Body'])
    df['played_at'] = pd.to_datetime(df['played_at'],utc = True)\
                        .dt.tz_convert('Asia/Kolkata')\
                        .dt.strftime('%Y-%m-%d %H:%M')

    #  TRANSFORMATIONS

    #  SONGS DATA
    songs_df = df[["song_name", "artist", "album", "played_at"]].drop_duplicates()

    #  ARTIST DATA
    artist_df = df[["artist"]].drop_duplicates()

    #  ALBUM DATA
    album_df = df[["album", "artist"]].drop_duplicates()

    #  SAVE TO S3

    timestamp = pd.Timestamp.now().strftime('%Y-%m-%d_%H-%M-%S')

    s3.put_object(
        Bucket=bucket,
        Key=f"transformed/songs_data/songs_{timestamp}.csv",
        Body=songs_df.to_csv(index=False)
    )

    s3.put_object(
        Bucket=bucket,
        Key=f"transformed/artist_data/artists_{timestamp}.csv",
        Body=artist_df.to_csv(index=False)
    )

    s3.put_object(
        Bucket=bucket,
        Key=f"transformed/album_data/albums_{timestamp}.csv",
        Body=album_df.to_csv(index=False)
    )

    new_key = latest_file.replace("raw/to_processed/", "raw/processed/")

    #copy file
    s3.copy_object(
        Bucket=bucket,
        CopySource={'Bucket': bucket, 'Key': latest_file},
        Key=new_key
    )

    #delete file
    s3.delete_object(
        Bucket=bucket,
        Key=latest_file
    )

    return {
            'statusCode': 200,
            'body': json.dumps('Transformation to structured data successful')
        }
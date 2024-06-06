

#import m3u8

import requests

url = "https://vz-53f46a8a-1c1.b-cdn.net/207c5cfe-d90d-41b9-b681-cf9892d6357f/thumbnail.jpg"
response = requests.get(url, stream=True)

if response.status_code == 200:
    with open('output.zip', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

# m3u8_master = m3u8.loads(r.text)
# playlist_url = m3u8_master.data['playlists'][0]['uri']
# r = requests.get(playlist_url)
# playlist = m3u8.loads(r.text)
# playlist.data['segments'][0]['uri']
# r = requests.get(playlist.data['segments'][0]['uri'])
# r.content
# with open("video.ts", 'wb') as f:
#     for segment in playlist.data['segments']:
#         url = segment['uri']
#         r = request.get(url)
#         f.write(r.content)
# #ts file to mp3
# subprocess.run(['ffmpeg', '-i', 'vidio.ts', 'vidio.mp4'])




# with open("lynda.mp4", "wb") as f:
#     for chunk in r.iter_content(chunk_size=chunk_size):
#         f.write(chunk)
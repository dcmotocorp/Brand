from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#this is the first api

api_key = 'AIzaSyBYkInQobwWohKd8VGkhUvOCO3Fvu2GfJQ'
youtube = build('youtube', 'v3', developerKey=api_key)



response = youtube.videos().list(
    part='snippet',
    chart='mostPopular',
    regionCode='IN',
    videoCategoryId='0',
    maxResults=100
).execute()


tag_counts = {}

for item in response['items']:
     tags = item['snippet'].get('tags')
     print(tags)
     print("================")
#     for tag in tags:
#         if tag in tag_counts:
#             tag_counts[tag] += 1
#         else:
#             tag_counts[tag] = 1


# sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
# for i in range(100):
#     print(sorted_tags[i][0])

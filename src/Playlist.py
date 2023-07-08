# Импорт библиотек
import datetime
import isodate
import src.channel


# Объявление класса PlayList
class PlayList:

    # Конструктор класса
    def __init__(self, playlist_id):
        # при создании объекта класса производим запрос о видео в плей-листах
        playlist_videos = src.channel.youtube.playlistItems().list(playlistId=playlist_id,
                                                                          part='contentDetails',
                                                                          maxResults=50,
                                                                          ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        self.__video_response = src.channel.youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(video_ids)).execute()
        self.__playlist_id = playlist_id
        self.title = src.channel.youtube.playlists().list(
            part='snippet', id=self.__playlist_id).execute()['items'][0]['snippet']['localized']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"

    @property
    def total_duration(self):
        """
        Метод возвращающий длительность всех видео
        в плей-листе в формате datetime.timedelta
        """
        duration = datetime.timedelta(0)
        for video in self.__video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration

    def show_best_video(self):
        """
        Метод возвращающий ссылку на самое
        популярное видео (по просмотрам)
        """
        view_count = 0
        best_video = ''
        for b_video in self.__video_response['items']:
            if int(b_video['statistics']['viewCount']) > view_count:
                best_video = b_video['id']
                view_count = int(b_video['statistics']['viewCount'])
        return f"https://youtu.be/{best_video}"

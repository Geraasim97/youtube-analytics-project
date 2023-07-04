import src.channel
class Video:
    def __init__(self, id_video):
        self.id_video = id_video
        try:
            self.__video_data = src.channel.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                                  id=id_video).execute()
            self.title = self.__video_data["items"][0]["snippet"]["title"]
            self.video_link = f'https://www.youtube.com/watch?v={id_video}'
            self.view_count = self.__video_data["items"][0]["statistics"]["viewCount"]
            self.like_count = self.__video_data["items"][0]["statistics"]["likeCount"]

        except IndexError:
            self.__video_data = None
            self.title = None
            self.video_link = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        """
        Метод str - вывод информации о видео
        """
        return f'{self.title}'


# Объявляем дочерний от Video класс PLVideo
class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        """
        Инициализация атрибутов класса + дополнительный
        защищенный атрибут playlist_data в котором все данные
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.__playlist_data = src.channel.youtube.playlistItems().list(playlistId=playlist_id,
                                                                        part='contentDetails,snippet',
                                                                        maxResults=50,
                                                                        ).execute()

    def __str__(self):
        """
        Переопределение метода str для класса PLVideo
        """
        return self.__playlist_data['items'][0]['snippet']['title']
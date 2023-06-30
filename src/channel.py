import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        youtube = Channel.get_service()
        result = youtube.channels().list(id=self.__channel_id, part="snippet, statistics").execute()

        self.title = result["items"][0]["snippet"]["title"]
        self.description = result["items"][0]["snippet"]["description"].split(":)")[0]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.video_count = result["items"][0]["statistics"]["videoCount"]
        self.view_count = result["items"][0]["statistics"]["viewCount"]
        self.subscriber_count = result["items"][0]["statistics"]["subscriberCount"]

        def __str__(self):
            return f"{self.title} ({self.url})"

        def __add__(self, other):
            return int(self.subscriber_count) + int(other.subscriber_count)

        def __sub__(self, other):
            return int(self.subscriber_count) - int(other.subscriber_count)

        def __gt__(self, other):
            return int(self.subscriber_count) > int(other.subscriber_count)

        def __ge__(self, other):
            return int(self.subscriber_count) >= int(other.subscriber_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        api_key_my_youtube: str = os.getenv('YT-API-KEY')

        youtube = build('youtube', 'v3', developerKey=api_key_my_youtube)

        result = youtube.channels().list(id=self.__channel_id, part="snippet, statistics").execute()

        result = json.dumps(result, indent=2, ensure_ascii=False)

        print(result)

    @classmethod
    def get_service(cls):
        api_key_my_youtube: str = os.getenv('YT-API-KEY')
        return build('youtube', 'v3', developerKey=api_key_my_youtube)

    def to_json(self, name_of_file):
        self_to_out = {
            "__channel_id": self.__channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "video_count": self.video_count,
            "view_count": self.view_count,
            "subscriber_count": self.subscriber_count
        }
        with open(name_of_file, "w", encoding="utf-8") as outfile:
            json.dump(self_to_out, outfile)

    @property
    def channel_id(self):
        return self.__channel_id
import requests
import os
import json
from googleapiclient.discovery import build

api_key = "AIzaSyBSduYPmnqebyvrcoCz9IW40GNZbc18KJk"
youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__channel=(self.__channel_id)
        self.__description = self.__channel['items'][0]['snippet']['description']
        self.__title=self.__channel['items'][0]['snippet']['title']
        self.__url=f'https://www.youtube.com/channel/{self.__channel_id}'
        self.__subscribers_count = int(self.__channel['items'][0]['statistics']['subscriberCount'])
        self.__video_count = int(self.__channel['items'][0]['statistics']['videoCount'])
        self.__views_count =int(self.__channel['items'][0]['statistics']['viewsCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    "Возвращает название канала"
    @property
    def title(self):
        return self.__title

    "Возвращает описание канала"
    @property
    def description(self):
        return self.__description

    "Возвращает ссылку на канал канала"
    @property
    def url(self):
        return self.__url

    "Возвращает кол-во подписчиков канала"
    @property
    def subscribers_count(self):
        return self.__subscribers_count

    "Возвращает кол-во видео на канале"
    @property
    def video_count(self):
        return self.__video_count

    "Возвращает кол-во просмотров"
    @property
    def views_count(self):
        return self.__views_count

    " Геттер Возвращает id канала"
    @property
    def channel_id(self):
        return self.__channel_id

    " Сеттер Возвращает id канала"
    @channel_id.setter
    def channel_id(self, id):
        print("AttributeError: property 'channel_id' of 'Channel' object has no setter")

    "Класс-метод возвращает объект для работы с Youtube API"
    @classmethod
    def get_service(cls):
        return cls.__channel

    def to_json(self, filename) -> None:
        "Метод возвращает в json значения атрибутов экземпляра Channel"
        data = {
            'channel_id': self.__channel_id,
            'title': self.__title,
            'description': self.__description,
            'url': self.__url,
            'subscribers_count': self.__subscribers_count,
            'video_count': self.__video_count,
            'views_count': self.__views_count
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)


import json


class PostsDAO:

    """ Класс ответственный за работу со всеми постами"""

    def __init__(self, path):
        self.path = path

    def _load(self):
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def get_all(self):
        """ Возвращает все посты"""
        return self._load()

    def get_by_pk(self, pk):
        """Возвращает пост по идентефикатору"""
        posts = self.get_all()

        for post in posts:
            if post['pk'] == pk:
                return post

    def get_by_user(self, username):
        """Возвращвет по определенному имени"""
        posts = self.get_all()
        posts_by_user = []

        for post in posts:
            if post["poster_name"] == username:
                posts_by_user.append(post)

        return posts_by_user

    def search(self, query):
        """Возвращает список словарей по вхождению query"""
        posts = self.get_all()
        matching_post = []

        query_lower = query.lower()

        for post in posts:
            if query_lower in post["content"].lower():
                matching_post.append(post)

        return matching_post

from run import app

class TestApi:

    def test_app_all_posts_status_code(self):
        """Проверяем получен ли список"""
        response = app.test_client().get('api/posts', follow_redirect=True)

        print(response.status_code)
        print(response.mimetype)

        assert response.status_code == 200, "Статус код запроса всех постов не верный"
        assert response.mimetype == "application/json", "Получен не Json"

    def test_app_one_posts_status_code(self):
        """Проверяем получен ли один пост"""
        response = app.test_client().get('api/posts/1', follow_redirect=True)

        print(response.status_code)
        print(response.mimetype)

        assert response.status_code == 200, "Статус код запроса всех постов не верный"
        assert response.mimetype == "application/json", "Получен не Json"
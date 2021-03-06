from flask import Flask

from app.posts.veiws import posts_blueprint
from app.api.veiws import api_blueprint
from app import logger

app = Flask(__name__)

logger.create_logger()

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == '__main__':
    app.run(debug=True, port=8002)
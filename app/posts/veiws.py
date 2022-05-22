import logging

from flask import Blueprint, render_template, request, abort
from app.posts.dao.posts_dao import PostsDAO
import app.posts.dao.comments_dao

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO("data/posts.json")
comments_dao = app.posts.dao.comments_dao.CommentsDAO("data/comments.json")

logger = logging.getLogger("basic")


@posts_blueprint.route('/')
def posts_all():

    logger.debug("Запрошены все посты")
    try:
        posts = posts_dao.get_all()
        return render_template("index.html", posts=posts)
    except:
        return "Ошибка"


@posts_blueprint.route('/posts/<int:post_pk>/')
def posts_one(post_pk):

    logger.debug(f"Запрошен помт {post_pk}")
    try:
        post = posts_dao.get_by_pk(post_pk)
        if post is None:
            abort(404)
        comments = comments_dao.get_by_post_pk(post_pk)
        number_comments = len(comments)
        return render_template("post.html", post=post, comments=comments, number_comments=number_comments)
    except:
        return "Нет таких постов"


@posts_blueprint.route('/search/')  # поиск по постам
def posts_search():
    query = request.args.get("s", None)
    posts = posts_dao.search(query)
    number_of_posts = len(posts)
    return render_template("search.html", query=query, posts=posts, number_of_posts=number_of_posts)


@posts_blueprint.route('/user/<username>/')  # поиск по именам
def posts_by_user(username):
    posts = posts_dao.get_by_user(username)
    return render_template("user-feed.html", posts=posts)



@posts_blueprint.errorhandler(404)
def post_error(e):
    return "Нет таких постов", 404



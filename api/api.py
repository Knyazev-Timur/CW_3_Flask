from flask import Blueprint
from utils import read_json
from logs.loging import logger_settings
import os

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')

path_start = os.path.abspath('api.py')
path_dir = os.path.dirname(path_start)
path_file = os.path.abspath('logs/api.log')
path_log = os.path.relpath(path_file, path_start)
# print(path_start)
# print(path_file)
# print(path_log)


@api_blueprint.route('/posts/')
def api_all_posts():
    """
    :return: dict
    получает данные из JSON и возвращает список всех постов
    """
    logger_settings(path_log, 'Запрос /api/posts')
    all_posts = read_json('../data/posts.json')
    return all_posts


@api_blueprint.route('/posts/<int:post_id>')
def api_post_pk(post_id):
    """
    :param post_id: int
    :return:dict
    Получает номер поста в виде int:post_id и возвращает словарь с постом
    """
    logger_settings(path_log, f"Запрос /api/posts/{post_id}")
    all_posts = read_json('../data/posts.json')
    for post in all_posts:
        if post_id == post.get('pk'):
            return post

from flask import Blueprint
from utils import read_json
# from logs.loging import logger_settings
import os
import logging

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')

path_api = os.path.abspath('app.py')
path_log_api = os.path.abspath('api.log')
path_file = os.path.relpath(path_log_api, path_api)
# path_file ='../logs/api.log'
print(path_api)
print(path_log_api)
print(path_file)

logging.basicConfig(level=logging.INFO)


logger_file = logging.getLogger('3')
file_handler = logging.FileHandler(path_file, encoding='UTF-8')
formatter_one = logging.Formatter("%(asctime)s : %(levelname)s :%(message)s")
file_handler.setFormatter(formatter_one)
logger_file.addHandler(file_handler)

consol_loger = logging.getLogger('4')
console_handler = logging.StreamHandler()
formatter_two = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
console_handler.setFormatter(formatter_two)
consol_loger.addHandler(console_handler)


@api_blueprint.route('/posts/')
def api_all_posts():
    """
    :return: dict
    получает данные из JSON и возвращает список всех постов
    """
    # logger_settings('../logs/api.log', 'Запрос /api/posts')
    print("@api_blueprint.route('/posts/')")
    print(path_file)
    logger_file.info('Запрос /api/posts')
    consol_loger.info('Запрос /api/posts')
    all_posts = read_json('../data/posts.json')
    return all_posts


@api_blueprint.route('/posts/<int:post_id>')
def api_post_pk(post_id):
    """
    :param post_id: int
    :return:dict
    Получает номер поста в виде int:post_id и возвращает словарь с постом
    """
    print("@api_blueprint.route('/posts/<int:post_id>')")
    print(path_file)
    # logger_settings('../logs/api.log', f"Запрос /api/posts/{post_id}")
    logger_file.info(f"Запрос /api/posts/{post_id}")
    consol_loger.info(f"Запрос /api/posts/{post_id}")
    all_posts = read_json('../data/posts.json')
    for post in all_posts:
        if post_id == post.get('pk'):
            return post

# print(api_all_posts())
# print(api_post_pk(1))
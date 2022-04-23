from User import *
from DataBase import *


class Post:

    def __init__(self, ID):
        self.id = ID
        insert_post_id(ID)
        self.author = get_db_value("author", "post", ID)
        self.link = get_db_value("link", "post", ID)
        self.type = get_db_value("type", "post", ID)
        self.text = get_db_value("text", "post", ID)
        self.nLikes = get_db_value("likes", "post", ID)
        self.comments = get_db_value("comments", "post", ID)

        self.likes = get_likes(ID)

        self.posts = []

"""
    def __init__(self, post_id, author, link, post_type, text, likes, comments, date):
        self.id = post_id
        self.author = author
        self.link = link
        self.type = post_type
        self.text = text
        self.likes = likes
        self.comments = comments
        self.date = date
        insert_post_all(post_id, author, link, post_type, text, likes, comments, date)


    def load_posts(self):
        self.posts.extend(get_posts_ids(self.author))
"""



from Post import *
from DataBase import *
from App import *
from Bot import *


class User:

    def __init__(self, user_id):
        self.id = user_id
        insert_user_id(user_id)
        self.login = get_db_value("login", "user", user_id)
        self.name = get_db_value("name", "user", user_id)
        self.nPosts = get_db_value("posts", "user", user_id)
        self.nFollowers = get_db_value("followers", "user", user_id)
        self.nFollowing = get_db_value("following", "user", user_id)
        self.webLink = get_db_value("webLink", "user", user_id)
        self.activeStory = get_db_value("activeStory", "user", user_id)
        self.scanTime = get_db_value("scanTime", "user", user_id)

        self.followers = get_followers(user_id)
        self.following = get_followings(user_id)

        self.posts = []
        for post in get_posts_ids(user_id):
            self.posts.append(Post(post))

    

"""
    def __init__(self, login):
        ID = get_db_user_id_from_login(login)
        self.id = ID
        insert_user_id(ID)
        self.login = get_db_value("login", "user", ID)
        self.name = get_db_value("name", "user", ID)
        self.nPosts = get_db_value("posts", "user", ID)
        self.nFollowers = get_db_value("followers", "user", ID)
        self.nFollowing = get_db_value("following", "user", ID)
        self.webLink = get_db_value("webLink", "user", ID)
        self.activeStory = get_db_value("activeStory", "user", ID)
        self.scanTime = get_db_value("scanTime", "user", ID)

        self.followers = get_followers(ID)
        self.following = get_followings(ID)

        self.posts = []
        for post in get_posts_ids(ID):
            self.posts.append(Post(ID=post))



    def __init__(self, ID, login, name, nPosts, nFollowers, nFollowing, webLink, activeStory):
        self.id = ID
        insert_user_id(ID)
        self.login = login
        self.name = name
        self.nPosts = nPosts
        self.nFollowers = nFollowers
        self.nFollowing = nFollowing
        self.webLink = webLink
        self.activeStory = activeStory
        self.scanTime = datetime.now()
        insert_user_info(ID, login, name, nPosts, nFollowers, nFollowing, webLink, activeStory)
"""


def get_loader_profile(self, botLoader):
    if self.login is not None:
        pr = instaloader.Profile.from_username(botLoader.context, self.login)
    else:
        pr = instaloader.Profile.from_id(botLoader.context, self.id)
    self.profile = pr


def user_from_login(login):
    user_id = get_db_user_id_from_login(login)
    u = User(user_id)
    return u


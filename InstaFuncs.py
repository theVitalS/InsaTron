from mysql import *
from DataBase import *
import instaloader
# from Bot import *
from User import *
import time
import random
from instaloader import TooManyRequestsException
# , TooManyRequestsExceptionMy
from Post import *

db = connect()

curs = db.cursor()


def scan_basic_info_by_username(botLoader, username):
    pr = instaloader.Profile.from_username(botLoader.context, username)
    insert_user_from_profile(pr)
    u = User(user_id=pr.userid)
    u.profile = pr
    return u


def scan_basic_info_by_id(botLoader, userid):
    pr = instaloader.Profile.from_id(botLoader.context, userid)
    insert_user_from_profile(pr)
    u = User(pr.userid)
    u.profile = pr
    return u


def scan_user(bot, pr):
    """done = False
    while not done:
        try:
            user_id = pr.userid
            if not if_user_info_in_table(user_id):
                insert_user_from_profile(pr)
            u = User(user_id)
            u.profile = pr
            done = True
        except TooManyRequestsExceptionMy:
            print("we caught an ERROR !!!!!!!!!")
            pause(5, 15)
            bot.change_bot()
            done = False"""

    user_id = pr.userid
    if not if_user_info_in_table(user_id):
        insert_user_from_profile(pr)
    u = User(user_id)
    u.profile = pr

    return u


def scan_followings(bot, profile):
    """done = False
    while not done:
        try:
            followings = profile.get_followees()
            follower_id = profile.userid
            done = True
        except TooManyRequestsExceptionMy:
            print("we caught an ERROR !!!!!!!!!")
            pause(5, 15)
            bot.change_bot()
            done = False"""
    followings = profile.get_followees()
    follower_id = profile.userid

    n = 0
    number_of_requests = 0

    print("{} -- scanning followings of user {}".format(datetime.now(),  follower_id))

    insert_user_id(follower_id)

    for following in followings:

        """done = False
        while not done:
            try:
                followed_id = following.userid
                done = True
            except TooManyRequestsExceptionMy:
                print("we caught an ERROR !!!!!!!!!")
                pause(5, 15)
                bot.change_bot()
                done = False"""

        followed_id = following.userid

        number_of_requests += 1
        insert_user_id(followed_id)
        insert_follow(follower_id, followed_id)
        n += 1
        if n > 10 + random.random()*7:
            time.sleep(random.random())
            n = 0

    print("{} -- {} followings of user {} inserted".format(datetime.now(), number_of_requests, follower_id))

    return number_of_requests


def scan_followers(bot, profile):
    n = 0
    number_of_requests = 0

    followers = profile.get_followers()
    followed_id = profile.userid

    insert_user_id(followed_id)
    for follower in followers:

        follower_id = follower.userid
        number_of_requests += 1
        insert_user_id(follower_id)
        insert_follow(follower_id, followed_id)
        n += 1
        if n > 10 + random.random() * 7:
            time.sleep(random.random() * 3)
            n = 0

    print("{} followers of user {} inserted".format(number_of_requests, followed_id))

    return number_of_requests


def scan_posts(bot, profile, max=0, scan_info=False, scan_likes=True, scan_likers=False, scan_comments=False, scan_tags=False):

    """done = False
    while not done:
        try:
            posts = profile.get_posts()
            author = profile.userid
            done = True
        except TooManyRequestsExceptionMy:
            print("we caught an ERROR !!!!!!!!!")
            pause(20, 60)
            bot.change_bot()
            done = False"""

    posts = profile.get_posts()
    author = profile.userid

    n = 0
    for post in posts:
        n += 1
        if max == 0 or (max > 0 and n < max):
            post_id = post.mediaid
            if not if_fresh_entry('post', post_id):

                if scan_info:
                    insert_post_all(post_id, author, post.shortcode, 1, post.caption, post.likes, post.comments,
                                    post.date)
                else:
                    insert_post_basics(post_id, author)

                if scan_likes:
                    likers = post.get_likes()
                    z = 0
                    for liker in likers:
                        x = 0
                        if scan_likers:
                            u = scan_user(liker)
                            liker_id = u.id
                            time.sleep(random.random() * 2)
                        else:
                            liker_id = liker.userid
                            insert_user_id(liker_id)

                        insert_like(liker_id, post_id)
                        x += 1
                        z += 1
                        if x > 10 + random.random() * 10:
                            time.sleep(random.random() * 3)
                            x = 0
                    print("{} -- {} likes on post {} inserted".format(datetime.now(), z, post_id))

                if scan_tags:
                    tags = post.caption_hashtags
                    for posttag in tags:
                        insert_tag(posttag)
                        insert_tag_in_post(posttag, post_id)

                if scan_comments:
                    comments = post.get_comments()
                    for comment in comments:
                        own = scan_user(comment.owner)
                        insert_comment(comment.id, post_id, own.id, comment.text,
                                       comment.likes_count, comment.created_at_utc)

                print("{} -- Post {}  author {} successfully scanned".format(datetime.now(), post_id, author))
                pause(40, 120)
                print("____________________________________________________")
        """try:
            if max == 0 or (max > 0 and n < max):
                post_id = post.mediaid
                if not if_fresh_entry('post', post_id):

                    if scan_info:
                        insert_post_all(post_id, author, post.shortcode, 1, post.caption, post.likes, post.comments, post.date)
                    else:
                        insert_post_basics(post_id, author)

                    if scan_likes:
                        likers = post.get_likes()
                        z = 0
                        for liker in likers:
                            x = 0
                            if scan_likers:
                                u = scan_user(liker)
                                liker_id = u.id
                                time.sleep(random.random()*2)
                            else:
                                liker_id = liker.userid
                                insert_user_id(liker_id)

                            insert_like(liker_id, post_id)
                            x += 1
                            z += 1
                            if x > 10 + random.random() * 10:
                                time.sleep(random.random() * 3)
                                x = 0
                        print("{} -- {} likes on post {} inserted".format(datetime.now(), z, post_id))

                    if scan_tags:
                        tags = post.caption_hashtags
                        for posttag in tags:
                            insert_tag(posttag)
                            insert_tag_in_post(posttag, post_id)

                    if scan_comments:
                        comments = post.get_comments()
                        for comment in comments:
                            own = scan_user(comment.owner)
                            insert_comment(comment.id, post_id, own.id, comment.text,
                                           comment.likes_count, comment.created_at_utc)

                    print("{} -- Post {}  author {} successfully scanned".format(datetime.now(), post_id, author))
                    pause(40, 120)
                    print("____________________________________________________")

        except TooManyRequestsExceptionMy:
            print("we caught an ERROR !!!!!!!!!")
            pause(20, 60)
            bot.change_bot()"""

    return posts



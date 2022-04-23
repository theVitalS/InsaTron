from InstaFuncs import *
from DataBase import *


def multiscanner(bot, ids, to_scan_user_info=True, to_scan_posts=False, n_posts=20, to_scan_post_info=False,
                 to_scan_likes=True, to_scan_likers=False, to_can_comments=False, to_scan_tags=False,
                 to_scan_followers=False, to_scan_followings=False):
    n = 0
    for user_id in ids:
        print("{} -- scanning user {}".format(datetime.now(), user_id))
        insert_user_id(user_id)
        profile = 0
        profile = instaloader.Profile.from_id(bot.context, user_id)
        pause(1, 3, False)
        """while profile == 0:
            try:
                profile = instaloader.Profile.from_id(bot.context, user_id)
                pause(1, 3, False)
            except TooManyRequestsExceptionMy as error:
                print("we caught an ERROR !!!!!!!!!")
                profile = 0
                bot.change_bot()"""

        if to_scan_user_info:
            scan_user(bot, profile)
            pause(1, 3, False)

            n += 1

        if get_db_value("isPrivate", "user", user_id) != 1 and len(get_followings(user_id)) == 0:
            if to_scan_posts:
                scan_posts(bot, profile, n_posts, to_scan_post_info, to_scan_likes, to_scan_likers, to_can_comments,
                           to_scan_tags)
                pause(10, 30)

            if to_scan_followers:
                scan_followers(bot, profile)
                pause(5, 20)

            if to_scan_followings:
                scan_followings(bot, profile)
                pause(10, 30)

        else:
            pause(5, 15)
        print("{} -- user {}({}) successfully scanned".format(datetime.now(), get_db_user_login_from_id(user_id),
                                                              user_id))
        if n == 15:
            n = 0
            bot.change_bot()
        else:
            pause(25, 90)

        print("__________________________________________")


def get_top_likers(user, parameter, value_type="amount"):
    posts = get_posts_ids(user.id)
    likes = []
    for post in posts:
        likes.extend(get_likes(post))
    likers = {}
    for like in likes:
        likers[like] = likes.count(like)

    result = {}
    if parameter == 0:
        for liker in sorted(likers, key=likers.get, reverse=True):
            result[liker] = likers[liker]
    else:
        if value_type == "amount":
            for liker in sorted(likers, key=likers.get, reverse=True)[0:parameter]:
                result[liker] = likers[liker]
        else:
            for liker in sorted(likers, key=likers.get, reverse=True):
                if likers[liker] >= parameter:
                    result[liker] = likers[liker]

    return result


def count_likers(user):
    likers = get_top_likers(user, 0)

    amount_of_likes = []
    for liker in likers:
        amount_of_likes.append(likers[liker])

    amount_of_likes.sort(reverse=True)

    cumulated_likes = {}
    n = 0
    for am in amount_of_likes:
        if not (am in cumulated_likes):
            n += amount_of_likes.count(am)
            cumulated_likes[am] = n

    for amount in cumulated_likes:
        print("We have {} users who gave {} likes or more".format(cumulated_likes[amount], amount))

    return cumulated_likes


def get_ghost_followers(user):

    followers = get_followers(user)
    posts = get_posts_ids(user.id)
    likes = []

    for post in posts:
        likes.extend(get_likes(post))

    ghosts = followers - likes
    return ghosts

    

""" top_likers_uns = {}
    top_likers = {}

    for liker in likers:
        if cumulated_likes[likers[liker]]/len(likers) < percent/100:
            top_likers_uns[liker] = likers[liker]

    for liker in sorted(top_likers_uns, key=top_likers_uns.get, reverse=True):
        top_likers[liker] = likers[liker]"""

"""
def most_followed(users, percent):
    followed_list = []
    for user in users:
        scan_followings()
        followed_list.extend(get_followings(user))

    followed = {}
    for follow in followed_list:
        followed[follow] = followed_list.count(follow)


    amount_of_followers = []
    for foll in followed:
        amount_of_followers.append(followed[foll])

    amount_of_followers.sort(reverse=True)

    cumulated_follows = {}
    n = 0
    for am in amount_of_followers:
        if not (am in cumulated_follows):
            n += amount_of_followers.count(am)
            cumulated_follows[am] = n

    top_followed_uns = {}
    top_followed = {}

    for follow in followed:
        if cumulated_follows[followed[follow]] / len(followed) < percent / 100:
            top_followed_uns[follow] = followed[follow]

    for follow in sorted(top_followed_uns, key=top_followed_uns.get, reverse=True):
        top_followed[follow] = followed[follow]

    return top_followed
"""

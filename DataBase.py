# import mysql.connector
from datetime import datetime
# from mysql.connector import (connection)
import sqlite3


def connect():
    # db_con = mysql.connector.connect(host='localhost', user='admin', password='admin', database='test1')
    # db_con = connection.MySQLConnection(host='localhost', user='root', password='1a12s23d3', database='instaintel')

    connection = sqlite3.connect('Info.db')
    return connection


db = connect()
curs = db.cursor()


def commit():
    db.commit()


# -----------------------CHECKS-------------------------------------


def if_user_id_in_table(user_id):
    curs.execute("SELECT userID FROM USER WHERE userID={}".format(user_id))
    for (ID,) in curs:
        if ID is not None:
            return True
        else:
            return False


def if_user_info_in_table(user_id):
    curs.execute("SELECT login FROM USER WHERE userID={}".format(user_id))
    for (ID,) in curs:
        if ID is not None:
            return True
        else:
            return False


def if_post_id_in_table(post_id):
    curs.execute("SELECT postID FROM POST WHERE postID={}".format(post_id))
    for (ID,) in curs:
        if ID is not None:
            return True
        else:
            return False


def if_post_info_in_table(post_id):
    curs.execute("SELECT link FROM POST WHERE postID={}".format(post_id))
    for (ID,) in curs:
        if ID is not None:
            return True
        else:
            return False


def if_comment_in_table(comment_id):
    curs.execute("SELECT CommentID FROM comment WHERE CommentID={}".format(comment_id))
    for (CommentID,) in curs:
        if CommentID is not None:
            return True
        else:
            return False


def if_follow_in_table(follower_id, followed_id):
    curs.execute("SELECT followID FROM FOLLOW WHERE follower={} AND followed={}".format(follower_id, followed_id))
    for (ID,) in curs:
        if ID is not None:
            return True
        else:
            return False


def if_like_in_table(post_id, user_id):
    curs.execute("SELECT likeID FROM LIKES WHERE user={} AND post={}".format(user_id, post_id))
    for (ID,) in curs:
        if ID is not None:
            return True
        else:
            return False


def if_tag_in_table(tag):
    curs.execute("SELECT tag FROM hashtag WHERE tag='{}'".format(tag))
    for (tag,) in curs:
        if tag is not None:
            return True
        else:
            return False


def if_tag_in_post_in_table(tag, post_id):
    curs.execute("SELECT tag FROM taginpost WHERE tag='{}' AND post={}".format(get_tagid(tag), post_id))
    for (tag,) in curs:
        if tag is not None:
            return True
        else:
            return False


def if_fresh_entry(table, entry_id):
    if get_db_value("scanTime", table, entry_id) is None:
        return False
    elif (datetime.now() - get_db_value("scanTime", table, entry_id)).days > 1:
        return False
    else:
        return True


#  ------------------------------------------INSERTS-----------------------------------------
def insert_user_id(user_id):
    if not if_user_id_in_table(user_id):
        # print("Inserting user id {} into database".format(user_id))
        curs.execute("INSERT INTO USER (userID) VALUES ({})".format(user_id))
        db.commit()


def insert_user_login(user_id, us_login):
    if not if_user_info_in_table(user_id):
        # print("Inserting info for user {}".format(user_id))
        #us_login_upd = us_login.replace("'", "''")
        curs.execute("UPDATE USER SET login='{}' WHERE userID={}".format(us_login, user_id))
        db.commit()


def insert_user_info(user_id, us_login, us_name, us_posts, us_followers, us_following, us_webLink, us_activeStory):
    if not if_user_info_in_table(user_id):
        # print("Inserting info for user {}".format(user_id))
        us_name_upd = us_name.replace("'", "''")
        print("UPDATE USER SET login='{}',"
         " name='{}',"
         " posts={}, followers={}, following={},"
         " webLink='{}', "
         "activeStory='{}', scanTime='' WHERE userID={}".format(us_login, us_name_upd, us_posts,
                                                              us_followers, us_following, us_webLink,
                                                              us_activeStory, user_id))


        curs.execute("UPDATE USER SET login='{}',"
                     " name='{}',"
                     " posts={}, followers={}, following={},"
                     " webLink='{}', "
                     "activeStory='{}', scanTime='' WHERE userID={}".format(us_login, us_name_upd, us_posts,
                                                                           us_followers, us_following, us_webLink,
                                                                          us_activeStory, user_id))
        db.commit()


def insert_user_all(user_id, us_login, us_name, us_posts, us_followers, us_following, us_webLink, us_activeStory):
    insert_user_id(user_id)
    insert_user_info(user_id, us_login, us_name, us_posts, us_followers, us_following, us_webLink, us_activeStory)


def insert_user_from_profile(pr):
    user_id = pr.userid
    if not if_user_info_in_table(user_id):
        insert_user_all(user_id, pr.username, pr.full_name, pr.mediacount, pr.followers, pr.followees, '','')
                      #  pr.external_url, pr.has_public_story)


def insert_post_id(post_id):
    if not if_post_id_in_table(post_id):
        print("Inserting post id {}".format(post_id))
        curs.execute("INSERT INTO POST (postID) VALUES ({})".format(post_id))
        db.commit()


def insert_post_basics(post_id, author):
    if not if_post_id_in_table(post_id):
        print("{} -- Inserting post id {}".format(datetime.now(), post_id))
        curs.execute("INSERT INTO POST (postID, author, scanTime) VALUES ({},{}, '')".format(post_id, author))
        db.commit()


def insert_post_info(post_id, link, post_type, text, likes, comments):
    if not if_post_info_in_table(post_id):
        print("Inserting info for post {}".format(post_id))
        if isinstance(text, str):
            text_upd = text.replace("'", "\\'")
        else:
            text_upd = text
        curs.execute("UPDATE POST SET link='{}', type={}, text='{}', likes={}, "
                     "comments={}, scanTime='' WHERE postID={}".format(link, post_type, text_upd, likes,
                                                                                   comments,  post_id))
        db.commit()


def insert_post_all(post_id, author, link, post_type, text, likes, comments): #, date):
    print("{} -- Inserting info for post {}, author {}".format(datetime.now(), post_id, author))
    insert_post_basics(post_id, author)
    insert_post_info(post_id, link, post_type, text, likes, comments)


def insert_like(user_id, post_id):
    if not if_like_in_table(post_id, user_id):
        #print("Inserting like from {} on post {}".format(user_id, post_id))
        curs.execute("INSERT INTO LIKES (post, user) VALUES ({},{})".format(post_id, user_id))
        db.commit()


def insert_follow(follower_id, followed_id):
    if not if_follow_in_table(follower_id, followed_id):
        # print("{} --- Inserting {} following {}".format(datetime.now(), follower_id, followed_id))
        curs.execute("INSERT INTO FOLLOW (follower, followed) VALUES ({},{})".format(follower_id, followed_id))
        db.commit()


def insert_tag(newtag):
    if not if_tag_in_table(newtag):
        print("Inserting tag {}".format(newtag))
        curs.execute("INSERT INTO hashtag (tag) VALUES ('{}')".format(newtag))
        db.commit()


def insert_tag_in_post(newtag, post_id):
    if not if_tag_in_post_in_table(newtag, post_id):
        print("Inserting tag {} in post {}".format(newtag, post_id))
        curs.execute("INSERT INTO taginpost (tag, post) VALUES ({}, {})".format(get_tagid(newtag), post_id))
        db.commit()


def insert_comment(comment_id, post_id, user_id, text, likes, create_time):
    if not if_comment_in_table(comment_id):
        if isinstance(text, str):
            text_upd = text.replace("'", "\\'")
        print("Inserting comment {} in post {}".format(comment_id, post_id))
        curs.execute("INSERT INTO comment (CommentID, post, user, text, likes) VALUES ({}, {}, {}, '{}', "
                     "{})".format(comment_id, post_id, user_id, text_upd, likes))
        db.commit()


def set_dummies():
    # (user_id, us_login, us_name, us_posts, us_followers, us_following, us_webLink, us_activeStory, is_private)
    insert_user_all(1, "user1", "Karl", 3, 2, 1, "", True)
    insert_user_all(2, "user2", "Frank", 3, 2, 1, "", False)
    insert_user_all(3, "user3", "Jamey", 3, 2, 1, "", False)
    insert_user_all(4, "user4", "Dorthy", 3, 2, 1, "", True)
    insert_user_all(5, "user5", "Morty", 3, 2, 1, "", True)
    insert_post_all(1, 1, "link1", 1, "blablabla", 3, 1)
    insert_post_all(2, 1, "link2", 1, "blablabla", 3, 1)
    insert_post_all(3, 1, "link3", 1, "blablabla", 3, 1)
    insert_post_all(4, 2, "link4", 1, "blablabla", 3, 1)
    insert_post_all(5, 3, "link5", 1, "blablabla", 3, 1)
    insert_post_all(6, 4, "link6", 1, "blablabla", 3, 1)
    insert_post_all(7, 4, "link7", 1, "blablabla", 3, 1)
    insert_follow(1, 2)
    insert_follow(1, 4)
    insert_follow(2, 1)
    insert_follow(3, 1)
    insert_follow(4, 1)
    insert_follow(5, 4)
    insert_like(1, 2)
    insert_like(1, 4)
    insert_like(1, 6)
    insert_like(2, 2)
    insert_like(2, 7)
    insert_like(3, 1)
    insert_like(3, 6)
    insert_like(3, 4)
    insert_like(4, 1)
    insert_like(4, 2)
    insert_like(4, 3)
    insert_like(5, 1)
    insert_like(5, 6)
    insert_like(5, 7)


# ---------------------------------GET-------------------------------------------------


def get_db_value(value, table, search_id):
    curs.execute("SELECT {} FROM {} WHERE {}ID={}".format(value, table, table, search_id))
    # curs.execute("SELECT login FROM User WHERE UserID=1;")
    result = None

    for (res,) in curs:
        result = res

    if result is not None:
        return result


def get_db_user_id_from_login(login):
    curs.execute("SELECT UserID FROM user WHERE login='{}'".format(login))
    # curs.execute("SELECT login FROM User WHERE UserID=1;")
    result = None

    for (res,) in curs:
        result = res

    if result is not None:
        return result


def get_db_user_login_from_id(user_id):
    curs.execute("SELECT login FROM user WHERE UserID='{}'".format(user_id))
    # curs.execute("SELECT login FROM User WHERE UserID=1;")
    result = None

    for (res,) in curs:
        result = res

    if result is not None:
        return result


def get_followers(ID):
    curs.execute("SELECT follower FROM Follow WHERE followed={}".format(ID))
    res = []
    for (fol,) in curs:
        res.append(fol)
    return res


def get_followings(ID):
    curs.execute("SELECT followed FROM Follow WHERE follower={}".format(ID))
    res = []
    for (fol,) in curs:
        res.append(fol)
    return res


def get_posts_ids(user):
    curs.execute("SELECT postID FROM post WHERE author={}".format(user))
    res = []
    for (post,) in curs:
        res.append(post)
    return res


def get_likes(post):
    curs.execute("SELECT user FROM LIKEs WHERE post={}".format(post))
    res = []
    for (like,) in curs:
        res.append(like)
    return res


def get_tagid(tag):
    curs.execute("SELECT HashTagID FROM hashtag WHERE tag='{}'".format(tag))
    for (tagid,) in curs:
        res = tagid
    return res


def get_most_followed(number):
    result = []
    curs.execute("select followed, count(followed) from follow group by followed order by count(followed) desc limit {};".format(number))
    for (user_id, n_followers, ) in curs:
        result.append({"User_id": user_id, "n_followers": n_followers})
    return result


#  -------------------------------------------Create Database-----------------------------------------------------

def create_tables():
    with open('CreateTables1.sql', 'r') as sql_file:
        sql_script = sql_file.read()
        curs.executescript(sql_script)
        db.commit()


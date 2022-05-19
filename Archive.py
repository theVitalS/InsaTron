import string

"""

load = instaloader.Instaloader()

    user = 'grogu.universe'
    password = '1a12S23#3'

    load.login(user, password)
    profile = 'highground.master'

    # Your preferred way of logging in:
    # L.load_session_from_file(USER)

    profile = instaloader.Profile.from_username(load.context, profile)

    n = 1
    print('Fetching likes of all posts of profile {}.'.format(profile.username))
    for post in profile.get_posts():
        curs.execute("INSERT INTO post VALUES ({}, 46652651789)".format(post.mediaid))
        print("INSERT INTO post VALUES ({}, 46652651789) -- EXECUTED".format(post.mediaid))
        likes = post.get_likes()
        for like in likes:
            curs.execute("INSERT INTO ilike VALUES ({},{},{})".format(n, post.mediaid, like.userid))
            print("INSERT INTO ilike VALUES ({},{},{}) -- EXECUTED".format(n, post.mediaid, like.userid))
            n = n + 1
        DataBse.commit()


-----------------------------



if if_user_in_table(46652651789):
    print("User in table")

load = instaloader.Instaloader()

user = 'grogu.universe'
password = '1a12S23#3'
load.login(user, password)
profile = instaloader.Profile.from_id(load.context, 46652651789)
followings = profile.get_followees()
# print(followings)
for following in followings:
    print(following)
    print(following.username)
    print('---------------------------')





==============================================second archive==================================================



#DataBse.drop_tables()
#DataBse.create_tables()
DataBse.insert_dummies()
print("==================================part1==========================================")
print("-------------Users:--------------------")
curs.execute("SELECT * FROM USER")
for sel in curs:
    print(sel)

print("-------------Posts:--------------------")
curs.execute("SELECT * FROM POST")
for sel in curs:
    print(sel)

print("-------------Likes:--------------------")
curs.execute("SELECT * FROM ILIKE")
for sel in curs:
    print(sel)

print("-------------Follows:--------------------")
curs.execute("SELECT * FROM FOLLOW")
for sel in curs:
    print(sel)

print("==================================part2==========================================")
DataBse.insert_user(2)
DataBse.insert_post(3)
DataBse.insert_like(3, 6)
DataBse.insert_follow(2, 9)

db = DataBse.connect()
curs = db.cursor()
print("-------------Users:--------------------")
curs.execute("SELECT * FROM USER")
for sel in curs:
    print(sel)

print("-------------Posts:--------------------")
curs.execute("SELECT * FROM POST")
for sel in curs:
    print(sel)

print("-------------Likes:--------------------")
curs.execute("SELECT * FROM ILIKE")
for sel in curs:
    print(sel)

print("-------------Follows:--------------------")
curs.execute("SELECT * FROM FOLLOW")
for sel in curs:
    print(sel)

print("==================================part3==========================================")
if not if_follow_in_table(6, 9):
    print("not in table")


curs.execute("SELECT * FROM POST")
for sel in curs:
    print(sel)

"""
# ----------------------------old user insert-------------------------------------------
"""self.login = ""
        self.name = ""
        self.nPosts = ""
        self.nFollowers = ""
        self.nFollowing = ""
        self.webLink = ""
        self.activeStory = ""
        self.scanTime = ""
        self.posts = []
        self.followers = get_followers(ID)
        self.following = [] 

        print("user with id {} successfully created".format(ID))
        if if_user_info_in_table(ID):
            self.login = get_db_value("login", "user", ID)
            self.name = get_db_value("name", "user", ID)
            self.nPosts = get_db_value("posts", "user", ID)
            self.nFollowers = get_db_value("followers", "user", ID)
            self.nFollowing = get_db_value("following", "user", ID)
            self.webLink = get_db_value("webLink", "user", ID)
            self.activeStory = get_db_value("activeStory", "user", ID)
            self.scanTime = get_db_value("scanTime", "user", ID)
        else:
            insert_user_id(ID)
            
            
            
            
            
                    if if_post_info_in_table(ID):
            self.link = get_db_value("link", "post", ID)
            self.type = get_db_value("type", "post", ID)
            self.text = get_db_value("text", "post", ID)
            self.likes = get_db_value("likes", "post", ID)
            self.comments = get_db_value("comments", "post", ID)
        else:
            insert_post_basics(ID)
            self.link = ""
            self.type = ""
            self.text = ""
            self.likes = ""
            self.comments = ""


"""


def printer_error(s):
    sum = 0
    for l in list(string.ascii_lowercase[14:]):
        sum += s.count(l)
    return str(sum)+"/"+str(len(s))

s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"

print(printer_error(s))

print(string.ascii_lowercase[14:])

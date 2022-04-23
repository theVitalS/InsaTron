import mysql.connector
from instaloader import TooManyRequestsException
# , TooManyRequestsExceptionMy

from InstaFuncs import *
from DataBase import *
import instaloader
from User import *
from Post import *
from App import *
from Bot import *
from ComplexFunctions import *


bot = Bot()

profile = instaloader.Profile.from_username(bot.context, "morning_millionaire")

id = profile.userid

print(id)

multiscanner(bot, id)

"""for liker in ids:
    if len(get_followings(liker)) == 0 and liker not in (8100443383, 12127126705, 5669252055):
        print("{} ------ Attempting to scan {}".format(datetime.now(), liker))

        try:
            profile = instaloader.Profile.from_id(bot.context, liker)
            multiscanner(bot, profile, to_scan_user_info=True, to_scan_followings=True)
        except TooManyRequestsExceptionMy as error:
            print("we caught an ERROR !!!!!!!!!")
            bot.change_bot()

        pause(30, 90)
        n += 1
        if n == 20:
            n = 0
            pause(60, 150)
            bot.change_bot()
        print("{} -- user {} successfully scanned".format(datetime.now(), get_db_user_login_from_id(liker)))
        print("__________________________________________________________")"""


"""u = user_from_login("highground.master")
#u = user_from_login("__dariarty__")

#amounts = count_likers(u)

ids = ""
likers = get_top_likers(u, 19, "min_likes")

for liker in likers:
    ids += str(liker)+", "
print(ids)"""


"""pages = get_most_followed(100)
for page in pages:

    if not if_user_info_in_table(page["User_id"]) and page["n_followers"] > 5:
        print("User {} has {} followings in database".format(page["User_id"], page["n_followers"]))

        try:
            profile = instaloader.Profile.from_id(bot.context, page["User_id"])
            scan_user(profile)
        except TooManyRequestsExceptionMy:
            pause(60, 120)
            bot.change_bot()

        pause(5, 30)
        print("_________________________________________________________________________")"""




"""for liker in likers:

    if len(get_followings(liker)) == 0 and liker not in (226598855, 45609209488, 3686873188, 7268304952, 25302154731, 1573854340):
        print("---------------------------{}--------------------------------".format(datetime.now()))
        print("User {} (id:{}) gave {} likes".format(get_db_user_login_from_id(liker), liker, likers[liker]))

        profile = instaloader.Profile.from_id(bot.context, liker)
        # print("Profile: {} -- Context: {}".format(profile, bot.context))

        followings = profile.get_followees()
        follower_id = profile.userid
        number_of_requests = scan_followings(profile)

        number_of_requests_before_switch += number_of_requests
        number_of_requests_total += number_of_requests

        if number_of_requests_before_switch > 2000:
            bot.change_bot()
            waiting_time = 90 + random.random() * 210
            print("{} BIG PAUSE for {} seconds".format(datetime.now(), waiting_time))
            time.sleep(waiting_time)
            number_of_requests_before_switch = 0

        n += 1
        time.sleep(3 + random.random()*7)

        print("---------- {} users scanned; {} requests made--------------------".format(n, number_of_requests_total))"""

import instaloader
import random
import time
from datetime import datetime

#logins = ['grogu.universe', 'easy_fittt', 'money.making.101', '__the.place.to.be__', 'fittestpoint']
# passwords = {'grogu.universe': '1a12S23#3', 'easy_fittt': '1a12s2EfVD', 'money.making.101': 'Mm.1710.$$$', '__the.place.to.be__': '1a12S23#3', 'fittestpoint': '1a12S23#3'}

""""""
extra_pause = 1
pause_factor = 1.1

accounts = [

    {'login': 'easy_fittt',
     'password': '1a12s2EfVD'},

    {'login': 'money.making.101',
     'password': 'Mm.1710.$$$'},

    {'login': 'fittestpoint',
     'password': '1a12S23#3'},

    {'login': '__the.place.to.be__',
     'password': '1a12S23#3'},

    {'login': 'grogu.universe',
     'password': '1a12S23#3'},

]

# loader = instaloader.Instaloader()


class Bot:
    def __init__(self, ind=0):
        self.index = ind
        self.login = accounts[self.index]['login']        # logins[self.index]
        self.password = accounts[self.index]['password']  # passwords[self.login]
        self.loader = instaloader.Instaloader()
        self.loader.login(self.login, self.password)
        self.context = self.loader.context

        print("{} ========= Logged as {} successfully =============".format(datetime.now(), self.login))

    def change_bot(self):

        pause(30, 60)
        self.loader.close()
        print("{} ===== session of {} closed =====".format(datetime.now(), self.login))

        if self.index + 1 < len(accounts):
            self.index += 1
        else:
            self.index = 0
            pause(900, 1800, True, "All bots used, break")

        pause(120, 180)

        self.login = accounts[self.index]['login']        # logins[self.index]
        self.password = accounts[self.index]['password']  # passwords[self.login]
        self.loader = instaloader.Instaloader()
        self.loader.login(self.login, self.password)
        self.context = self.loader.context
        print("{} ========= switched to {} =============".format(datetime.now(), self.login))

        pause(30, 60)


def pause(min_pause, max_puase, notification=True, extratext = ""):
    waiting_time = (min_pause + random.random() * (max_puase-min_pause))*pause_factor+extra_pause
    if notification:
        print("{} -- {} pause for {} seconds".format(datetime.now(), extratext, waiting_time))
    time.sleep(waiting_time)


"""

def insta_login():
    bot = instaloader.Instaloader()

    user = 'grogu.universe' #'easy_fittt'#'money.making.101'  #'grogu.universe'
    password = '1a12S23#3' #'1a12s2EfVD' #'Mm.1710.$$$'  #'1a12S23#3'

    bot.login(user, password)
    return bot



def show_bot_info(xbot):
    print("Bot {} login: {}".format(xbot.bots_number, xbot.login))


iter_bot_n = 0
for login in logins_passwords:
    iter_bot = Bot(login, logins_passwords[login])
    iter_bot.bots_number = iter_bot_n
    bots.append(iter_bot)
    iter_bot_n += 1


def switch_bot(old_bot):
    waiting_time = random.random() * 12
    print("pausing for {} seconds".format(waiting_time))
    time.sleep(waiting_time)

    # print("old number: {}; length: {}".format(old_bot.bots_number, len(bots)))
    if old_bot.bots_number + 1 < len(bots):
        new_bots_number = old_bot.bots_number + 1
    else:
        new_bots_number = 0

    # print("new bots number: {}".format(new_bots_number))

    new_bot = bots[new_bots_number]

    if not new_bot.logged:
        new_bot.log_to_instagram()
        print("logging {}".format(new_bot.login))

    bots[new_bots_number] = new_bot
    print("BOT SWITCHED to {}".format(new_bot.login))

    waiting_time = random.random() * 12
    print("pausing for {} seconds".format(waiting_time))
    time.sleep(waiting_time)

    return new_bot


bot = bots[0]
bot.log_to_instagram()

profile = instaloader.Profile.from_id(bot.context, 1450823362)
print(profile)

for i in range(1, 10):
    print_bot_info(bot)
    print("itteration {}".format(i))
    bot = switch_bot(bot)
    print("-----------------------------------")
"""






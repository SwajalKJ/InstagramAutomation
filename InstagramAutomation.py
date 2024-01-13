from instabot import Bot
bot = Bot()
bot.login(username = "_____", password = "______")
bot.follow('______') #any ID you want to follow
bot.unfollow('______')
bot.load_photo("_________", caption = "_______") #add photo path and caption
bot.send_message("_______", ["__ID___"]) #send message in chat
followers = bot.get_user_followers("__username__") #followers info in loop
for follower in followers:
    print(bot.get_user_info(follower))
followings = bot.get_user_following("__username__") #followings info in loop
for following in followings:
    print(bot.get_user_info(following))
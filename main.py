import asyncio
from time import time
import discord
from discord.ext import tasks
import datetime as dt

from config import *

def main_function():
    #Set up variables
    user_id = your_discord_user_id
    when_to_send_notifications = time_when_to_send_notifications

    token = your_bot_token
    client = discord.Client()

    # Function for geting how much seconds to wait until the end of next hour
    # eg. it is 10:40:20 (hours, minutes, seconds) the function will calculate how many seconds until 11:00:00
    # This is done so when the bot sends the message it will be exactly at hour:00:00 and not at some random time
    # when I run the script

    def how_long_sleeping():
        how_long_waiting_in_sec = 0

        if dt.datetime.now().second > 0:
            how_long_waiting_in_sec = how_long_waiting_in_sec + (60 - dt.datetime.now().second)
        
        if dt.datetime.now().minute > 0:
            how_long_waiting_in_sec = how_long_waiting_in_sec + ((60 - (dt.datetime.now().minute + 1)) * 60)
        
        return how_long_waiting_in_sec
    
    # Loops trough given list and finds all the people that have b-day or name-day
    def get_current_birthday(list_to_loop_trough):
        global b_days_today, b_days_tomorrow, name_days_today, name_days_tomorrow
        b_days_today = []
        b_days_tomorrow = []
        name_days_today = []
        name_days_tomorrow = []

        for human in list_to_loop_trough:
            if human.birthday_date.day == dt.datetime.now().day and human.birthday_date.month == dt.datetime.now().month:
                b_days_today.append(human)
            
            if human.birthday_date.day == (dt.datetime.now() + dt.timedelta(1)).day and human.birthday_date.month == (dt.datetime.now() + dt.timedelta(1)).month:
                b_days_tomorrow.append(human)

            if human.nameday_date.day == dt.datetime.now().day and human.nameday_date.month == dt.datetime.now().month:
                name_days_today.append(human)

            if human.nameday_date.day == (dt.datetime.now() + dt.timedelta(1)).day and human.nameday_date.month == (dt.datetime.now() + dt.timedelta(1)).month :
                name_days_tomorrow.append(human)

    @tasks.loop(hours = 1)
    async def main_loop():

        if dt.datetime.now().hour == when_to_send_notifications:
            get_current_birthday(user_dm)
            user = await client.fetch_user(user_id)

            for human in b_days_today:
                await user.send(f"{human.name} is celebrating birthday today :partying_face:")
            
            for human in b_days_tomorrow:
                await user.send(f"{human.name} has birthday tomorrow :partying_face:")

            for human in name_days_today:
                await user.send(f"Dnes má {human.name} is celebrating nameday today :partying_face:")

            for human in name_days_tomorrow:
                await user.send(f"{human.name} has nameday tomorrow :partying_face:")

    @main_loop.before_loop
    async def before_main_loop():
        await asyncio.sleep(how_long_sleeping())

    @client.event
    async def on_ready():
        main_loop.start()
        print("Happy Birthday Bot is online")
        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "out for next birthday"))

    client.run(token)
    
main_function()

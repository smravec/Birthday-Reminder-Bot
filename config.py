import datetime as dt
from default_class import *


#START OF CONFIG - DONT EDIT ANYTHING OUTSIDE CONFIG

# Config vars

your_discord_user_id = 0 #input your discord user id here as int

your_bot_token = "" #input your bot token here as string

time_when_to_send_notifications = 10 #input here the time when you want your notifications to be sent from 0 to 23 as int


# To add new dates into your birthday reminder just copy the template below with coresponding values, new instances of Human class will be added to reminder automatically

# Template1
Template1 = Human("Name", dt.date(2001, 2, 3), dt.date(2001, 4, 5))

# Example how to edit the template
# First date is birthday , the second is nameday (for the year in nameday put the same date as in birthday)
# Dates are Year , Month, Day
Simon = Human("Simon", dt.date(2005, 9, 2), dt.date(2005, 10, 11))

#After understanding how adding new dates work you can delete example and template above

#END OF CONFIG - DONT EDIT ANYTHING OUTSIDE CONFIG

user_dm = Human.all_instances


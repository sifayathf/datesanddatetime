# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

timezones ={1:'Africa/Tunis',
            2:'America/Argentina/Cordoba',
            3:'America/Detroit',
            4:'America/New_York',
            5:'Asia/Kuwait',
            6:'Asia/Tokyo'
}

reqtimezone = int(input())
print(reqtimezone,timezones[reqtimezone])
world_time = datetime.datetime.now(tz=pytz.timezone(timezones[reqtimezone]))
utc_time =  datetime.datetime.utcnow()

print("The time in  {} is {} {} ".format(timezones[reqtimezone],world_time.strftime('%A %x %X %z'),world_time.tzname()))
print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
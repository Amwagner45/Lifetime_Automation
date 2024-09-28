import datetime


# def get_next_sunday():
#     today = datetime.date.today()
#     sunday = today + datetime.timedelta(days=(6 - today.weekday()) % 7)
#     return sunday


# next_sunday = get_next_sunday()
# print(next_sunday)


weekday_dict = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
}

today = datetime.date.today()
next_weekday = today + datetime.timedelta(
    days=(6 - today.weekday() + weekday_dict["Tuesday"]) % 7
)

print(next_weekday.year)

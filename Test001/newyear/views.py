from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    new_year = datetime.datetime(year=now.year + 1, month=1, day=1)
    countdown = new_year - now

    is_new_year = now.month == 1 and now.day == 1

    return render(request, "newyear/index.html", {
        "newyear": is_new_year,
        "new_year_datetime": new_year.strftime('%Y-%m-%d %H:%M:%S')
    })

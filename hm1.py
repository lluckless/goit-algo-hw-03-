import datetime as dt
from datetime import datetime as dtdt

def get_days_from_today(date_setup="YYYY-MM-DD"):
    date_setup = input("Введіть дату у форматі YYYY-MM-DD: ")
    try:
        datetime_object = dtdt.strptime(date_setup, "%Y-%m-%d").date()
        current_date = dtdt.today().date()
        diff_date = current_date.toordinal() - datetime_object.toordinal()
        print(diff_date)
           
    except Exception:
        print("Не вірний формат дати!")
        quit()
    return diff_date

get_days_from_today()
    
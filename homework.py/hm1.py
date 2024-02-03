import datetime as dt
from datetime import datetime as dtdt

def get_days_from_today(date):
    try:
        datetime_object = dtdt.strptime(date, "%d-%m-%Y").date() # Об'явлення необхідної дати(без часу) та обробка її формату
        current_date = dtdt.today().date()                                        # Об'явлення сьогоднішньої дати(без часу)
        diff_date = current_date.toordinal() - datetime_object.toordinal()
        print(diff_date)
           
    except Exception:
        print("Не вірний формат дати!")
        quit()
    
    return diff_date

get_days_from_today()
    

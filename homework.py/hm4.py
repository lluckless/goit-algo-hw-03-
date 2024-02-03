import datetime as dt
from datetime import datetime as dtdt

colleagues = [{"name": "John Gold", "birthday": "1980.07.12"},
              {"name": "James Jame", "birthday": "2002.02.02"},
              {"name": "Dig Digon", "birthday": "1971.01.11"},
              {"name": "Diks Dikson", "birthday": "1981.01.29"},              
              {"name": "Big Bigon", "birthday": "1991.01.30"},
              {"name": "Biks Bikson", "birthday": "1961.01.31"},
              {"name": "Gig Gigon", "birthday": "1951.02.01"}
              ]

def get_upcoming_birthdays(colleagues=None):
    today_date = dtdt.today().date()
    birthdays = []
    for ppl in colleagues:
        birth_date = ppl["birthday"]                                 # отримуємо дату народження людини у вигляді рядка
        birth_date = str(today_date.year) + birth_date[4:]           # Замінюємо рік на поточний
        
        birth_date = dtdt.strptime(birth_date, "%Y.%m.%d").date()    # перетворюємо дату народження в об’єкт date
        week_day = birth_date.isoweekday()
        diff_days = (birth_date-today_date).days                     # рахуємо різницю між днем народження і днем сьогодні цьогоріч у днях
                
        if 0 <= diff_days < 7:
            if week_day < 6:                                         # перевірка для пн-пт і запис у список
                birthdays.append({'name':ppl['name'], 'birthday':birth_date.strftime("%Y.%m.%d")})
                print(f"Список привітань на цьому тижні --> {ppl['name']} : {birth_date}")
            else:
                if (birth_date + dt.timedelta(days=1)).weekday()==0: # перевірка для неділі, перенос на понеділок і запис у список
                    birthdays.append({'name':ppl['name'], 'birthday':(birth_date+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                else:                                                # перевірка для суботи, перенос на понеділок і запис у список
                    birthdays.append({'name':ppl['name'], 'birthday':(birth_date+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    return birthdays

get_upcoming_birthdays(colleagues)



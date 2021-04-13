from datetime import datetime, date, timedelta

class RestDays:

    def __init__(self, username, day, date):
        self.username = username
        self.day = day
        self.date = date


    def run(self):
        if self.day == '1':
            self.actual_date = date.today()
        elif self.day == '2':
            self.actual_date = date.today() + timedelta(days=1)
        elif self.day == '3':
            self.actual_date = date.today() - timedelta(days=1)
        elif self.day == '4':
            self.actual_date = date.today() - timedelta(days=2)
        else:
            raise Exception("Lo sentimos, ingrese un número correcto del 1 al 3")


    def get_free_days(self):
        print(self.other_date, self.actual_date)
        result = self.other_date - self.actual_date

        days = list(range(result.days))

        days_busy = 0
        days_free = 0

        for day in days:
            if days_busy == 2:
                days_busy = 0
                days_free += 1
                continue

            if days_free == 2:
                days_free = 0
                days_busy += 1
                continue

            if days_busy == 0 or days_busy == 1:
                if days_free == 1:
                    days_free += 1
                else:
                    days_busy += 1

        if days_busy:
            return False

        return True


    def get_other_date(self):
        new_date = self.date.split('-')
        actual_year = int(new_date[0])
        actual_month = int(new_date[1])
        actual_day = int(new_date[2])

        self.other_date = date(actual_year, actual_month, actual_day)

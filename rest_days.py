from datetime import datetime, date, timedelta


class RestDays:

    def __init__(self, username, day, date):
        self.username = username
        self.day = day
        self.date = date


    def get_actual_date(self):
        """ Esta función obtiene la fecha actual o en su defecto la fecha desde que comienza o término el Descanso
        del usuario, crea una variable de instancia llamada self.actual_date"""
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
        """
        Función encargada de iterar de acuerdo a los dias que existen entre la fecha actual y la que nuestro Usuario
        esta consultado, ej 10 días, de esta manera el programa separa de 2 en 2, ya que 2 días trabaja y descansa 2,
        suponiendo que manañana y pasado mañana trabaja entonces, los 2 primeros dias de la lista seran de trabajo.
        """
        result = self.user_date - self.actual_date # ejemplo: 10 días

        days = list(range(result.days)) # lista del 1 al 10

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
        """ Esta función se encarga de crear una fecha, la cual es la que queremos saber si nuestro usuario descansa"""
        new_date = self.date.split('-')

        try:
            actual_year = int(new_date[0])
            actual_month = int(new_date[1])
            actual_day = int(new_date[2])
            self.user_date = date(actual_year, actual_month, actual_day)

            if self.user_date < self.actual_date:
                raise Exception

        except (ValueError, IndexError, Exception):
            return False

        return True

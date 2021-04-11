from datetime import datetime, date, timedelta


def run(answer):
    if answer == 1:
        actual_day = date.today()

        return actual_day
    elif answer == 2:
        tomorrow = date.today() + timedelta(days=1)

        return tomorrow
    elif answer == 3:
        print("Ingresa el dia en que termina tu proximo descanso")
        actual_year = int(input("Ingresa el año: "))
        actual_month = int(input("Ingresa el mes: "))
        actual_day = int(input("Ingresa el día: "))

        actual_date = date(actual_year, actual_month, actual_day)

        return actual_date
    else:
        raise Exception("Lo sentimos, ingrese un número correcto del 1 al 3")


def get_free_days(actual_date, other_date):
    result = other_date - actual_date
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


def get_other_date():
    actual_year = int(input("Ingresa el año: "))
    actual_month = int(input("Ingresa el mes: "))
    actual_day = int(input("Ingresa el día: "))

    actual_date = date(actual_year, actual_month, actual_day)

    return actual_date


if __name__ == '__main__':
    answer = int(
        input(
        """
        Cuando terminas tu descanso?
        1. Hoy
        2. Manañana
        3. Estoy trabajando
        """
        )
    )

    actual_date = run(answer)

    print("Ingresa la fecha que quieras saber si es tu descanso")
    other_date = get_other_date()

    result = get_free_days(actual_date, other_date)

    if result:
        print(f"El {other_date}, descansas")
    else:
        print(f"El {other_date}, NO descansas")

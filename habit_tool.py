from datetime import datetime


def break_habit(habit_name, start_date, cost_per_day, minutes_wasted):
    goal = 60
    hourly_wage = 50  # euros

    time_elapsed = (datetime.now() - start_date).total_seconds()
    hours = round(time_elapsed / 60 / 60, 1)
    days = round(hours / 24, 2)

    money_saved = cost_per_day * days
    minutes_saved = round(days * minutes_wasted)
    total_money_saved = f'€{round(money_saved + (minutes_saved / 60 * hourly_wage), 2)}'

    days_to_go = round(goal - days)
    if hours > 72:
        hours = str(days) + ' days'
    else:
        hours = str(hours) + ' hours'
    return {'habit': habit_name, 'time_since':hours, 'days_remaining': days_to_go, 'minutes_saved':minutes_saved, 'money_saved':total_money_saved}


print(break_habit('Coffee', datetime(2023, 1, 1, 10, 30), cost_per_day=2, minutes_wasted=15))

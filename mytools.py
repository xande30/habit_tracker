from datetime import datetime
from habit_tool import break_habit
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Back


habits = [break_habit('Coffee', datetime(2023, 1, 1, 10, 30), cost_per_day=2, minutes_wasted=15),
          break_habit('Beer', datetime(2023, 1, 1, 10, 30), cost_per_day=2, minutes_wasted=30),
          break_habit('Sugar', datetime(2023, 1, 1, 10, 30), cost_per_day=1, minutes_wasted=5),
          break_habit('Junk Food', datetime(2023, 1, 1, 10, 30), cost_per_day=10, minutes_wasted=60),
          break_habit('Social Media', datetime(2023, 1, 1, 10, 30), cost_per_day=10, minutes_wasted=120),
          break_habit('Netflix', datetime(2023, 1, 1, 10, 30), cost_per_day=0, minutes_wasted=120)
          ]

df = pd.DataFrame(habits)
print(Fore.LIGHTRED_EX + Back.BLACK,(tabulate(df, headers='keys', tablefmt='psql')))
print(Fore.LIGHTGREEN_EX, '----HAPPY LIFE IS WAITING FOR YOU----')
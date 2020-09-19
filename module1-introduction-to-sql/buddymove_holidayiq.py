
import pandas as pd

df = pd.read_csv("buddymove_holidayiq.csv")

df.to_sql(buddymove_holidayiq.sqlite3)
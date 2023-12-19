import pandas as pd

file_name = "NIS_2019_Core"
data = pd.io.stata.read_stata(file_name + ".dta")
data.to_csv(file_name + ".csv")
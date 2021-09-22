import pandas as pd

def jsontocsv(file):
    df = pd.read_json(file)
    df.to_csv("finalCSV.csv", index=None)
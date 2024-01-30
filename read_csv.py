import polars as pl


df = pl.read_csv("assets/csv_exemplo.csv", separator=";")
print(df)

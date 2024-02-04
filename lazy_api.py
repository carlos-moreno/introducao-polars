import polars as pl

q1 = pl.scan_csv("assets/csv_exemplo.csv", separator=";").collect(streaming=True)

df = pl.read_csv("assets/csv_exemplo.csv", separator=";")

print(df)

print(df.head())

print(df.tail())

print(q1)

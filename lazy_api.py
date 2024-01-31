import polars as pl

q1 = pl.scan_csv("assets/csv_exemplo.csv", separator=";").collect(streaming=True)

print(q1)

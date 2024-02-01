import polars as pl


df = pl.read_csv("assets/csv_exemplo.csv", separator=";")

print(f"Colunas do Dataframe => {df.columns}")

print(df.head())

print(df.tail(3))

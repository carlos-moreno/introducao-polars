import polars as pl


df = pl.read_csv("assets/csv_exemplo.csv", separator=";")

print(f"Colunas do Dataframe => {df.columns}")

print(df.head(4))

print(df.tail(2))

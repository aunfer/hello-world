import pandas as pd

"ITEM 1"
df=pd.read_excel("best-selling game consoles.xlsx",sheet_name="consoles")

"ITEM 3 (inverti a ordem pois no terminal o comando replace omite as outras colunas)"
df_filtrado=df.where(df["Released Year"]>2010)

"ITEM 2"
df_nome=df_filtrado["Console Name"].str.replace("NES","Nintendinho")
df_upper=df_filtrado["Console Name"].str.upper()
print(df_upper.dropna()) 

"ITEM 4"
print(df.describe())
print(df.info())
df_missing=df[df["Remarks"].isnull()]
df_missing["Remarks"]="missing"
print(df_missing)

"ITEM 5"
df["Delta"]=df["Discontinuation Year"]-df["Released Year"]
df_filtro=df[(df["Discontinuation Year"]>0)&(df["Delta"]<=2)&(df["Delta"]>0)]
print(df_filtro)
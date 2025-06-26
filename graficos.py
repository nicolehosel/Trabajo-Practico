import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from collections import Counter


#Cargar base de datos
conn = sqlite3.connect("base_datos.db")  # Subí este archivo a Colab
df = pd.read_sql_query("SELECT * FROM boliches", conn)
conn.close()


#Mostrar las primeras filas
print(df.head())


#Configuración global de gráficos
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.grid"] = True


# 1. Cantidad de boliches por perfil
perfil_counts = df['perfil'].value_counts()
perfil_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Cantidad de boliches por perfil")
plt.xlabel("Perfil")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#2. Cantidad de boliches según edad mínima
edad_counts = df['edad_minima'].value_counts().sort_index()
edad_counts.plot(kind='bar', color='salmon', edgecolor='black')
plt.title("Cantidad de boliches por edad mínima")
plt.xlabel("Edad mínima")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()


#3. Géneros musicales más frecuentes
musicas = df['musica'].str.lower().str.split(", ")
generos = [item.strip() for sublist in musicas for item in sublist]
conteo_generos = Counter(generos)
generos_df = pd.DataFrame(conteo_generos.items(), columns=["Género", "Cantidad"]).sort_values("Cantidad", ascending=False)


generos_df.set_index("Género").plot(kind="barh", legend=False, color='mediumseagreen', edgecolor='black')
plt.title("Géneros musicales más frecuentes")
plt.xlabel("Cantidad de apariciones")
plt.ylabel("Género musical")
plt.tight_layout()
plt.show()


#4. Días de apertura más comunes
dias = df['dias'].str.lower()
dias = dias.str.replace("sábados", "sábado").str.replace("viernes", "viernes")  # uniformar
dias_separados = dias.str.split(", ")
todos_dias = [dia.strip() for sublist in dias_separados for dia in sublist]
conteo_dias = Counter(todos_dias)
dias_df = pd.DataFrame(conteo_dias.items(), columns=["Día", "Cantidad"]).sort_values("Cantidad", ascending=False)


dias_df.set_index("Día").plot(kind="bar", legend=False, color='plum', edgecolor='black')
plt.title("Días de apertura más comunes")
plt.xlabel("Día")
plt.ylabel("Cantidad de boliches que abren ese día")
plt.tight_layout()
plt.show()

import seaborn as sns
print(sns.__version__)

"""# Analisando as notas em geral"""

import pandas as pd

notas = pd.read_csv("ratings.csv")
notas.head()

notas.shape

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.head()

notas['nota'].unique()

notas['nota'].value_counts()

print("Media",notas['nota'].mean())
print("Mediana",notas['nota'].median())

notas.nota.head()

notas.nota.plot(kind='hist')

notas.nota.describe()

import seaborn as sns

sns.boxplot(notas.nota)

"""# Olhando os filmes"""

filmes = pd.read_csv("movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]
filmes.head()

notas.head()

"""# Analisando algumas notas especificas por filme"""

notas.query("filmeId==1").nota.mean()

notas.query("filmeId==2").nota.mean()

medias_por_filme = notas.groupby("filmeId").mean().nota
medias_por_filme.head()

medias_por_filme.plot(kind='hist')

import matplotlib.pyplot as plt

plt.figure(figsize=(5,8))
sns.boxplot(y=medias_por_filme)

medias_por_filme.describe()

sns.distplot(medias_por_filme)

plt.hist(medias_por_filme)
plt.title("Histograma das médias dos filmes")

tmdb = pd.read_csv("tmdb_5000_movies.csv")
tmdb.head()

tmdb.original_language.unique() # categorica nominal

# primeiro grau
# segundo grau
# terceiro grau
# 1 grau < 2 grau < 3 grau # categorica ordinal

# budget => orcamento => quantitativa continuo

# quantidade de votos => 1, 2, 3, 4, nao tem 2.5 votos.
# notas do movielens => 0.5, 1, 1.5, ... ,5 nao tem 2.7

tmdb["original_language"].value_counts().index

tmdb["original_language"].value_counts().values

contagem_de_lingua = tmdb["original_language"].value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ["original_language", "total"]
contagem_de_lingua.head()

sns.barplot(x="original_language", y = "total", data = contagem_de_lingua)

sns.catplot(x = "original_language", kind="count", data = tmdb)

plt.pie(contagem_de_lingua["total"], labels = contagem_de_lingua["original_language"])

total_por_lingua = tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles, total_do_resto)

dados = {
    'lingua' : ['ingles','outros'],
    'total' : [total_de_ingles, total_do_resto]
}
dados = pd.DataFrame(dados)
sns.barplot(x="lingua", y="total", data = dados)

plt.pie(dados["total"], labels = dados["lingua"])

total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()
total_por_lingua_de_outros_filmes



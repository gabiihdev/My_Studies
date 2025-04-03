from AT_10 import consultar_dados_BD
df_movies, _ = consultar_dados_BD()

try:
    df_filmes_ordenados_por_rating = df_movies.sort_values(by="rating", ascending=False)
    df_filmes_rating_maior_9 = df_filmes_ordenados_por_rating[df_filmes_ordenados_por_rating["rating"] > 9.0]
    
    print('FILMES ORDENADOS PELO RATING\n')
    print(df_filmes_ordenados_por_rating.to_string(index=False))
    
    print("\nTOP 5 FILMES COM RATING ACIMA DE 9.0 NO IMBD\n")
    print(df_filmes_rating_maior_9.to_string(index=False))
    
except Exception as e:
    print(f">> ERRO: consulta ao BD - {e}")

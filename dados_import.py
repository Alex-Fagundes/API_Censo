import pandas as pd


def ler_arquivo(arquivo):
    arquivo = pd.read_csv(arquivo, sep=";", encoding="latin-1")
    return arquivo


def filtrar_dados(dataframe, lista_colunas):
    dataframe = dataframe.iloc[:, lista_colunas]
    dataframe.drop_duplicates(inplace=True)
    return dataframe


def concatenar_df(lista_df, titulo_coluna):
    for i, df in enumerate(lista_df):
        df["NOVA_COLUNA"] = f"df{i}"
        codigo = f"df{i+1}"
    df_concatenado = pd.concat(lista_df)
    df_final = df_concatenado.drop_duplicates(subset=titulo_coluna)
    linhas_repetidas = df_concatenado[
        df_concatenado.duplicated(keep=False, subset=titulo_coluna)
    ]
    df_final.loc[df_final.index.isin(linhas_repetidas.index), "NOVA_COLUNA"] = codigo
    return df_final


def padronizar_cabecalho(dataframe, dict_cabecalho):
    dataframe = dataframe.rename(columns=dict_cabecalho)
    return dataframe


def substituir_codigos(dataframe, titulo_coluna, dict_codigos):
    dataframe[titulo_coluna] = dataframe[titulo_coluna].replace(dict_codigos)
    return dataframe


arquivo_ed_basica = "microdados_ed_basica_2023.csv"
arquivo_tecnicos = "suplemento_cursos_tecnicos_2023.csv"

colunas_ed_basica_2023 = [0, 1, 3, 4, 6, 17, 18, 19]
colunas_tecnicos_2023 = [0, 1, 3, 4, 6, 10, 11, 12]

novo_cabecalho = {
    "NU_ANO_CENSO": "ano_censo",
    "NO_REGIAO": "regiao",
    "NO_UF": "uf",
    "SG_UF": "sigla_uf",
    "NO_MUNICIPIO": "municipio",
    "NO_ENTIDADE": "entidade",
    "CO_ENTIDADE": "codigo_entidade",
    "TP_DEPENDENCIA": "administracao",
    "NOVA_COLUNA": "nivel",
}
depen_adm = {
    1: "federal",
    2: "estadual",
    3: "municipal",
    4: "privada",
}
niveis_ensino = {
    "df0": "básico",
    "df1": "técnico",
    "df2": "básico e técnico",
}

ed_basica_2023 = ler_arquivo(arquivo_ed_basica)
tecnicos_2023 = ler_arquivo(arquivo_tecnicos)

ed_basica_2023 = filtrar_dados(ed_basica_2023, colunas_ed_basica_2023)
tecnicos_2023 = filtrar_dados(tecnicos_2023, colunas_tecnicos_2023)

dados_2023 = concatenar_df([ed_basica_2023, tecnicos_2023], "CO_ENTIDADE")

dados_2023 = padronizar_cabecalho(dados_2023, novo_cabecalho)

dados_2023 = substituir_codigos(dados_2023, "administracao", depen_adm)
dados_2023 = substituir_codigos(dados_2023, "nivel", niveis_ensino)

import pandas as pd


def ler_arquivo(arquivo):
    arquivo = pd.read_csv(arquivo, sep=";", encoding="latin-1")
    return arquivo


def filtrar_dados(dataframe, colunas):
    dataframe = dataframe.iloc[:, colunas]
    return dataframe


def concatenar_df(lista_df):
    df_concatenado = pd.concat(lista_df, ignore_index=True)
    return df_concatenado


def padronizar_cabecalho(dataframe, dict_cabecalho):
    dataframe = dataframe.rename(columns=dict_cabecalho)
    return dataframe


def substituir_codigos(dataframe, coluna, dict_codigos):
    dataframe[coluna] = dataframe[coluna].replace(dict_codigos)
    return dataframe


arquivo_ed_basica = "microdados_ed_basica_2023.csv"
arquivo_tecnicos = "suplemento_cursos_tecnicos_2023.csv"

colunas_ed_basica_2023 = [0, 1, 3, 4, 6, 17, 19]
colunas_tecnicos_2023 = [0, 1, 3, 4, 6, 10, 11]

novo_cabecalho = {
    "NU_ANO_CENSO": "ano_censo",
    "NO_REGIAO": "regiao",
    "NO_UF": "uf",
    "SG_UF": "sigla_uf",
    "NO_MUNICIPIO": "municipio",
    "NO_ENTIDADE": "entidade",
    "TP_DEPENDENCIA": "administracao",
}
depen_adm = {
    1: "federal",
    2: "estadual",
    3: "municipal",
    4: "privada",
}

ed_basica_2023 = ler_arquivo(arquivo_ed_basica)
tecnicos_2023 = ler_arquivo(arquivo_tecnicos)

ed_basica_2023 = filtrar_dados(ed_basica_2023, colunas_ed_basica_2023)
tecnicos_2023 = filtrar_dados(tecnicos_2023, colunas_tecnicos_2023)

dados_2023 = concatenar_df([ed_basica_2023, tecnicos_2023])

dados_2023 = padronizar_cabecalho(dados_2023, novo_cabecalho)

dados_2023 = substituir_codigos(dados_2023, "administracao", depen_adm)

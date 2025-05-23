#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
/fiap/cap14/app_predicao.py

Aplicativo simples para prever a cultura ideal com base em condições de solo e clima
'''

import joblib
import numpy as np
import argparse
import sys
from pathlib import Path

# Carregar modelo
MODEL_PATH = Path('fase3_cap14/src/datasets/output/modelos_preditivos/modelos/random_forest_best_model.pkl')
modelo = joblib.load(MODEL_PATH)

# Definir nomes das features e mapeamento de classes
feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
target_mapping = {0: 'apple', 1: 'banana', 2: 'blackgram', 3: 'chickpea', 4: 'coconut', 5: 'coffee', 6: 'cotton', 7: 'grapes', 8: 'jute', 9: 'kidneybeans', 10: 'lentil', 11: 'maize', 12: 'mango', 13: 'mothbeans', 14: 'mungbean', 15: 'muskmelon', 16: 'orange', 17: 'papaya', 18: 'pigeonpeas', 19: 'pomegranate', 20: 'rice', 21: 'watermelon'}

def prever_cultura(valores):
    '''
    Prevê a cultura ideal com base nos valores informados

    Parâmetros:
    valores (list): Lista com os valores na ordem: N, P, K, temperature, humidity, ph, rainfall

    Retorna:
    dict: Dicionário com a cultura prevista e confiança (se disponível)
    '''
    # Converter entrada para array numpy
    X = np.array(valores).reshape(1, -1)

    # Fazer previsão
    y_pred = modelo.predict(X)[0]
    cultura = target_mapping.get(y_pred, "Desconhecida")

    # Tentar obter probabilidades (se o modelo suportar)
    confianca = None
    try:
        if hasattr(modelo, 'predict_proba'):
            proba = modelo.predict_proba(X)
            confianca = float(np.max(proba))
    except:
        pass

    return {
        'cultura': cultura,
        'confianca': confianca
    }

def exemplo_interativo():
    '''
    Executa um exemplo interativo de previsão
    '''
    print("\n===== Sistema de Previsão de Cultura Ideal =====")
    print(f"Utilizando o modelo: {MODEL_PATH.name}")
    print("\nDigite os valores para as seguintes condições:")

    valores = []

    for feature in feature_names:
        while True:
            try:
                valor = float(input(f"{feature}: "))
                valores.append(valor)
                break
            except ValueError:
                print("Por favor, digite um valor numérico válido.")

    resultado = prever_cultura(valores)

    print("\n----- Resultado -----")
    print(f"Cultura ideal prevista: {resultado['cultura']}")

    if resultado['confianca']:
        print(f"Confiança da previsão: {resultado['confianca']:.2f}")

    print("\nObservação: Este é um modelo experimental e os resultados devem ser")
    print("validados por especialistas em agricultura antes de aplicação prática.")

def modo_nao_interativo(valores):
    '''
    Executa o modelo em modo não-interativo

    Parâmetros:
    valores (list): Lista com os valores na ordem: N, P, K, temperature, humidity, ph, rainfall
    '''
    if len(valores) != len(feature_names):
        print(f"Erro: Número incorreto de valores. Esperado {len(feature_names)} valores.")
        print(f"Ordem dos valores: {', '.join(feature_names)}")
        sys.exit(1)

    try:
        # Converter para float
        valores_float = [float(v) for v in valores]

        # Fazer previsão
        resultado = prever_cultura(valores_float)

        print("\n----- Resultado -----")
        print(f"Cultura ideal prevista: {resultado['cultura']}")

        if resultado['confianca']:
            print(f"Confiança da previsão: {resultado['confianca']:.2f}")

        return resultado
    except ValueError as e:
        print(f"Erro ao converter valores: {e}")
        sys.exit(1)

def usar_exemplo_real():
    '''
    Usa um exemplo real do conjunto de dados para demonstração
    '''
    # Carregar dataset original
    try:
        import pandas as pd
        DATA_DIR = Path('fase3_cap14/src/datasets/')
        DATASET_PATH = DATA_DIR / 'Atividade_Cap_14_produtos_agricolas.csv'
        df = pd.read_csv(DATASET_PATH)

        # Selecionar uma amostra aleatória
        amostra = df.sample(n=1, random_state=42)

        # Extrair valores das features
        valores = amostra.drop('label', axis=1).values[0].tolist()
        cultura_real = amostra['label'].values[0]

        # Fazer previsão
        resultado = prever_cultura(valores)

        print("\n===== Exemplo com Dados Reais =====")
        print("\nValores das características:")
        for i, feat in enumerate(feature_names):
            print(f"  {feat}: {valores[i]:.2f}")

        print("\n----- Resultado -----")
        print(f"Cultura real: {cultura_real}")
        print(f"Cultura prevista: {resultado['cultura']}")

        if resultado['confianca']:
            print(f"Confiança da previsão: {resultado['confianca']:.2f}")

        print(f"Previsão correta: {cultura_real == resultado['cultura']}")

        return resultado
    except Exception as e:
        print(f"Erro ao usar exemplo real: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Previsão de cultura agrícola ideal')
    parser.add_argument('--valores', nargs='+', help=f"Valores das características na ordem: {', '.join(feature_names)}")
    parser.add_argument('--exemplo-real', action='store_true', help='Usar um exemplo real do conjunto de dados')

    args = parser.parse_args()

    if args.exemplo_real:
        # Usar exemplo real do dataset
        usar_exemplo_real()
    elif args.valores:
        # Modo não-interativo com valores fornecidos
        modo_nao_interativo(args.valores)
    else:
        # Modo interativo
        exemplo_interativo()

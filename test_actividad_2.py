'''
Test unitarios para Actividad_1.py
'''
import Actividad_1
import pytest
import pandas as pd

def test_resultados_mes():
    mes= [10,10,-10,-10]
    resultado = (-20,20)
    assert resultado == Actividad_1.resultados_mes(mes)

def test_gasto_ahorro_max():
    df = {"Enero":[10,10],
    "Febrero":[1,-10],
    "Marzo":[1,-10],
    "Abril":[1,-10],
    "Mayo":[1,-10],
    "Junio":[1,-10],
    "Julio":[1,-10],
    "Agosto":[1,-10],
    "Septiembre":[1,-10],
    "Octubre":[1,-10],
    "Noviembre":[1,-10],
    "Diciembre":[1,-100]}
    df =pd.DataFrame(df, columns=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],dtype=int)
    # Gastos ingresos ahorros 
    resultado = ([0,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-100],
                 [20,1,1,1,1,1,1,1,1,1,1,1],
                 [20,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-99])
    print (Actividad_1.gasto_ahorro_max(df))
    assert resultado == Actividad_1.gasto_ahorro_max(df)
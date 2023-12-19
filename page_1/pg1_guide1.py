# External library
import streamlit as st
import pandas as pd
import shap
import warnings

# Internal library
from machine_learning_algorithm import model, dataframe
from utils import one_hot_for_prediction, st_shap

# Dictionaries relating variables' names with their corresponding numbers

results = {
    0: 'Disapproved',
    1: 'Approved',
}

actives = {
    'None': 0,
    'Sodium Alkyl Benzene Sulfonate': 1,
    'Benzalkonium Chloride': 2,
    'Dialkyloxyethyl Hydroxyethyl Methyl Ammonium Methyl Sulphate': 3,
    'Hydrogen Peroxide': 4,
    'Sodium hypochlorite': 5,
    'Ethoxylated Alcohol': 6,
    'Lactic acid': 7,
    'Alkyl Dimethyl Benzyl Ammonium Chloride': 8
}

tests = {
    'EN1276': 1,
    'ASTM2274': 2,
    'EN1040': 3,
    'Inhibition halo': 4,
    'OECD202': 5,
    'EN13697': 6,
    'EN14561': 7
}

# Columns names for plots

ind = ['Corrente Agitador 1601',
    'Corrente Agitador 1602',
    'Corrente Agitador 1603',
    'Corrente Agitador 1604',
    'Corrente Agitador 1605',
    'Corrente Bomba 1601',
    'Corrente Bomba 1602',
    'Corrente BB 1006',
    'Potência Agitador 1605',
    'Potência Bomba 1006',
    'Vazão Pasta',
    'Pressão CZ 1603',
    'Pressão CZ 1605',
    'Temperatura Final',
    'Temperatura Holding 1633',
    'Temperatura Holding 1634',
    'Temperatura 1 Corpo',
    'Temperatura 3 Corpo',
    'Temperatura Amostra',
    'Dosagem Açúcar',
    'Dosage Óleo',
    'Dosagem Água',
    'Dosagem Vinagre'
      ]

def run_guide1():

    # Data input

    try:

        if 'predict_pg1_guide1' not in st.session_state:
            st.session_state['predict_pg1_guide1'] = False
        
        with st.form("Inputs1"):

            var1, var2 = st.columns(2)

            x1 = var1.selectbox("Corrente Agitador:")
            x2 = var2.text_input("Corrente Bomba:")

            var3, var4 = st.columns(2)

            x3 = var3.text_input("Corrente BB:")
            x4 = var4.text_input("Potência Bomba:")

            var5, var6 = st.columns(2)

            x5 = var5.text_input("Potência Agitador:")
            x6 = var6.text_input("Vazão Pasta:")

            var7, var8 = st.columns(2)

            x7 = var7.text_input("Pressão CZ:")
            x8 = var8.text_input("Temperatura Final:", help = "Unit: ºC")

            var9, var10 = st.columns(2)

            x9 = var9.selectbox("Temperatura Holding",help = "Unit: ºC")
            x10 = var10.text_input("Temperatura Corpo", help = "Unit: ºC")

            var11, var12 = st.columns(2)

            x11 = var11.text_input("Temperatura Amostra", help = "Unit: ºC")
            x12 = var12.text_input("Dosagem Açúcar")

            var13, var14 = st.columns(2)

            x13 = var13.text_input("Dosagem Óleo")
            x14 = var14.text_input("Dosagem Vinagre")

            var15 = st.columns(1)

            x15 = var15.text_input("Vinagre")
            

            # Corresponding variables with their numbers


            
          

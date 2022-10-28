import streamlit as st

import requests
import pandas as pd

dfQP = pd.read_csv("csv/quatropatas/tbOrdServico.csv") 
dfQP["dataflowid"] = "QP2022"
print(dfQP.shape[0])
dfVC = pd.read_csv("csv/vitacare/tbOrdServico.csv")
dfVC["dataflowid"] = "VC2022"
print(dfVC.shape[0])


frames = [dfQP, dfVC]  
result = pd.concat(frames)
print(result.shape[0])
resultJson = result.to_json(orient='split', index=False)
st.json(resultJson)
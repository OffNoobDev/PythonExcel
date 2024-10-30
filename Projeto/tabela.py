from pathlib import Path
import streamlit as st
import pandas as pd

pasta_media = Path(__file__).parent.parent / 'Projeto'
caminho_media = pasta_media / 'media.xlsx'

df = pd.read_excel(caminho_media)

st.dataframe(df)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df3 = pd.read_csv("tabla3.csv")
print(df3.columns[0])
print(df3[df3["SDG "] == "Solariza África "])

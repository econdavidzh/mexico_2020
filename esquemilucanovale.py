# APP #milucanovale:
import streamlit as st
from PIL import Image
import pandas as pd
import requests
import bs4

# URL para extraer valor peso colombiano vs peso mexicano:
url_peso = "https://www.cambiodolar.mx/peso-mexicano-a-peso-colombiano"
response_peso = requests.get(url_peso)
# documento html del sitio web:
html_doc_peso = bs4.BeautifulSoup(response_peso.text, 'html.parser')
text = html_doc_peso.find_all("div")

# Extrayendo info de tasa de cambio para COP:
lines = []
for line in text:
  try:
    if line.string.startswith("1"):
      lines.append(line.string)
      break
  except:
    continue

# Calculando tasas de cambio MEX-COP:
try:
  pesos_colombianos_por_1_mexicano = float(lines[0].split("  ")[1].split(" ")[0])
except:
  lines[0] = lines[0].replace(",", ".")
  pesos_colombianos_por_1_mexicano = float(lines[0].split("  ")[1].split(" ")[0])
pesos_mexicanos_por_1_colombiano = 1 / pesos_colombianos_por_1_mexicano

# URL para extraer valor dolar vs peso mexicano:
url_dolar = "https://www.cambiodolar.mx/MXN_USD"
response_dolar = requests.get(url_dolar)
# documento html del sitio web:
html_doc_dolar = bs4.BeautifulSoup(response_dolar.text, 'html.parser')
text_dolar = html_doc_dolar.find_all("div")

# Extrayendo info de tasa de cambio para USD:
lines_dolar = []
for line in text_dolar:
  try:
    if line.string.startswith("1"):
      lines_dolar.append(line.string)
      break
  except:
    continue

# Calculando tasas de cambio MEX-USD:
try:
  pesos_mexicanos_por_1_dolar = float(lines_dolar[0].split("  ")[1].split(" ")[0])
except:
  lines_dolar[0] = lines_dolar[0].replace(",", ".")
  pesos_mexicanos_por_1_dolar = float(lines_dolar[0].split("  ")[1].split(" ")[0])
dolares_por_1_peso_mexicano = 1 / pesos_mexicanos_por_1_dolar

### --- Imágenes:
hola_pobres = Image.open("hola_pobres.png")
mexico = Image.open("mexico.png")
luca = Image.open("luca.png")
felicidad = Image.open("felicidad.png")
eliminado = Image.open("eliminado.png")
paila = Image.open("paila.png")

# Estructura de la APP:
st.set_page_config(page_title = "Mi Luca No Vale")
st.image(hola_pobres, use_column_width = False, width = 125)
st.title('Bienvenidos a #EsQueMiLucaNoVale Versión México 2022!!!')
st.image(mexico, use_column_width = True)

# Tasas de Cambio Actuales:
st.write(pd.DataFrame({
    "COP/MEX" : [pesos_colombianos_por_1_mexicano],
    "MEX/USD" : [pesos_mexicanos_por_1_dolar]
}).round(2), use_column_width = True)

# Cambiar de USD a MEX:
la_reluca = st.number_input('Cuánta luca (en dólares) quieres cambiar a pesos mexicanos?')
la_reluca = float(la_reluca)

if la_reluca != 0:
    st.write("Deberías recibir $", 
            round(la_reluca * pesos_mexicanos_por_1_dolar, 2), 
            "pesos mexicanos por tu luca gringa") 

if la_reluca != 0:
    st.image(felicidad, use_column_width = False, width = 200)

# Precio de MEX a COP:
precio_en_mex = st.number_input('Cuánto cuesta esto en mi luca?')
if precio_en_mex != 0:
    st.write("En luca colombiana esto vale $", 
            round(precio_en_mex * pesos_colombianos_por_1_mexicano, 2), 
            "pero no te sientas pobre!")
    st.write("Esto mismo en dolarucos te cuesta $",
            round(precio_en_mex / pesos_mexicanos_por_1_dolar, 2))

if precio_en_mex != 0:
    st.image(luca, use_column_width = False, width = 150)

# Dividir una cuenta:
cuenta_dividida = st.number_input('Quieres dividir una cuenta?')
if cuenta_dividida != 0:
    st.image(eliminado, use_column_width = False, width = 150)
    st.write("Cindy paga", 
            round(cuenta_dividida / 5, 2))
    st.write("Paula paga", 
            round(cuenta_dividida / 5, 2))
    st.write("Kiki paga",
            round((cuenta_dividida / 4), 2),
            "te tocó dar la propina asignada de forma aleatoria")
    st.image(paila, use_column_width = False, width = 150)
    st.write("Daniel paga",
            round(cuenta_dividida / 5, 2))
    st.write("David paga",
            round(cuenta_dividida / 5, 2))
    

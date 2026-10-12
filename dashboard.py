# dashboard.py
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


st.set_page_config(page_title="Giełda Dashboard", page_icon="📈", layout="wide")
st.title("📈 Mój Portfel Inwestycyjny GPW")
st.markdown("Witaj w panelu analitycznym! Poniżej znajdują się dane pobrane z Twojej bazy.")


@st.cache_data
def load_data():

    conn = sqlite3.connect('stocks.db')

    df = pd.read_sql_query("SELECT * FROM stock_history", conn)
    conn.close()
    

    df['date'] = pd.to_datetime(df['date'])
    return df


df = load_data()


st.sidebar.header("Filtry")

dostepne_spolki = df['ticker'].unique()

wybrane_spolki = st.sidebar.multiselect(
    "Wybierz spółki do wyświetlenia:",
    options=dostepne_spolki,
    default=dostepne_spolki 
)


filtered_df = df[df['ticker'].isin(wybrane_spolki)]


st.subheader("Aktualne wyceny (ostatnie pobranie)")

kolumny = st.columns(len(wybrane_spolki) if len(wybrane_spolki) > 0 else 1)

for idx, ticker in enumerate(wybrane_spolki):
    dane_spolki = filtered_df[filtered_df['ticker'] == ticker]
    if not dane_spolki.empty:
        
        ostatnia_cena = dane_spolki.sort_values(by='date', ascending=False).iloc[0]['price']
        kolumny[idx].metric(label=f"Cena {ticker}", value=f"{ostatnia_cena} PLN")


st.subheader("Historia notowań")
if not filtered_df.empty:
    
    fig = px.line(filtered_df, x='date', y='price', color='ticker', markers=True, title="Wykres cenowy spółek")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Brak danych do wyświetlenia. Wybierz spółkę z panelu bocznego.")


with st.expander("Pokaż surowe dane (Tabela)"):
    st.dataframe(filtered_df.sort_values(by='date', ascending=False))
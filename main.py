import polars as pl
import streamlit as st

CSV_PATH = "./data/Video_Game_Information.csv"

def showPlots(df: pl.DataFrame):
    st.markdown("# Video Game Information")
    st.markdown("## Correlation")
    st.dataframe(df)

    st.table(df.corr())


def run():
    df = pl.read_csv(CSV_PATH)
    showPlots(df)

if __name__ == "__main__":
    run()

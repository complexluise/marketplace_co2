import streamlit as st


def format_as_title(title):
    return st.markdown(
        f"<h1 style='text-align: center; color: #576F58;'>{title}</h1>",
        unsafe_allow_html=True,
    )


def format_as_subtitle(title):
    return st.markdown(
        f"<h2 style='text-align: center; color: #576F58;'>{title}</h2>",
        unsafe_allow_html=True,
    )

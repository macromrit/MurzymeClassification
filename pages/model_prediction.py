import streamlit as st
from io import StringIO
from model_exe import classificationWrapper

st.header("🏫 Murzyme | Non-Murzyme Classification")
st.divider()
uploaded_file = st.file_uploader("Choose a PDB file")
if uploaded_file is not None:
    # To read file as bytes and convert to string:
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()
    #st.write(string_data)
    inpt = ""
    for i in string_data.split('\n'):
        if 'TITLE' in i or 'KEYWDS' in i:
            inpt+=i

    ans = classificationWrapper(inpt)
    with st.container(border=True):    
        if ans == 1:
            st.markdown("## It's a Murzyme 🌟")
        else:
            st.markdown("## It's a Non-Murzyme 🌟")
        st.markdown("#### Details")
        for i in string_data.split('\n'):
            if 'TITLE' in i:
                st.markdown(F"###### TITLE: {i.strip().strip('TITLE').strip('KEYWDS')}") 
            if 'KEYWDS' in i:
                st.markdown(F"###### KEY-WORDS: {i.strip().strip('TITLE').strip('KEYWDS')}") 

    


    
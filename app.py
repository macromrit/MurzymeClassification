import streamlit as st
from datapoints import PDB_MURZ_RAW_TEXT, PDB_NON_MURZ_RAW_TEXT

st.markdown("# Search Our Feature DB 🧑🏻‍💻")

PDB_related_name = st.text_input("Enter the Title or KEYWDS of the PDB ")
st.write("The current search input is", PDB_related_name)


res_set = list()
for i in PDB_MURZ_RAW_TEXT:
    if PDB_related_name.casefold() in PDB_MURZ_RAW_TEXT[i].casefold() or PDB_related_name.casefold() in "murzymes":
        res_set.append([i, PDB_MURZ_RAW_TEXT[i], 'murzyme'])

for i in PDB_NON_MURZ_RAW_TEXT:
    if PDB_related_name.casefold() in PDB_NON_MURZ_RAW_TEXT[i].casefold() or PDB_related_name.casefold() in "non-murzymes":
        res_set.append([i, PDB_NON_MURZ_RAW_TEXT[i], 'non-murzyme'])

for ele in res_set[:50]:
    with st.container(border=True):
        st.markdown("##### ID: {}".format(ele[0]))
        st.markdown("##### Type: {}".format(ele[2]))
        st.divider()
        for k in ele[1].split('\n'):
            if "TITLE" in k:
                st.markdown("##### Title: {}".format(k).strip().strip("TITLE"))
            else:
                st.markdown("##### KeyWds: {}".format(k).strip().strip("KEYWDS"))
        st.divider()

        with open(F"{ele[2] if ele[2] == 'murzyme' else 'non_murzyme'}s/{ele[0]}.pdb", "r") as file:
            btn = st.download_button(
                    label="Download PDB file",
                    data=file.read(),
                    file_name=F"{ele[0]}.pdb",
                )

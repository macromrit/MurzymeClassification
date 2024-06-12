import streamlit as st
import requests

st.markdown("# Download PDB from RCSB ⬇️")

PDB_related_name = st.text_input("Input PDB Id of the murbun file")
st.write("The current search Id is", PDB_related_name)


def download_pdb(pdb_id, save_path=None):
    """
    Downloads a PDB file from the RCSB PDB site.

    Parameters:
    pdb_id (str): The ID of the PDB file to download.
    save_path (str): The path to save the downloaded PDB file. If None, saves in the current directory.
    """
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)
    if response.status_code == 200:
        file_name = f"{pdb_id}.pdb"
        if save_path:
            file_name = f"{save_path}/{file_name}"
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"PDB file {pdb_id} downloaded successfully.")
        return True
    else:
        print(f"Failed to download PDB file {pdb_id}. Status code: {response.status_code}")
        return False

if PDB_related_name: # if input is there
    # Example usage # download_pdb('1A2B')
    res = download_pdb(PDB_related_name, 'search_murbun')
    if res:
        with open('search_murbun/{}.pdb'.format(PDB_related_name)) as mammer:
            res = list()
            for i in mammer.read().split('\n'):
                if "TITLE" in i or "KEYWDS" in i:
                    res.append(i)

        with st.container(border=True):
            st.markdown("##### ID: {}".format(PDB_related_name))
            st.divider()
            for k in res:
                if "TITLE" in k:
                    st.markdown("##### Title: {}".format(k).strip().strip("TITLE"))
                else:
                    st.markdown("##### KeyWds: {}".format(k).strip().strip("KEYWDS"))
            st.divider()
            with open(F"search_murbun/{PDB_related_name}.pdb", "r") as file:
                btn = st.download_button(
                        label="Download PDB file",
                        data=file.read(),
                        file_name=F"{PDB_related_name}.pdb",
                    )
    else:
        st.markdown("### No such file exists")
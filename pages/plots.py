import streamlit as st
import pandas as pd
import numpy as np
import datapoints
import plotly.express as px




# Prepping Plots
tnse_f1 = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzyme"] for i in datapoints.TNSE_FASTA_FEATURE_1_M], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], 'non-murzyme'] for i in datapoints.TNSE_FASTA_FEATURE_1_NM], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )

tnse_f2 = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzyme"] for i in datapoints.TNSE_FASTA_FEATURE_2_M], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], 'non-murzyme'] for i in datapoints.TNSE_FASTA_FEATURE_2_NM], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )


tnse_f3 = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzyme"] for i in datapoints.TNSE_FASTA_FEATURE_3_M], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], 'non-murzyme'] for i in datapoints.TNSE_FASTA_FEATURE_3_NM], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )


tnse_f4 = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzyme"] for i in datapoints.TNSE_FASTA_FEATURE_4_M], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], 'non-murzyme'] for i in datapoints.TNSE_FASTA_FEATURE_4_NM], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )

pca_f1 = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzyme"] for i in datapoints.PCA_FASTA_FEATURE_1_M], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], 'non-murzyme'] for i in datapoints.PCA_FASTA_FEATURE_1_NM], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )

pca_f2 = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzyme"] for i in datapoints.PCA_FASTA_FEATURE_2_M], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], 'non-murzyme'] for i in datapoints.PCA_FASTA_FEATURE_2_NM], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )


pca_f3 = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzyme"] for i in datapoints.PCA_FASTA_FEATURE_3_M], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], 'non-murzyme'] for i in datapoints.PCA_FASTA_FEATURE_3_NM], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )


pca_f4 = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzyme"] for i in datapoints.PCA_FASTA_FEATURE_4_M], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], 'non-murzyme'] for i in datapoints.PCA_FASTA_FEATURE_4_NM], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )


# Plots

st.markdown("<center><h2>📊 Fasta Data Plots - TNSE<h2></center>", unsafe_allow_html=True)


fig_1 = px.scatter(
    tnse_f1,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)
with st.container(border=True):
    st.markdown("<center>Feature 1</center>", unsafe_allow_html=True)
    event_1 = st.plotly_chart(fig_1, key="tnse_1", on_select="rerun")

# -------------

fig_2 = px.scatter(
    tnse_f2,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)
with st.container(border=True):
    st.markdown("<center>Feature 2</center>", unsafe_allow_html=True)
    event_2 = st.plotly_chart(fig_2, key="tnse_2", on_select="rerun")

# -------------

fig_3 = px.scatter(
    tnse_f3,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)
with st.container(border=True):
    st.markdown("<center>Feature 3</center>", unsafe_allow_html=True)
    event_3 = st.plotly_chart(fig_3, key="tnse_3", on_select="rerun")

# -------------

fig_4 = px.scatter(
    tnse_f4,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)
with st.container(border=True):
    st.markdown("<center>Feature 4</center>", unsafe_allow_html=True)
    event_4 = st.plotly_chart(fig_4, key="tnse_4", on_select="rerun")

# -------------
st.divider()
st.markdown("<center><h2>📊 Fasta Data Plots - PCA<h2></center>", unsafe_allow_html=True)

fig_5 = px.scatter(
    pca_f1,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)
with st.container(border=True):
    st.markdown("<center>Feature 1</center>", unsafe_allow_html=True)
    event_5 = st.plotly_chart(fig_5, key="pca_1", on_select="rerun")

# -------------

fig_6 = px.scatter(
    pca_f2,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)
with st.container(border=True):
    st.markdown("<center>Feature 2</center>", unsafe_allow_html=True)
    event_6 = st.plotly_chart(fig_6, key="pca_2", on_select="rerun")

# -------------

fig_7 = px.scatter(
    pca_f3,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)
with st.container(border=True):
    st.markdown("<center>Feature 3</center>", unsafe_allow_html=True)
    event_7 = st.plotly_chart(fig_7, key="pca_3", on_select="rerun")

# -------------

fig_8 = px.scatter(
    pca_f4,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)
with st.container(border=True):
    st.markdown("<center>Feature 4</center>", unsafe_allow_html=True)
    event_8 = st.plotly_chart(fig_8, key="pca_4", on_select="rerun")

# -------------

st.divider()
st.markdown("<center><h2>📊 PDB Data Plots - PCA<h2></center>", unsafe_allow_html=True)

# PDB data prep

# tnse_pdb = pd.concat(
#     [
#         pd.DataFrame([[i[0], i[1], "murzyme"] for i in zip(datapoints.TNSE_PDB_M["murzyme_x"], datapoints.TNSE_PDB_M['murzyme_y'])], columns=["x", "y", "murzymes or non-murzymes"]),
#         pd.DataFrame([[i[0], i[1], "murzyme"] for i in zip(datapoints.TNSE_PDB_M["non_murzyme_x"], datapoints.TNSE_PDB_M['non_murzyme_y'])], columns=["x", "y", "murzymes or non-murzymes"]),
#     ]
#     )

print(
    
    [[i[0], i[1], "murzymes"] for i in zip(datapoints.TNSE_PDB_NM[0], datapoints.TNSE_PDB_NM[1])]
    )


pca_pdb = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzymes"] for i in zip(datapoints.PCA_PDB_M[0], datapoints.PCA_PDB_M[1])], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], "non-murzymes"] for i in zip(datapoints.PCA_PDB_NM[0], datapoints.PCA_PDB_NM[1])], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )

fig_9 = px.scatter(
    pca_pdb,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)

with st.container(border=True):
    st.markdown("<center>PCA - PDB Embeddings</center>", unsafe_allow_html=True)
    event_8 = st.plotly_chart(fig_9, key="pca_pdb", on_select="rerun")

# -------


tnse_pdb = pd.concat(
    [
        pd.DataFrame([[i[0], i[1], "murzymes"] for i in zip(datapoints.TNSE_PDB_M[0], datapoints.TNSE_PDB_M[1])], columns=["x", "y", "murzymes or non-murzymes"]),
        pd.DataFrame([[i[0], i[1], "non-murzymes"] for i in zip(datapoints.TNSE_PDB_NM[0], datapoints.TNSE_PDB_NM[1])], columns=["x", "y", "murzymes or non-murzymes"])
    ]
    )

fig_10 = px.scatter(
    tnse_pdb,
    x="x",
    y="y",
    color="murzymes or non-murzymes",
    #size="petal_length",
    hover_data=["murzymes or non-murzymes"],
)

with st.container(border=True):
    st.markdown("<center>TNSE - PDB Embeddings</center>", unsafe_allow_html=True)
    event_8 = st.plotly_chart(fig_10, key="pca_pdb", on_select="rerun")

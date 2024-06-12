import json

MURZYMES_PDB_EMBEDDINGS = list()
NON_MURZYMES_PDB_EMBEDDINGS = list()

with open("murbun_pdb_embeddings.json", "r") as murbun_pdb:
    murbun_pdb_embeddings = json.loads(murbun_pdb.read())
    for k, v  in murbun_pdb_embeddings.items():
        if v[1] == "murzyme":
            MURZYMES_PDB_EMBEDDINGS.append((k, v[0]))
        else:
            NON_MURZYMES_PDB_EMBEDDINGS.append((k, v[0]))



# PLOTS
# fasta features 1, 2, 3, 4
with (open("pca/murzymes/feature1_murzymes_pca.json") as a_1,
      open("pca/non_murzymes/feature1_non_murzymes_pca.json") as a_2,
      open("pca/murzymes/feature2_murzymes_pca.json") as b_1,
      open("pca/non_murzymes/feature2_non_murzymes_pca.json") as b_2,
      open("pca/murzymes/feature3_murzymes_pca.json") as c_1,
      open("pca/non_murzymes/feature3_non_murzymes_pca.json") as c_2,
      open("pca/murzymes/feature4_murzymes_pca.json") as d_1,
      open("pca/non_murzymes/feature4_non_murzymes_pca.json") as d_2,):
    

    PCA_FASTA_FEATURE_1_M = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(a_1.read()).items()])]
    PCA_FASTA_FEATURE_1_NM = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(a_2.read()).items()])]
    PCA_FASTA_FEATURE_2_M = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(b_1.read()).items()])]
    PCA_FASTA_FEATURE_2_NM = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(b_2.read()).items()])]
    PCA_FASTA_FEATURE_3_M = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(c_1.read()).items()])]
    PCA_FASTA_FEATURE_3_NM = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(c_2.read()).items()])]
    PCA_FASTA_FEATURE_4_M = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(d_1.read()).items()])]
    PCA_FASTA_FEATURE_4_NM = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(d_2.read()).items()])]

# print(PCA_FASTA_FEATURE_1_NM)

with (open("tnse/murzymes/feature1_murzymes_tnse.json") as a_1,
      open("tnse/non_murzymes/feature1_non_murzymes_tnse.json") as a_2,
      open("tnse/murzymes/feature2_murzymes_tnse.json") as b_1,
      open("tnse/non_murzymes/feature2_non_murzymes_tnse.json") as b_2,
      open("tnse/murzymes/feature3_murzymes_tnse.json") as c_1,
      open("tnse/non_murzymes/feature3_non_murzymes_tnse.json") as c_2,
      open("tnse/murzymes/feature4_murzymes_tnse.json") as d_1,
      open("tnse/non_murzymes/feature4_non_murzymes_tnse.json") as d_2,):

    TNSE_FASTA_FEATURE_1_M = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(a_1.read()).items()])]
    TNSE_FASTA_FEATURE_1_NM = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(a_2.read()).items()])]
    TNSE_FASTA_FEATURE_2_M = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(b_1.read()).items()])]
    TNSE_FASTA_FEATURE_2_NM = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(b_2.read()).items()])]
    TNSE_FASTA_FEATURE_3_M = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(c_1.read()).items()])]
    TNSE_FASTA_FEATURE_3_NM = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(c_2.read()).items()])]
    TNSE_FASTA_FEATURE_4_M = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(d_1.read()).items()])]
    TNSE_FASTA_FEATURE_4_NM = [[j[0][0], j[0][1]] for j in zip([(v[0], v[1]) for k, v in json.loads(d_2.read()).items()])]

# print(TNSE_FASTA_FEATURE_4_NM)

# # +++===========+++
# PDB points for TNSE and PCA

with (open("plot_data/pca_datapoints.json") as pca, open("plot_data/tnse_datapoints.json") as tnse):
    pca_read = pca.read()
    TNSE_PDB_M = [json.loads(pca_read)["murzyme_x"], json.loads(pca_read)["murzyme_y"]]
    TNSE_PDB_NM = [json.loads(pca_read)["non_murzyme_x"], json.loads(pca_read)["non_murzyme_y"]]

    non_pca_read = tnse.read()
    PCA_PDB_M = [json.loads(non_pca_read)["murzyme_x"], json.loads(non_pca_read)["murzyme_y"]]
    PCA_PDB_NM = [json.loads(non_pca_read)["non_murzyme_x"], json.loads(non_pca_read)["non_murzyme_y"]] 
    

with (open('murzyme_pdb_features.json') as kammer,
      open('non_murzyme_pdb_features.json') as mammer):
    PDB_MURZ_RAW_TEXT = json.loads(kammer.read())
    PDB_NON_MURZ_RAW_TEXT = json.loads(mammer.read())


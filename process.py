import glob
import json

# Specify the directory path
murzyme_directory_path = "murzymes"
non_murzyme_directory_path = "non_murzymes"

# Define the pattern to match .pdb files
murzyme_pdb_files = glob.glob(f"{murzyme_directory_path}/*.pdb")
non_murzyme_pdb_files = glob.glob(f"{non_murzyme_directory_path}/*.pdb")

# Print the list of .pdb files
print("Total Number of Murzyme Files Registered:",len(murzyme_pdb_files))
print("Total Number of Non-Murzyme Files Registered:", len(non_murzyme_pdb_files))

# KEYWDS
# TITLE

murzyme_features = dict()
non_murzyme_features = dict()

for murzyme_file in murzyme_pdb_files:
    with open(murzyme_file, 'r') as jammer:
        data = list()
        for line in jammer.readlines():
            if "TITLE" in line or "KEYWDS" in line:
                data.append(line.strip())
    murzyme_features[murzyme_file.strip('.pdb').strip('murzymes/')] = '\n'.join(data)

for non_murzyme_file in non_murzyme_pdb_files:
    with open(non_murzyme_file, 'r') as hammer:
        data = list()
        for line in hammer.readlines():
            if "TITLE" in line or "KEYWDS" in line:
                data.append(line.strip())
    non_murzyme_features[non_murzyme_file.strip('.pdb').strip('non_murzymes/')] = '\n'.join(data)

with open("murzyme_pdb_features.json", "w") as m_writer:
    m_writer.write(json.dumps(murzyme_features))


with open("non_murzyme_pdb_features.json", "w") as nm_writer:
    nm_writer.write(json.dumps(non_murzyme_features))
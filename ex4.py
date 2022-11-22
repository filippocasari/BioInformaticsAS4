import pandas as pd
import numpy as np
import sys
#print(MatrixInfo.blosum50)
import os

import warnings
warnings.filterwarnings("ignore")


path = "CSV"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs(path)
   print("dir "+ path+"created")
path = "TEX"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs(path)
   print("dir "+ path+"created")
if(len(sys.argv) < 2):
    raise ValueError("Exiting, expected more arguments")

seq1 = sys.argv[1]#"TGCTTTACTCGTTATATTGAATATC"
seq2 =sys.argv[2] #"TGCTTCACAAGATATATTGAATATC"
seq3 =sys.argv[3]#"TGCTTTACCCGTTACATTGAATATC"
seq4 =sys.argv[4]#"TGCTTTACCCGTTATATTGAGTATC"
seq5 =sys.argv[5]#"TGCTTTACCCGATATATAGAGTATC"
print("sequences input:")
for i in sys.argv[1:]:
    print(i)

rand_prob = 0.25

table_freqs =[]

amino_acids = ["A", "T", "C", "G", "SUM"]
table_freqs.append(amino_acids)
amino_acids = ["A", "T", "C", "G"]

for i in range(len(seq1)):
    column = []
    for amin in amino_acids:
        
        column.append(1+seq1[i].count(amin) +seq2[i].count(amin) + seq3[i].count(amin)+seq4[i].count(amin) + seq5[i].count(amin))
    column.append(sum(column))
    table_freqs.append(column)
table_freqs = np.array(table_freqs, dtype=object).T

table_freqs_norm = np.round(table_freqs[0:, 1:].astype(float)/table_freqs[4, 1], 3)
table_freqs_dataframe = pd.DataFrame((table_freqs))

print("\nFrequency Table:\n", table_freqs_dataframe)
table_freqs_dataframe.to_csv("CSV/table_freqs.csv")
table_freqs_dataframe.to_latex("TEX/table_freqs.tex")

table_freqs_norm_dataframe = pd.DataFrame(table_freqs_norm)
print("\nRelative Frequency Table:\n", table_freqs_norm_dataframe)
table_freqs_norm_dataframe.T.to_csv("CSV/table_rel_freqs.csv")
table_freqs_norm_dataframe.T.to_latex("TEX/table_rel_freqs.tex")

table_log_freqs = np.round(np.log2((table_freqs_norm.astype(float)[:4, :]/rand_prob)), 3)
table_log_freqs_dataframe = pd.DataFrame(table_log_freqs)

#HUMAN= "TGCATCTCCCTTTCCTCTGTCCTCC"

CHIMPANZEE ="CACGCCTCCCGGTCAGAGACAAGAG"
HOMO_SAPIENS ="CAAGCCTCCCGGTCAGAGACAAGAG" #"TGCATCTCCCTTTCCTCTGTCCTCC"#

table_log_freqs_dataframe.insert(0, "AminoAcids", amino_acids)
print("\nPosition Specific Scoring Matrix: \n", table_log_freqs_dataframe)
table_log_freqs_dataframe.T.to_csv("CSV/table_log_freqs.csv")
table_log_freqs_dataframe.T.to_latex("TEX/table_log_freqs.tex")

sum_score_CHIMPANZEE =0.
sum_score_HOMO_SAPIENS =0.
for i in range(len(HOMO_SAPIENS)):
    char = CHIMPANZEE[i]
    char2 = HOMO_SAPIENS[i]
    pos = amino_acids.index(char)
    pos2 = amino_acids.index(char2)
    sum_score_CHIMPANZEE+= table_log_freqs[pos][i]
    sum_score_HOMO_SAPIENS+= table_log_freqs[pos2][i]

print("Sum Score for HOMO SAPIENS\n", sum_score_HOMO_SAPIENS)
print("Sum Score for CHIMPANZEE\n", sum_score_CHIMPANZEE)
    










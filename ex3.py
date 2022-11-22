from Bio.SubsMat import MatrixInfo
import pandas as pd
import numpy as np
import os
#print(MatrixInfo.blosum50)
query = "CCYEKRRKHYCQHCNQWWVEW"
test = "CCLVILPGHCDDIEW"

cols =[]
rows= []
path = "TEX"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs(path)
   print("dir "+ path+"created")

for i in range(len(query)-2):
    
    rows.append(query[i]+query[i+1]+query[ i+2])
for i in range(len(test)-2):
    
    cols.append(test[i]+test[i+1]+test[ i+2])
print(rows)
print(cols)
#print(pd.DataFrame(MatrixInfo.blosum50))
matrix =[]
count_cols = -1
for i in cols:
    count_cols += 1
    matrix.append([])
    for j in rows:
        
        #sum_cell += MatrixInfo.blosum50[([i[0], j[0]])]
        char1, char2 = list(i), list(j)
        
        #print(char1[0], char2[0])
        #pair = (char2[0], char1[0])
        try:
            #print(char1[0], char2[0])
            pair = (char2[0], char1[0])
            sum1 = MatrixInfo.blosum50[pair]
            
        except:
            pair = (char1[0], char2[0])
            sum1 = MatrixInfo.blosum50[pair]
        
        try:
            pair2 = (char2[1], char1[1])
            sum2 = MatrixInfo.blosum50[pair2]
        except:
            pair2 = (char1[1], char2[1])
            sum2 = MatrixInfo.blosum50[pair2]
        
        try:
            
            pair3 = (char2[2], char1[2])
            sum3 = MatrixInfo.blosum50[pair3]
        except:
            pair3 = (char1[2], char2[2])
            sum3 = MatrixInfo.blosum50[pair3]
        print(f"pair {pair} pair 2 {pair2} pair3 {pair3} ")
        sum_cell =  sum1 + sum2 + sum3

        matrix[count_cols].append(sum_cell)
matrix_array = np.array(matrix).T
matrix_dataframe = pd.DataFrame(matrix_array, columns=cols)
matrix_dataframe.insert( loc=0,
          column='query',
          value=rows)
threshold_acceptance = 20.
print(matrix_dataframe)#
matrix_dataframe.to_latex("TEX/wmer_matrix.tex")
rows = ["S", "P", "G", "P", "E", "R", "G", "P", "P"]
cols = ["T", "P", "G", "E", "S", "P", "P"]

#print(((matrix_array>=threshold_acceptance)))
#print(np.where(matrix_array>=threshold_acceptance))
#print(matrix_dataframe[matrix_dataframe>= threshold_acceptance])



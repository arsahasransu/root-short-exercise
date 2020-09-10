import ROOT
import numpy as np
import pandas

df = ROOT.RDataFrame('TreeS', 'https://root.cern/files/tmva_class_example.root')
columns = ['var1','var2','var3','var4']
data = df.AsNumpy(columns)
print('Column 0: ',data['var1'][0],data['var2'][0],data['var3'][0],data['var4'][0])

print('Means: {',[np.mean(data[c]).item() for c in columns],'}')

pdf = pandas.DataFrame(data)
print('Pandas Format - Column 0: ',pdf.iloc[0,:])

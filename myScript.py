import ROOT

rfile = ROOT.TFile.Open('https://root.cern/files/tmva_class_example.root')
for key in rfile.GetListOfKeys():
    name = key.GetName()
    entries = rfile.Get(name).GetEntries()
    print('{} : {}'.format(name, entries))

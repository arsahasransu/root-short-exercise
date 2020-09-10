import ROOT
import numpy as np

# Make global style changes
ROOT.gStyle.SetOptStat(0) # Disable the statistics box
ROOT.gStyle.SetTextFont(42)

# Create a canvas
c = ROOT.TCanvas('c', 'my canvas', 800, 600)

# Create a histogram with some dummy data and draw it
data = np.random.randn(1000).astype(np.float32)
h = ROOT.TH1F('h', ';Gaussian process; N_{Events}', 30, -3, 3)
for x in data: h.Fill(x)
h.Draw('E')

# Fit a Gaussian function to the data
f = ROOT.TF1('f', '[0] * exp(-0.5 * ((x - [1]) / [2])**2)')
f.SetParameters(100, 0, 1)
h.Fit(f)

# Let's add some CMS style headline
label = ROOT.TLatex()
label.SetNDC(True)
label.SetTextSize(0.040)
label.DrawLatex(0.10, 0.92, '#bf{CMS Dummy Data}')
label.DrawLatex(0.58, 0.92, '#sqrt{s} = 13 TeV, L_{int} = 100 fb^{-1}')

# Save as png file and show interactively
c.SaveAs('dummy_data.png')
c.Draw()

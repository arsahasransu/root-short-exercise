import ROOT

# Enable multi-threading with the specified amount of threads (let's start with just one)
# Note that older ROOT versions may require to write ROOT.ROOT.EnableImplicitMT()
ROOT.ROOT.EnableImplicitMT(1)

# Or enable multi-threading with an auto-detected amount of threads
#ROOT.EnableImplicitMT()

# Create dataframe from a (reduced) NanoAOD file
df = ROOT.RDataFrame("Events", "Run2012BC_DoubleMuParked_Muons.root")

# For simplicity, select only events with exactly two muons and require opposite charge
df_2mu = df.Filter("nMuon == 2", "Events with exactly two muons")
df_os = df_2mu.Filter("Muon_charge[0] != Muon_charge[1]", "Muons with opposite charge")

# Compute invariant mass of the dimuon system

# Perform the computation of the invariant mass in C++
ROOT.gInterpreter.Declare('''
using Vec_t = const ROOT::RVec<float>&;
float ComputeInvariantMass(Vec_t pt, Vec_t eta, Vec_t phi, Vec_t mass) {
    const ROOT::Math::PtEtaPhiMVector p1(pt[0], eta[0], phi[0], mass[0]);
    const ROOT::Math::PtEtaPhiMVector p2(pt[1], eta[1], phi[1], mass[1]);
    return (p1 + p2).M();
}
''')

# Add the result of the computation to the dataframe
df_mass = df_os.Define("Dimuon_mass", "ComputeInvariantMass(Muon_pt, Muon_eta, Muon_phi, Muon_mass)")

# Book histogram of the dimuon mass spectrum (does not actually run the computation!)
h = df_mass.Histo1D(("Dimuon_mass", ";m_{#mu#mu} (GeV);N_{Events}", 30000, 0.25, 300), "Dimuon_mass")

# Request a cut-flow report (also does not run the computation yet!)
report = df_mass.Report()

# Produce plot
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetTextFont(42)
c = ROOT.TCanvas("c", "", 800, 700)
# The contents of one of the dataframe results are accessed for the first time here:
# this is when all results will actually be produced!
h.GetXaxis().SetTitleSize(0.04)
h.GetYaxis().SetTitleSize(0.04)
c.SetLogx(); c.SetLogy()
h.Draw()

label = ROOT.TLatex()
label.SetNDC(True)
label.SetTextSize(0.040)
label.DrawLatex(0.100, 0.920, "#bf{CMS Open Data}")
label.DrawLatex(0.550, 0.920, "#sqrt{s} = 8 TeV, L_{int} = 11.6 fb^{-1}")

# Save as png file
c.SaveAs("dimuon_spectrum.png")

# Print cut-flow report
report.Print()

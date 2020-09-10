SAMPLES=(
    GluGluToHToTauTau
    VBF_HToTauTau
    DYJetsToLL
    TTbar
    W1JetsToLNu
    W2JetsToLNu
    W3JetsToLNu
    Run2012B_TauPlusX
    Run2012C_TauPlusX
    )

for SAMPLE in ${SAMPLES[@]}
do
    # Via XRootD:
    xrdcp root://eospublic.cern.ch//eos/root-eos/HiggsTauTauReduced/${SAMPLE}.root .
    # Via HTTP:
    # curl -O https://root.cern/files/HiggsTauTauReduced/${SAMPLE}.root
done

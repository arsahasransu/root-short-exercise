#include "TFile.h"
#include "TTree.h"
#include <iostream>

void myScript_3() {
  auto file = TFile::Open("https://root.cern/files/tmva_class_example.root");
  for (auto key : *file->GetListOfKeys()) {
    const auto name = key->GetName();
    const auto entries = file->Get<TTree>(name)->GetEntries();
    std::cout << name << " : " << entries << std::endl;
  }
}

int main() {

  myScript_3();
  return 0;

}

import ROOT

ROOT.gInterpreter.Declare('''
int my_heavy_computation(std::string x) {

return x.length();

}
''')

# Functions and object made available via the interpreter are accessible from
# the ROOT module
y = ROOT.my_heavy_computation("the ultimate answer to life and everything")
print(y) # Guess the result!

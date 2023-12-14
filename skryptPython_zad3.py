from modeller import *
from modeller.automodel import *

env = Environ()
env.io.atom_files_directory = [".", "./atom_files"]

a = AutoModel(env, alnfile="dopasowanie.txt", knowns=("3J4Q", "6F14", "1CTP"), sequence="model",)
a.make()
a.write("wyjscie_modeller-sekwencja.pdb")

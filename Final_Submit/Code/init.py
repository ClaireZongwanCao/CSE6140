from Approximation import Approximation
from BnB import BnB
from localSearch1 import LocalSearch1
from localSearch2 import LocalSearch2

def initialize_project(filename, cutoff, method_use, random_seed):
	print method_use
	if method_use == "Approx":
		Approximation(filename, cutoff, random_seed)
	elif method_use == "BnB":
		BnB(filename, cutoff, random_seed)
	elif method_use == "LS1":
		LocalSearch1(filename,cutoff,random_seed)
	elif method_use == "LS2":
		LocalSearch2(filename,cutoff,random_seed)
		
initialize_project("sample",1000, "BnB", 512)
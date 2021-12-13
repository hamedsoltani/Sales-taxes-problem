import random
import numpy as np
from input import *
from tax.TaxModel import *

def main0():

    data = input
    for item in data:
        factor = TaxModel(data[item])
        data[item] = factor.calculateTax(exempt = exemptTax)
        factor.printOut()



if __name__ == "__main__":
    # execute only if run as a script
    main0()





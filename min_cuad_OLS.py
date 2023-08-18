import pandas_datareader.data as wb
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np
import warnings
import argparse
from colorama import init, Fore, Style

init()

warnings.filterwarnings("ignore")

def validate_date(d):
    try:
        return datetime.strptime(d, '%Y-%m-%d')
    except:
        raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + "Bad date format (must be '%Y-%m-%d')" + Fore.RESET +Style.RESET_ALL)

def main():
    parser = argparse.ArgumentParser(prog='cuad_minOLS', description="OLS Regression")
    parser.add_argument('-dv', '--dependent_var', required=True, type=str, help="dependent variable")
    parser.add_argument('-iv', '--independent_var', required=True, type=str, help="independent variable")
    parser.add_argument('-st','--start',type=validate_date, required=True, help="Start date for regression")
    parser.add_argument('-e','--end',type=validate_date, help="End date for regression")
    
    args = parser.parse_args()

    
if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas_datareader.data as wb
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np
import warnings
import argparse
from colorama import init, Fore, Style
from datetime import datetime

init()

warnings.filterwarnings("ignore")

def make_model(v,s):
    data = wb.DataReader(v, 'fred', s)
    mod = smf.ols(f'{v[0]} ~ {v[1]}', np.log(data)).fit()
    print(Fore.GREEN + '\n')
    print(mod.summary(), mod.params)
    print(Fore.RESET)

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
    make_model([args.dependent_var,args.independent_var],args.start)

    
if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
import numpy as np
from os import system
import argparse

def main():
    parser = argparse.ArgumentParser(prog="macd 0.0", description="MCAD from CMD",
                                     epilog="")
    parser.add_argument('-sym','--symbol',required=True,type=str, help="Thicker symbol")
    parser.add_argument('-st','--start',type=str, help="Thicker symbol")

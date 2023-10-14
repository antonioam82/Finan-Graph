from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import argparse
from pynput import keyboard
from colorama import init, Fore, Back, Style

def main():
    parser = argparse.ArgumentParser(prog="QUOTER 0.0",description="Show quotes in real time")
    parser.add_argument('-tick', '--ticker', required=True, type=str, help='Ticker name')
    parser.add_argument('-int', '--interval', type=str, help='Interval')

    args = parser.parse_args()
    print("OK")

if __name__ == '__main__':
    main()

import argparse
import pandas as pd
import sys
from corella import Corella


def main():
    parser = argparse.ArgumentParser(description='Plot a correlation matrix')
    parser.add_argument('--pos-color', type=str, default='light_red', help='color for positive correlation')
    parser.add_argument('--neg-color', type=str, default='light_blue', help='color for negative correlation')
    parser.add_argument('--input', type=str, required=False, help='delimited input file')
    parser.add_argument('--delimiter', type=str, default=',', help='delimiter for the input file')
    parser.add_argument('--method', type=str, default='pearson',
                        help='method to use for correlation (pearson/kendall/spearman)')
    parser.add_argument('--padding', type=int, default=20, help='left padding for the plot')
    parser.add_argument('--no-header', action='store_true', default=False, help='input data has no header')
    args = parser.parse_args()

    C = Corella(pos_color=args.pos_color, neg_color=args.neg_color, padding=args.padding)
    if args.input:
        df = pd.read_csv(args.input, delimiter=args.delimiter, header=None if args.no_header else 'infer')
    else:
        df = pd.read_csv(sys.stdin, delimiter=args.delimiter, header=None if args.no_header else 'infer')
    C.draw(df, args.method)

if __name__ == '__main__':
    main()
import pandas as pd
from colored import fg, bg, attr
import sys

GRADIENT_CHARS = ['█', '▓', '▒', '░']
# GRADIENT_CHARS = ['#', '▓', '▒', '░']
# GRADIENT_CHARS = list('ᚋᚌᚍᚎᚏ')
GRADIENT_COLORS = ['blue'] * len(GRADIENT_CHARS) + ['yellow'] + ['red'] * len(GRADIENT_CHARS)
GRADIENT = GRADIENT_CHARS + [' '] + GRADIENT_CHARS[::-1]


def draw_row(cells):
	for n_cell, cell in enumerate(cells):
		val = int((float(cell)+1) // (2/(len(GRADIENT)-1)))
		print('{color}{c}{c}{c}{c}{reset}'.format(
			color=fg(GRADIENT_COLORS[val]),
			c=GRADIENT[val],
			reset=attr('reset')
			), end='')


df = pd.read_csv(sys.argv[1])
corr_df = df.corr()
a = corr_df.to_csv(index=False)
lines = a.strip('\n').split('\n')
header = lines.pop(0).split(',')
print('\n')
for n, l in enumerate(lines):
	print(header[n].ljust(17, '.'), end='')
	print(str(n+1).rjust(2, '0'), end=' ')
	cells = l.split(',')
	draw_row(cells)
	print('\n' + (' '*20), end='')
	draw_row(cells)
	print()

print('\n' + (' '*20), end='')
for n in range(len(lines)):
	print(' {} '.format(str(n+1).rjust(2, '0')), end='')
print('\n')

# Display legend
print('-1.0 '.rjust(20), end='')
for char, cols in zip(GRADIENT, GRADIENT_COLORS):
	print('{color}{c}{reset}'.format(
			color=fg(cols) if char != ' ' else  '',
			c=char * 5 if char != ' ' else ' 0.0  ',
			reset=attr('reset')
			), end='')
print(' 1.0')


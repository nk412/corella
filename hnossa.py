import pandas as pd
from colored import fg, bg, attr
import sys

GRADIENT = [196, 197, 198, 199, 200, 201, 207, 213, 219, 225, 224, 223, 222, 221, 220][::-1]
# GRADIENT = [34, 35, 36, 37, 38, 39]
GRADIENT = list(range(82, 88))[::-1]
GRADIENT = [33, 45, 123, 254, 183, 170, 160][::-1]
GRADIENT = list(range(237, 254))
GRADIENT_COLORS = ['light_blue'] * 4 + ['yellow'] + ['magenta'] * 4
GRADIENT_CHARS = ['█', '▓', '▒', '░']
GRADIENT = GRADIENT_CHARS + [' '] + GRADIENT_CHARS[::-1]

print('\n')

df = pd.read_csv(sys.argv[1])
corr_df = df.corr()
a = corr_df.to_csv(index=False)
lines = a.strip('\n').split('\n')
header = lines.pop(0).split(',')
for n, l in enumerate(lines):
	print(header[n].ljust(17, '.'), end='')
	print(str(n+1).rjust(2, '0'), end=' ')
	cells = l.split(',')
	for n_cell, cell in enumerate(cells):
		if n_cell > n:
			if (n_cell - n) % 2 == 1:
				print(str(round(float(cell),1)).rjust(4), end='')
			else:
				print('    ', end='')
			continue
		val = int((float(cell)+1) // (2/(len(GRADIENT)-1)))
		print('{color}{c}{c}{c}{c}{reset}'.format(
			color=fg(GRADIENT_COLORS[val]),
			c=GRADIENT[val],
			reset=attr('reset')
			), end='')
	print('\n' + (' '*20), end='')
	for n_cell, cell in enumerate(cells):
		if n_cell > n:
			if (n_cell - n) % 2 == 0:
				print(str(round(float(cell),1)).rjust(4), end='')
			else:
				print('    ', end='')
			continue
		val = int((float(cell)+1) // (2/(len(GRADIENT)-1)))
		print('{color}{c}{c}{c}{c}{reset}'.format(
			color=fg(GRADIENT_COLORS[val]),
			c=GRADIENT[val],
			reset=attr('reset')
			), end='')
	print()

print('\n' + (' '*20), end='')
for n in range(len(lines)):
	print(' {} '.format(str(n+1).rjust(2, '0')), end='')
print('\n')

print('-1.0 '.rjust(20), end='')
for char, cols in zip(GRADIENT, GRADIENT_COLORS):
	print('{color}{c}{reset}'.format(
			color=fg(cols) if char != ' ' else  '',
			c=char * 5 if char != ' ' else '  0  ',
			reset=attr('reset')
			), end='')
print(' 1.0')

# for x in range(16, 255):
# 	color = bg(x)
# 	res = attr('reset')
# 	print(str(x) + '  ' + color + "  " + res)\

import pandas as pd
from colored import fg, bg, attr
import sys

GRADIENT = [196, 197, 198, 199, 200, 201, 207, 213, 219, 225, 224, 223, 222, 221, 220][::-1]
# GRADIENT = [34, 35, 36, 37, 38, 39]
GRADIENT = list(range(82, 88))[::-1]
GRADIENT = [33, 45, 123, 254, 183, 170, 160][::-1]
GRADIENT = list(range(237, 254))
GRADIENT = [33, 81, 159, 195, 254, 220, 208, 202, 160]
# GRADIENT_CHARS = ['█', '▓', '▒', '░']
# GRADIENT = GRADIENT_CHARS + [' '] + GRADIENT_CHARS[::-1]

df = pd.read_csv(sys.argv[1])
corr_df = df.corr()

a = corr_df.to_csv(index=False)

lines = a.strip('\n').split('\n')
header = lines.pop(0).split(',')
for n, l in enumerate(lines):
	print(header[n].ljust(20, '.'), end='')
	cells = l.split(',')
	for cell in cells:
		val = int((float(cell)+1) // (2/(len(GRADIENT)-1)))
		color = fg(GRADIENT[val])
		res = attr('reset')
		print(color + '▓▓' + res, end='')
		# print(color + str(round(val, 2)) + '/' + str(round(float(cell), 2)) + res, end ='         ')
	print()

print ('\n-ve correlation ', end='')
for x in GRADIENT:
	color = fg(x)
	res = attr('reset')
	# print(x + )
	print(color + "▓▓" + res, end='')
print(' +ve correlation')

# for x in range(16, 255):
# 	color = bg(x)
# 	res = attr('reset')
# 	print(str(x) + '  ' + color + "  " + res)\



██▓▓▒▒░░
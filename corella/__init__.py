import colored


class Corella():
    GRADIENT_CHARS = ['▓', '▒', '░']

    def __init__(self, pos_color='light_red', neg_color='light_blue', padding=20):
        len_chars = len(self.GRADIENT_CHARS)
        self.gradient = self.GRADIENT_CHARS + [' '] + self.GRADIENT_CHARS[::-1]
        self.gradient_colors = [neg_color] * len_chars + ['yellow'] + [pos_color] * len_chars
        self.padding = padding
        self.reset_colors = colored.attr('reset')

    def _draw_row(self, cells, rows=2):
        """ Displays a colored row for the given cells """
        for n_row in range(rows):
            if n_row > 0:
                print(' ' * self.padding, end='')
            for n_cell, cell in enumerate(cells):
                try:
                    cell = float(cell)
                except ValueError:
                    cell = 0
                val = int((float(cell) + 1) // (2 / (len(self.gradient) - 1)))
                print('{color}{c}{c}{c}{c}{reset}'.format(
                    color=colored.fg(self.gradient_colors[val]),
                    c=self.gradient[val],
                    reset=self.reset_colors
                ), end='')
            print()

    def _label_columns(self, n_cols):
        """ Displays the column indices padded along with the matrix """
        print('\n' + (' ' * self.padding), end='')
        for n in range(n_cols):
            print(' {} '.format(str(n + 1).rjust(2, '0')), end='')
        print()

    def _draw_legend(self, cell_width=5):
        print()
        print('-1.0 '.rjust(self.padding), end='')
        for char, clr in zip(self.gradient, self.gradient_colors):
            print('{color}{c}{reset}'.format(
                color=colored.fg(clr) if char != ' ' else  '',
                c=char * cell_width if char != ' ' else '  0  ',
                reset=self.reset_colors
            ), end='')
        print(' +1.0\n')

    def draw(self, df, method='pearson'):
        self.padding = max(self.padding, max(map(len, df.columns)) + 4)
        corr_df = df.corr(method=method)
        a = corr_df.to_csv(index=False)
        lines = a.strip('\n').split('\n')
        header = lines.pop(0).split(',')

        print()
        for n, l in enumerate(lines):
            print(header[n].ljust(self.padding - 3, ' '), end='')
            print(str(n + 1).rjust(2, '0'), end=' ')
            self._draw_row(l.split(','))
        self._label_columns(len(lines))

        cell_width = max(2, (len(lines) * 4) // len(self.gradient))
        self._draw_legend(cell_width)

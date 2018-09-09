# corella
Correlation plots on the terminal, for quick and simple insights. Powered by `pandas`.

<img src="https://github.com/nk412/corella/raw/master/imgs/fifa.png" width=720>

_Dataset source: [FIFA World Cup 2018 Match Stats](https://www.kaggle.com/mathan/fifa-2018-match-statistics)_

## Quickstart
Requires Python3. Currently, only CSV files are supported. <br>
The dataset parsing and correlation calculation is all done via `pandas`.

`pip install corella`

## Usage

### Command Line

`corella` accepts CSV data either through STDIN or as an input file.

`cat file.csv | corella` or `corella --input file.csv`

### Supported CLI options

##### `--pos-color`
Set the color to use for positive correlation. Defaults to `light_red` <br>
Supported colors include `black, red, green, yellow, blue, magenta, cyan, white` and `light_gray, dark_gray, light_red, light_green, light_yellow, light_blue, light_magenta, light_cyan`. <br>
Full list of all 256 supported colors can be found at the [colorama project page](https://pypi.org/project/colored/).

##### `--neg-color`
Set the color to use for negative correlation. Defaults to `light_blue` <br>

##### `--input`
Optional input CSV file. If specified, STDIN is ignored.

##### `--delimiter`
The delimiter for the CSV file. Defaults to `,`.

##### `--method`
The method to use for calculating the correlation coefficient. Defaults to `pearson`. <br>
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.corr.html

##### `--padding`
The character padding to use on the left of the plot. Defaults to `20`. If the length of a column name exceeds the specified padding, it is ignored.

##### `--no-header`
A flag to specify if the provided input does not have a header. Defaults to `False`. If specified, column numbers are used as names instead.

### Usage within Python
```python
from corella import Corella
C = Corella()
C.draw(pandas_df)
```
## License
MIT

## Thanks
[colorama](https://github.com/tartley/colorama)

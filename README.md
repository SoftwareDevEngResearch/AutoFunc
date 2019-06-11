# AutoFunc
Data Mining for Automated Functional Representations

[![Build Status](https://travis-ci.org/AlexMikes/AutoFunc.svg?branch=master)](https://travis-ci.org/AlexMikes/AutoFunc)

This package automatically generates functional representations for components based on the results of data mining a
design repository. It was developed for use with the Design Repository house at Oregon State University. A rudimentary 
web interface can be found here: http://ftest.mime.oregonstate.edu/repo/browse/

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install autofunc.

The package is not yet on PyPI, so it must be downloaded from here as a .zip file: https://github.com/AlexMikes/AutoFunc

Once downloaded as a .zip file, install with:

```bash
pip install /path/to/file/AutoFunc-master.zip
```

## Usage

Example files are provided in the examples folder. Autofunc will automate the functional representations of components
as  long as the format of the .csv file is has the component in column 1 and the function-flow in column 2


This is the ```example_get_func_rep.py``` file:

```python
from autofunc.simple_counter import count_stuff
from autofunc.get_func_rep import get_func_rep
from autofunc.get_top_results import get_top_results
from autofunc.write_results import write_results_from_dict
import os.path

""" Example showing how to automate functional representation using simple counting  """


# Dataset used for data mining
script_dir = os.path.dirname(__file__)
file1 = os.path.join(script_dir, '../assets/bladeCombined.csv')

comb_sort = count_stuff(file1)

# Use a threshold to get the top XX% of confidence values
threshold = 0.5
thresh_results = get_top_results(comb_sort, threshold)

# Use a known product for verification
input_file = os.path.join(script_dir, '../assets/InputExample.csv')

# Get dictionary of functions and flows for each component based on data mining
results, unmatched = get_func_rep(thresh_results, input_file, True)


# Optional write to file - uncomment and rename to write file
write_results_from_dict(results, 'test1.csv')
```


Run from within examples folder:

```bash
python example_get_func_rep
```

And it will generate a file ```test1.csv``` with the results of the autonmated functional representation based on 
the example data in the ```assets``` folder.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
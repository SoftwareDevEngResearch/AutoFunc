
"""

Use psycopg2 to connect to the design repository database and query the desired tables into Python data structures

OR

Import csv queries into Python data structures

"""

import pandas as pd
import os


def get_data(file):

    """ Returns pandas data frame and list of csv file"""

    # Read in dataset
    store_data = pd.read_csv(os.path.expanduser(file), header=None)
    store_data.head()

    # Convert dataset to a list
    records = []

    for i in range(len(store_data)):
        records.append([str(store_data.values[i, j]) for j in range(len(store_data.columns))])

    return store_data, records


# if __name__ == "__main__":




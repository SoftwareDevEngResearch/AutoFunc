
from get_data import get_data

"""

Use association rule finding algorithms (apriori, eclat, etc.) to find associations between component,
function, and flow in the repository data.

"""

def count_stuff():

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../assets/bladeQueryClean.csv')

    store_data, records = get_data(file)

    comps = {}

    comp =

    if comp not in comps:

        # if i == sys.argv[1]:
        #     set1.add(word)
        # if i == sys.argv[2]:
        #     set2.add(word)

        # counting[looper] += 1

        comps[comp] = 1
    else:
        # repeating[looper] += 1
        comps[comp] += 1

# if __name__ == "__main__":
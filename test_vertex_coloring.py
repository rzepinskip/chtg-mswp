from mswp.utils import read_graph_dimacs_format, draw_graph
from mswp.algo import MSWPAlgo
from os import listdir, system
from os.path import isfile, join


data_dir = './data/'
passed = 0
count = 0

dimacs_files = [join(data_dir, f) for f in listdir(data_dir) if isfile(join(data_dir, f))]

for f in dimacs_files:
    G, expected_solution = read_graph_dimacs_format(f)
    algo = MSWPAlgo(G)
    result = algo.mswp()
    if algo.mswp() == expected_solution:
        passed += 1
    count += 1
    print('PASSED {0}/{1}'.format(passed, count))
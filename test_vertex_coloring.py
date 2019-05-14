from mswp.utils import read_graph_dimacs_format, add_weights, draw_graph
from mswp.algo import MSWPAlgo
from os import listdir, system
from os.path import isfile, join


data_dir = './data/'
passed = 0
count = 0

# dimacs_files = [join(data_dir, f) for f in listdir(data_dir) if isfile(join(data_dir, f))]
dimacs_files = ['./data/myciel{0}.col'.format(it) for it in range(4, 8)]

for f in dimacs_files:
    print(f)
    G, expected_solution = read_graph_dimacs_format(f)
    add_weights(G, 1)
    # draw_graph(G)
    algo = MSWPAlgo(G)
    if algo.mswp() == expected_solution:
        passed += 1
    count += 1
    #system('cls')
    print('PASSED {0}/{1}'.format(passed, count))
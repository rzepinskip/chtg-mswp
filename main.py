import click
from mswp.utils import get_sample_graph, draw_graph, draw_bipartite_graph
from mswp.algo import MSWPAlgo, reconstruct_coloring


@click.command()
def main():
    G = get_sample_graph()
    print(MSWPAlgo(G).mswp())
    coloring = reconstruct_coloring(G)
    print(coloring)
    draw_bipartite_graph(G, coloring)


if __name__ == "__main__":
    main()

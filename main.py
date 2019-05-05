import click
from mswp.utils import get_sample_graph, draw_graph, draw_bipartite_graph
from mswp.mswp import mswp


@click.command()
def main():
    G = get_sample_graph()
    # draw_bipartite_graph(G)
    mswp(G)


if __name__ == "__main__":
    main()

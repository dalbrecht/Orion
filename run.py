from bottle import route, run, static_file
import os
import igraph


@route('/')
def orion():

    constellation = igraph.Graph()
    constellation.add_vertices(8)
    # draw outline of body
    constellation.add_edges([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])
    # draw belt
    constellation.add_edges([(3, 6), (6, 7), (7, 5)])

    layout = constellation.layout("kamada_kawai")

    igraph.plot(constellation, target="img.png", layout=layout)
    return static_file("img.png", os.getcwd())

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)


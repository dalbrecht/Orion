from bottle import route, run, response

import igraph
import cairo
from tempfile import NamedTemporaryFile

@route('/')
def orion():

    constellation = igraph.Graph()
    constellation.add_vertices(8)
    # draw outline of body
    constellation.add_edges([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])
    # draw belt
    constellation.add_edges([(3, 6), (6, 7), (7, 5)])

    layout = constellation.layout("kamada_kawai")

    tempFileObj = NamedTemporaryFile(mode='w+b', suffix='svg')
    renderSurface = cairo.SVGSurface(tempFileObj, 480, 640)
    renderContext = cairo.Context(renderSurface)

    constellation.plot(renderContext)

    constellation.plot(layout=layout)
    response.content_type = "image/svg+xml"
    return tempFileObj

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)


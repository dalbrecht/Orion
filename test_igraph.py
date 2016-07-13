import igraph.test


def test_igraph():
    assert igraph.test.run_tests(verbosity=255) is None


import igraph.test


def test_igraph():
    assert igraph.test.run_tests(verbosity=255) is None

if __name__ == "__main__":
    print("No tests were executed.  Did you mean to use nose or pytest?")
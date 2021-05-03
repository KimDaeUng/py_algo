def testcase():
    yield '6 11'
    yield '1'
    yield '1 2 2'
    yield '1 3 5'
    yield '1 4 1'
    yield '2 3 3'
    yield '2 4 2'
    yield '3 2 3'
    yield '3 6 5'
    yield '4 3 3'
    yield '4 5 1'
    yield '5 3 1'
    yield '5 6 2'

G = testcase()

def input():
    return next(G)
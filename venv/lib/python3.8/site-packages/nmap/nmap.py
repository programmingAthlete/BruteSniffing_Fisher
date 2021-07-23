def nmap(a, b, c, d, curvefn=None, normfn=None):
    """
    Returns a function that maps a number n from range (a, b) onto a range
    (x, y). If no curvefn is given, linear mapping will be used. Optionally a
    normalisation function normfn can be provided to transform output.
    """
    if not curvefn:
        curvefn = lambda x: x

    def map(n):
        r = 1.0 * (n - a) / (b - a)
        out = curvefn(r) * (d - c) + c
        if not normfn:
            return out
        return normfn(out)
    return map


if __name__ == '__main__':
    mapfn = nmap(0, 100, 500, 1000)
    assert mapfn(0) == 500
    assert mapfn(100) == 1000
    assert mapfn(50) == 750
    print('done')

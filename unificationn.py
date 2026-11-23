def unify(x, y, subs=None):
    if subs is None:
        subs = {}

    if x == y:
        return subs

    if isinstance(x, str) and x in ['x', 'y']:
        subs[x] = y
        return subs

    if isinstance(y, str) and y in ['x', 'y']:
        subs[y] = x
        return subs

    if isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0] or len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):
            subs = unify(a, b, subs)
            if subs is None:
                return None
        return subs

    return None


# Example
expr1 = ('Knows', 'x', 'John')
expr2 = ('Knows', 'Mary', 'y')

print("Unifier:", unify(expr1, expr2))
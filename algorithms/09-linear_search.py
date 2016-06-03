def linear_search(L, query):
    for item in L:
        if item == query:
            return True

        # only for sorted lists:
        if item > query:
            return False

    return False
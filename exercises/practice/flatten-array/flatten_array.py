def flatten(iterable):
    """
    Take a nested list and return a single flattened list with all values except None.

    :param iterable: A list potentially containing nested lists and None values.
    :return: A flattened list with all None values removed.
    """
    flattened_list = []

    def _flatten(sub_iterable):
        for item in sub_iterable:
            if isinstance(item, list):
                _flatten(item)
            elif item is not None:
                flattened_list.append(item)

    _flatten(iterable)
    return flattened_list

def handle_error_by_throwing_exception():
    raise RuntimeError("An error occurred")


def handle_error_by_returning_none(input_data):
    try:
        # Convert input_data to integer and return
        return int(input_data)
    except Exception:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        # Convert input_data to integer and return a successful tuple
        result = int(input_data)
        return (True, result)
    except Exception:
        return (False, None)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.open()
        filelike_object.do_something()
    except Exception as e:
        filelike_object.close()
        raise e
    else:
        filelike_object.close()

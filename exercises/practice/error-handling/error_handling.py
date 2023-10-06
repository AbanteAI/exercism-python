def handle_error_by_throwing_exception():
    raise Exception("An error occurred")


def handle_error_by_returning_none(input_data):
    return None


def handle_error_by_returning_tuple(input_data):
    return (True, None)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.do_something()
    finally:
        filelike_object.close()
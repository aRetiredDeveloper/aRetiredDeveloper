import functools


def generic_response(func=None, status=400, success=200):
    if func is None:
        return functools.partial(generic_response, status, success)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        status_code = status
        response = func(*args, **kwargs)
        print('============YESSSSSSSSSSSS+===============')
        print(response)
        if response.success:
            status_code = success
        print("=====updated=====")
        print(response)
        return response, status_code
    return wrapper
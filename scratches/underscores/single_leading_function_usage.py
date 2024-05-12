if __name__ == '__main__':
    from single_leading_function import *  # Avoid using wildcard imports

    external_func()
    _internal_func()  # This will raise a NameError


if __name__ == '__main__':
    import single_leading_function

    single_leading_function.external_func()
    single_leading_function._internal_func()  # This will not raise a NameError

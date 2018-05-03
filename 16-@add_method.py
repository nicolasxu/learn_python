@add_method

customize python decorator


def add_method(cls, name=None):
    """Decorator which adds a method to the specified class.

    @param cls the class which will have a method added to it
    @param name optional name of the method added to the class
    @return a decorator which adds a method to the specified class
    """
    def fn(method):
        setattr(cls, name or method.__name__, method)
    return fn



# usage
@add_method(models.User, 'health_report')
def generate_health_report(self):
	# ...
	pass



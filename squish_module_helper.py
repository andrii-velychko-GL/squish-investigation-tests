import inspect
import sys

# For more information see:
# https://kb.froglogic.com/display/KB/Article+-+Using+Squish+functions+in+your+own+Python+modules+or+packages#Article-UsingSquishfunctionsinyourownPythonmodulesorpackages-Solution%232%22Custom%22importofcurrentfunctionsandmembers

def import_squish_symbols(to_be_decorated=None):
    # For use as a decorator:
    if to_be_decorated is not None:
        def wrapper():
            __import_squish(sys.modules[to_be_decorated.__module__])
            to_be_decorated()
        return wrapper

    # For regular use like a normal function:
    __import_squish(sys.modules[inspect.getmodulename(inspect.stack()[1][1])])

def __import_squish(import_into_module):
    import test
    from squish import applicationContextList

    if len(applicationContextList()) == 0:
        test.fixateResultContext(2)
        test.warning("No application context. Some functions from the 'squish' module won't be available.")
        test.restoreResultContext()
    import_into_module.__dict__.update(sys.modules["squish"].__dict__)
    setattr(import_into_module, "test", sys.modules["test"])
    setattr(import_into_module, "testData", sys.modules["testData"])
    setattr(import_into_module, "object", sys.modules["object"])
    setattr(import_into_module, "objectMap", sys.modules["objectMap"])
    setattr(import_into_module, "squishinfo", sys.modules["squishinfo"])

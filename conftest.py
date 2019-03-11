import sys, os

print("""Adding "src" to Current path """.format(os.path.join(os.path.dirname(__file__))))
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


def pytest_sessionstart(session):
    """ before session.main() is called. """
    pass


def pytest_sessionfinish(session, exitstatus):
    """ whole test run finishes. """
    pass


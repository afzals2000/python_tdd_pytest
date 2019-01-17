import sys, os

print("""Adding "src" to Current path """.format(os.path.join(os.path.dirname(__file__))))
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

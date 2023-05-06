# import printing_functions
# import printing_functions as pf
from printing_functions import print_models as pm, show_completed_models as scm

if __name__ == '__main__':
    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    pm(unprinted_designs, completed_models)
    scm(completed_models)

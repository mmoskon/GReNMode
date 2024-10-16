import numpy as np

# if param is iterable with two elements, a value from a distribution is used
def get_param_value(param, dist = 'uniform'):
    # if single value is specified
    if type(param) == float or type(param) == int:
        return param
    
    # if two values are specific generate a value from a uniform distribution
    if len(param) == 2 and dist == 'uniform':
        return np.random.uniform(param[0], param[1])
    
    if len(param) == 2 and dist == 'normal':
        while True:
            val = np.random.normal(param[0], param[1])
            if val > 0:
                return val
    
    print ("Invalid option!")
    return 0
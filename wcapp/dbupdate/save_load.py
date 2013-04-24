'''
Saves and loads data in different formats
'''

import pickle

def pickle_save (output, data):
    print 'saving in pickle', output
    f = open(output, "wb")
    try:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL) 
    except EnvironmentError as er:
        print("save error: " + er)
    finally:
        f.close();
    print 'saving complete'
    
    
def pickle_load (input):
    try:
        f = open (input, "rb")
        data = pickle.load(f)
    except (EnvironmentError, pickle.UnpicklingError) as er:
        print("load error: {0}".format(er))
    finally:
        f.close();  
    return data
import numpy as np

def read_ecuation_system():
    '''This reads the ecuation system and returns two numpy arrays: a with the coefficients and b with
    the corresponding vector result'''
    new_coef=[]
    new_result=[]
    while True:
        ecuation= input("Please enter the coefficients of the ecuation and the result in order \
        sepparated by comma. Example: 2x+y+0z = 1 has to be entered as 2, 1, 0, 1\
         (Or press Enter to quit)")
        if not ecuation:
            break
        else:
            ecuation= ecuation.split(',')
            try:
                x= [float(x) for x in ecuation[:-1]]
            except ValueError:
                print(f"Error converting 1 or more coefficients to float")
                continue
            try:
                res= float(ecuation[-1])

            except ValueError:
                print(f"Error converting '{res}' to float")
                continue




            new_coef.append(x)
            new_result.append(res)




    a=np.array(new_coef)
    b=np.array(new_result)
    return a, b



def calculator (a,b):
    '''a is a numpy array that contains the coefficients for theunknowns of the system of equations
    b es el numpy array that contains the results vector
    This returns the values of the unknowns'''
    return np.linalg.solve(a, b)





if __name__ == "__main__":
    a, b=read_ecuation_system()
    x= calculator(a, b)
    print(x)

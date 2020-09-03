import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = []
    
   
    
    for x in range(100):
        if (x % 3 == 0):
            
            temp = pow(x,2)
            return_value.append(temp)

    return return_value    
   
    
if __name__ == "__main__":
        for x in squared_threes():
            print(x)

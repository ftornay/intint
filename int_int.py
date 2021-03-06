#!/usr/bin/env python
def steps(min, max, n):
    """ Function that interpolates values of a variable
    linearly between (min, max) in a number of steps (n)
    it uses a variation of Bresenham's algorithm taken from:
    http://www.pyaray.com/articles/lines.htm
    """
    assert max > min
    assert n > 1
    deltay = max - min
    deltax = n - 1
    if deltax >= deltay:
        return stepsX(min, max, n) # Iterate over X (steps)
    else:
        return stepsY(min, max, n) # Iterate over Y (variable values)

def stepsY(min, max, n):
    """ Function that interpolates values _assuming_ that the variation
    in the values is _larger_ than the number of steps
    See function steps for more details """
    deltay = max - min
    deltax = n - 1
    deltaerr = 0 # variable for figuring out when
                # to increment the other axis
    
    results = [min] # list to accumulate the values
    x = 1
    for y in range(min, max+1): # y changes faster so iterate on it
        deltaerr += deltax
        if deltaerr >= deltay: # If enough increases in the variable (y steps)
            x += 1              # then move to the next x step
            deltaerr -= deltay # Reset deltaerr in deltay units
                                # so that we keep the changes
                                # proportional to deltax/deltay (the slope)
            results.append(y+1) # At the next iteration,
                                # we'll be at a new x step,
                                # save the y level for it
    return results

def stepsX(min, max, n):
    """ Function that interpolates values _assuming_ that the variation
    in the values is _smaller_ than the number of steps
    See function steps for more details """
    deltay = max - min
    deltax = n - 1
    deltaerr = 0 # variable for figuring out when
                # to increment the other axis
    
    results = [] # list to accumulate the values
    y = min
    for x in range(1, n+1): # x changes faster so iterate on it
        results.append(y)
        deltaerr += deltay
        if deltaerr >= deltax: # If enough increases in the steps
            y += 1              # then move to the next y value
            deltaerr -= deltax # Reset deltaerr in deltax units
                                # so that we keep the changes
                                # proportional to deltay/deltax (the slope)
    return results

if __name__ == "__main__":
    l = steps(235, 273, 12)
    print(l)
    l = steps(23, 27, 12)
    print(l)

#!/usr/bin/env python
def steps(min, max, n):
    """ Function that interpolates values of a variable
    linearly between (min, max) in a number of steps (n)
    it uses the "integer line algorithm", simpler than Bresenham's
    The algorithm was taken from: http://www.pyaray.com/articles/lines.htm
    This version assumes that
    the to-be-interpolated variable (y)
    varies _more_than the number of steps (x)"""

    deltay = max - min
    deltax = n - 1
    assert deltay >= deltax # Check that y varies more widely
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

if __name__ == "__main__":
    l = steps(235, 273, 12)
    print(l)

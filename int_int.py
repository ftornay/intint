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
    stepVal = 0 # variable for figuring out when
                # to increment the other axis
    
    results = [min] # list to accumulate the values
    x = min
    for y in range(min, max+1):
        stepVal += deltax   # Everytime we _don't_ increase x
                            # we incur in an error proportional to deltax
        if stepVal >= deltay: # Is our error larger than deltay?
            x += 1 # Then move to the next step
            stepVal -= deltay # By increasing x, we lower our error
            results.append(y+1) # At the next iteration,
                                # we'll be at a new step, save the level for it
    return results

if __name__ == "__main__":
    l = steps(235, 273, 12)
    print(l)

This is a function that interpolates a variable from a minimum to a maximum value in a series of n "steps"

The function "steps" returns a list with n elements, each giving a level
of the variable from the min to the max with intermediate levels that
vary as closely to linear as possible.

It is based on a line drawing algorithm similar to Bresenham's.

taken from http://www.pyaray.com/articles/lines.htm

Both python and matlab implementations are included

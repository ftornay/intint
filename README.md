This is a function that interpolates a variable in a series of "steps"
That is, we've got a minimum and a maximum of a variable
and we want to distribute its variation in a series of steps
The function (steps) returns a list with n elements, each giving a level
of the variable from the min to the max with intermediate levels that
vary as closely to linear as possible
It is based on a line drawing algorithm similar to Bresenham's
taken from http://www.pyaray.com/articles/lines.htm
Boty python and matlab implementations are included

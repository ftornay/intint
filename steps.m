% This function linearly interpolates values between min and max in n "steps"
% It is based on a line drawing algorithm presented in
% http://www.pyaray.com/articles/lines.htm
function results = steps(min, max, n)
    deltay = max - min;
    deltax = n - 1;
    if (deltay <= deltax)
        results = stepsX(min, max, n);
    else
        results = stepsY(min, max, n);
    end
end

% Function that iterates over y
function results = stepsY(min, max, n)
    deltay = max - min;
    deltax = n - 1;
    deltaerr = 0;
    results = 1:n;
    results(1) = min;
    x = 1;
    for y = min:max
        deltaerr = deltaerr + deltax;
        if (deltaerr >= deltay)
            x = x + 1;
            deltaerr = deltaerr - deltay;
            next_y = y + 1;
            results(x) = next_y;
        end
    end
end

% Function that iterates over x
function results = stepsX(min, max, n)
    deltay = max - min;
    deltax = n - 1;
    deltaerr = 0;
    results = 1:n;
    y = min
    for x = 1:n
        cur_x = x;
        results(cur_x) = y;
        deltaerr = deltaerr + deltay;
        if (deltaerr >= deltax)
            y = y + 1;
            deltaerr = deltaerr - deltax;
        end
    end
end


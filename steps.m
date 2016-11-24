function results = steps(min, max, n)
    deltay = max - min;
    deltax = n - 1;
    deltaerr = 0;
    results = 1:n;
    results(1) = min;
    x = 1;
    for y = min:max
        deltaerr += deltax;
        if (deltaerr >= deltay)
            x += 1;
            deltaerr -= deltay;
            results(x) = y + 1;
        end
    end
end


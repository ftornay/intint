function results = stepsx10(min, max, n)
    results = steps(min*10, max*10, n);
    results = round(results/10);
end

function results = steps(min, max, n)
    deltay = max - min;
    deltax = n - 1;
    deltaerr = 0;
    results = 1:n;
    results(1) = min;
    x = 1;
    for y = min:max
        deltaerr = deltaerr + deltax;
        if (deltaerr >= deltay)
            x += 1;
            deltaerr = deltaerr - deltay;
            next_y = y + 1;
            results(x) = next_y;
        end
    end
end


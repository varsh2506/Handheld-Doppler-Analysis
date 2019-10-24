function n = normalise(d)

    m = mean(d);
    maxd = max(abs(d));
    n = (d-m)./maxd;

end
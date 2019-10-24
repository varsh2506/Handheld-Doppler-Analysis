function [upperenv lowerenv] = envelope(sig, method)
if nargin == 1 
    method = 'linear';
end
upperind = find(diff(sign(diff(sig))) < 0) + 1;
lowerind = find(diff(sign(diff(sig))) > 0) + 1;
f = 1;
l = length(sig);
try
    upperind = [f upperind l];
    lowerind = [f lowerind l];
catch 
    upperind = [f; upperind; l];
    lowerind = [f; lowerind; l];
end
xi = f : l;
upperenv = interp1(upperind, sig(upperind), xi, method, 'extrap');
lowerenv = interp1(lowerind, sig(lowerind), xi, method, 'extrap');

end
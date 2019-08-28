function [coef,totalEnergy] = DiameterCoeff(data, fs)

ft = fft(data);
N = length(ft);
df = fs/N;
f = 0:df:fs-df;
fmax = fs/2;

window = 1000;
num_window = floor(fmax/window);
coef = [];
totalEnergy = 0;

for i = 1:num_window
    fft_window = ft((i)*window:((i+1)*window)-1);
    energy = sum(abs(fft_window).*abs(fft_window));
    totalEnergy = totalEnergy + energy;
    coef(i) = energy;
end

end
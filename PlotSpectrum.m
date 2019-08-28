function PlotSpectrum(data,fs,range)

ft = fft(data);
N = length(ft);
df = fs/N;
f = 0:df:fs-df;

figure;
plot(f,abs(ft));
xlim(range);
xlabel('Frequency in Hertz');
ylabel('Magnitude');
title('Frequency Spectrum');

end

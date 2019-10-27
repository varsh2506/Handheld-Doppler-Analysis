clear all;
[y, fs] = audioread('filename.wav');
figure(1);
plot(y);
window_size = 0.04*44100;
window = hann(window_size); 
iter = floor(length(y)/window_size);
y_new = y(1:iter*window_size);
y_padded = [zeros(window_size,1); y_new; zeros(window_size,1)];
for i = 1:iter  % will skip the last frame, intentionally
    seg (:,i) = (y_padded((i-1)*window_size+1:i*window_size+window_size)).*window_size;
end
seg_fft = fft(seg,fs);
for i = 1:iter
    thresh_vector(i) = sum(abs(seg_fft(1:fs/2,i)))/5000;
end
thresh = max(thresh_vector);
for i = 1:iter
    max_freq_vector(i) = max([1; find(abs(seg_fft(1:fs/2,i))>=thresh)]); 
end
max_freq = max(max_freq_vector) 



function [max_freq, avg_freq] = maximum_frequency(data, best_beats_indices, fs)
k=1;
    for i=1:2:10
        beat = data(best_beats_indices(i):best_beats_indices(i+1));
        max_freq_vector(k) = PeakVelocity(beat, fs);
    end
    max_freq = max(max_freq_vector);
    avg_freq = sum(max_freq_vector)/5;
end
function [heart_rate, avg_freq, max_freq, best_beat_indices] = find_parameters(data, fs)
    [beats, index, diff_indices, best_beat] = beat_ind(data, fs);
    best_beat_indices = best_five_beats(data, best_beat);
    [max_freq, avg_freq] = maximum_frequency(data, best_beat_indices, fs);
    heart_rate = ExtractPeriod(data, fs);
end
function [heart_rate, avg_freq, max_freq, best_beat_indices, vector, best_energy, avg_energy] = find_parameters(data, fs)
    
    [beats, index, diff_indices, best_beat] = beat_ind(data, fs);
    [best_beat_indices, best_energy] = best_five_beats(data, best_beat);
    avg_energy = mean(best_energy);
    [max_freq, avg_freq, vector] = maximum_frequency(data, best_beat_indices, fs);
    Period = ExtractPeriod(data, fs);
    heart_rate = (fs/Period)*60;
    
end
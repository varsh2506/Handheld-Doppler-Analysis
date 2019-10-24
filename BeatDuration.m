function beats = BeatDuration(data, fs)

    window_length = 0.010*fs;
    beats = zeros(size(data));
    data = normalise(data);
    thresh = 0.04;
    for i =1:window_length:(floor(length(data)/window_length)*window_length-window_length)
        window = data(i:i+window_length-1);
        var_win = max(window)-min(window);
        
        if(var_win > thresh)
            beats(i:i+window_length-1) = 1;
        else 
            beats(i:i+window_length-1) = 0;
        end
    end
end
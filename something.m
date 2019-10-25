function [beats,index,diff_indices,best_beat] = something(data, fs)

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
    k=1;
    for j=1:length(beats)
        if(j~=1 && (beats(j)+beats(j-1)==1))
            index(k)=j;
            k=k+1;
        end
    end
    k=1;
    for j=1:2:length(index)
        diff_indices(k)=index(j+1)-index(j);
        k=k+1;
    end
    threshold=mean(diff_indices);
    k=1;
    for j=1:2:length(index)
        if((index(j+1)-index(j))>=threshold)
            best_beat(k)=index(j);
            best_beat(k+1)=index(j+1);
            k=k+2;
        end
    end
end
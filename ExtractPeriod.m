function HeartRate = ExtractPeriod(data,fs)

    len = length(data);
    
    %Defining max and min period
    maxBPM = 100;
    minBPM = 50;
    maxf = maxBPM/60;
    minf = minBPM/60;
    minPeriod = floor(fs/maxf);
    maxPeriod = ceil(fs/minf);
    
    %Taking 4 seconds of data for analysis
    DataSlice = data(1:floor(len/4));
    
    %Finding autocorrelation
    [a,lags] = xcorr(DataSlice, maxPeriod + 1, 'coef');
    aPoslag = a(maxPeriod: length(a));

    %Finding the Peak 
    [pks, locs] = findpeaks(aPoslag, 'MinPeakDistance', minPeriod);
    [centerp,indcenter] = max(pks);
    pks(indcenter) =[];
    locs(indcenter) = [];
    [Peak, index] = max(pks);
    
    
    HeartRate = locs(index);
    
end

%file = fopen('filenames.csv');
%array = textscan(file,'%s');
%fclose(file);
len = length(array);
HR = [];
Favg = [];
Fmax = [];
Energy = [];

for i = 1:len
    name = strcat('HandheldRecorded\',array{i},'.wav');
    [data, fs] = audioread(name);
    if(i == 22 || i == 39 || i == 50 || i == 52 || i == 62 || i == 64 || i == 74 || i == 73 || i == 74 || i == 75 || i == 76 |i == 77)
        heart_rate = 0;
        avg_freq = 0;
        max_freq = 0;
        avgEnergy =0;
    else
        [heart_rate, avg_freq, max_freq, ind, vec, energyArray, avgEnergy] = find_parameters(data,fs);
    end
    
    HR = [HR; heart_rate];
    Favg = [Favg; avg_freq];
    Fmax = [Fmax; max_freq];
    Energy = [Energy; avgEnergy];
    i
end


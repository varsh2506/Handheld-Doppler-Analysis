function [max_array,min_array,range_array,mean_array]=analyze(data,fs,x,y)
beat=data(x:y);
plot(beat);
[s,w,t]=spectrogram(beat,512,256,1024,fs,'yaxis');
s=abs(s);
s=s.^2;
s=10*log10(s);
s=normalize(s,'range',[-150,-30]);
[len,wid]=size(s);
freq=zeros(len,wid);
for c=1:wid
    for b=1:len
        if(s(b,c)>=-65)
            freq(b,c)=w(b);
        end
    end
 f=freq;
max_array(c)=max(freq(:,c));
temp=freq(:,c);
min_array(c)=min(temp(temp>0));
range_array(c)=max_array(c)-min_array(c);
mean_array(c)=mean(temp(temp>0));
end
end

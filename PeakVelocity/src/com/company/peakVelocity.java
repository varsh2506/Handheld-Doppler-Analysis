package com.company;

import com.company.wavexception.WavFileException;
import com.company.wavfile.WavFile;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

import org.jtransforms.fft.DoubleFFT_1D;

public class peakVelocity {

    private double maxOf(double[] a){
        double max = 0;
        for(double i: a){
            if(i > max)
                max = i;
        }
        return max;
    }

    private int maxOf(Integer[] a){
        int max = 0;
        for(int i = 0; i<a.length; i++){
            try {
                int temp = a[i].intValue();
                if (temp > max)
                    max = temp;
            }
            catch (NullPointerException e){
                System.out.println(i);
            }
        }
        return max;
    }

    private int maxOf(int[] a){
        int max = 0;
        for(int i = 0; i<a.length; i++) {
            if (i > max)
                max = i;
        }
        return max;
    }

    public int findMaxFrequency(double[] data, double fs){
        int len = data.length;
        int window_size = (int) (0.04*44100);
        int iter = (int) Math.floor(len/window_size);

        double[] padding = new double[window_size];
        Arrays.fill(padding,0);

        int len_padded = 2*window_size + len;
        double[] data_padded = new double[len_padded];
        System.arraycopy(padding,0,data_padded,0, window_size);
        System.arraycopy(data,0,data_padded, window_size,len );
        System.arraycopy(padding,0,data_padded,len+window_size, window_size);

        //double[][] seg_fft = new double[iter][2*window_size];
        double[] seg;
        double[] thresholdVector = new double[iter];
        double[][] halfFFT = new double[iter][(int) fs/2 + 1];
        for(int i=1;i<iter;i=i+1) {
            seg = Arrays.copyOfRange(data_padded,(i-1)*window_size + 1, i*window_size + window_size);
            for(int j = 0; j<seg.length; j++) {
                seg[j] = seg[j] * window_size;
            }
            //Object to perform fft
            DoubleFFT_1D fftDo = new DoubleFFT_1D(seg.length);
            double[] fft = new double[seg.length * 2];
            System.arraycopy(seg, 0, fft, 0, seg.length);
            fftDo.realForwardFull(fft);

            halfFFT[i] = Arrays.copyOfRange(fft,0,(int) fs/2);
            double sum = 0;
            for(double j:halfFFT[i]){
                sum = sum + Math.abs(j);
            }
            thresholdVector[i] = sum/5000;
        }

        double threshold = maxOf(thresholdVector);
        int[] maxFreqArray = new int[iter];
        ArrayList<Integer> freq = new ArrayList<>();
        freq.add(1);

        for(int i =1; i<iter; i=i+1){
            for (int j = 0; j<halfFFT[i].length; j = j+1) {
                if(Math.abs(halfFFT[i][j])>threshold)
                    freq.add(j);
            }
            maxFreqArray[i]=maxOf(freq.toArray(new Integer[freq.size()]));
        }

        for (int i:
             maxFreqArray) {
             System.out.println(i);
        }
        return maxOf(maxFreqArray);

    }

    public static void main(String[] args) throws IOException, WavFileException {
        long startTime = System.nanoTime();// Open the wav file
        WavFile wavFile = WavFile.openWavFile(new File("/home/mehak/Handheld-Doppler-Analysis/HandheldRecorded/cw_anirudh_341.wav"));
        // Display information about the wav file
        //wavFile.display();
        //Get the number of frames in the wav file
        int numFrames = (int) wavFile.getNumFrames();

        // Create a buffer of num frames
        double[] data = new double[numFrames];
        //List<macrobase.datamodel.Datum> testCases = Arrays.asList(data)
        //Get sampling rate
        double fs = wavFile.getSampleRate();
        // Read frames into bufferArray
        wavFile.readFrames(data, numFrames);
        peakVelocity PV = new peakVelocity();
        int maxFreq = PV.findMaxFrequency(data,fs);
        System.out.println(maxFreq);

    }
}

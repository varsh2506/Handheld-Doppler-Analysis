package com.dimowner.audiorecorder.debug;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

import org.jtransforms.fft.DoubleFFT_1D;

public class PeakVelocity {

    private double maxOf(double[] a) {
        double max = 0;
        for (double i : a) {
            if (i > max)
                max = i;
        }
        return max;
    }

    private int maxOf(Integer[] a) {
        int max = 0;
        for (int i = 0; i < a.length; i++) {
            try {
                int temp = a[i].intValue();
                if (temp > max)
                    max = temp;
            } catch (NullPointerException e) {
                System.out.println(i);
            }
        }
        return max;
    }

    public int maxOf(int[] a) {
        int max = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] > max)
                max = a[i];
        }
        return max;
    }

    private double[] HanningWindow(double[] signal_in, int pos, int size) {
        double[] signal_out = new double[size];
        for (int i = pos; i < pos + size; i++) {
            int j = i - pos; // j = index into Hann window function
            signal_out[j] = (signal_in[i] * 0.5 * (1.0 - Math.cos(2.0 * Math.PI * j / size)));
        }
        return signal_out;
    }

    private double[] FFTConvert(double[] fft) {
        int len1 = fft.length;
        int len2 = len1 / 2;
        double[] real_ftt = new double[len2];

        real_ftt[0] = fft[0];
        real_ftt[len2 - 1] = fft[1];
        int k = 1;
        for (int i = 2; i < len1; i = i + 2) {
            real_ftt[k] = Math.hypot(fft[i], fft[i + 1]);
            k = k + 1;
        }


        return real_ftt;

    }

    public int findMaxFrequency(double[] data, double fs) {
        //Defining window size and overlap
        int len = data.length;
        int window_size = (int) (0.04 * 44100);
        int overlap = (int) (0.02 * 44100);
        int iterations = (int) Math.ceil(((float) len - (float) window_size) / ((float) window_size - (float) overlap));

   /*   System.out.println("Window Size: ");
        System.out.println(len);
        System.out.println("Overlap: ");
        System.out.println(overlap);
        System.out.println("Iterations: ");
        System.out.println(iterations);
*/

        //Padding the Array of data
        double[] padding = new double[window_size];
        Arrays.fill(padding, 0);
        int len_padded = 2 * window_size + len;
        double[] data_padded = new double[len_padded];
        System.arraycopy(padding, 0, data_padded, 0, window_size);
        System.arraycopy(data, 0, data_padded, window_size, len);
        System.arraycopy(padding, 0, data_padded, len + window_size, window_size);

        //double[][] seg_fft = new double[iterations][2*window_size];
        double[] seg;
        double[] thresholdVector = new double[iterations];
        double[][] halfFFT = new double[iterations][(int) fs / 2 + 1];
        for (int i = 0; i < iterations; i = i + 1) {
            int pos = i * overlap;
            seg = HanningWindow(data_padded, pos, window_size);
            //  System.out.println(seg.length);

         /*   if(i==1) {
                for (double s : seg) {
                    System.out.println(s);
                }
            }*/
            //Object to perform fft
            DoubleFFT_1D fftDo = new DoubleFFT_1D((int) fs);
            double[] fft = new double[(int) fs];
            Arrays.fill(fft, 0);
            System.arraycopy(seg, 0, fft, 0, seg.length);
            fftDo.realForward(fft);

            //Taking the first half values of frequency
            //halfFFT[i] = Arrays.copyOfRange(fft,0,(int) fs/2);
            //double sum = 0;
            //System.out.println("FFT");
            //int k = 1;
            //for(double j:fft){
            //    if(i==1){
            //        System.out.println(j);
            //    }
            //    sum = (sum + Math.abs(j));
            //}
            double[] real_ftt = FFTConvert(fft);
            double sum = 0;

            for (int j = 0; j < real_ftt.length; j++) {
                sum = sum + real_ftt[j];
            }

            thresholdVector[i] = sum /2500;
            //System.out.println(i);
            //System.out.println(thresholdVector[i]);
            halfFFT[i] = real_ftt;
        }

        //System.out.println("Threshold:");
        double threshold = maxOf(thresholdVector);
        //System.out.println(threshold);


        int[] maxFreqArray = new int[iterations];
        ArrayList<Integer> freq = new ArrayList<>();
        freq.add(1);

        for (int i = 0; i < iterations; i = i + 1) {
            for (int j = 0; j < halfFFT[i].length; j = j + 1) {
                if (Math.abs(halfFFT[i][j]) > threshold)
                    freq.add(j);
            }
            maxFreqArray[i] = maxOf(freq.toArray(new Integer[freq.size()]));
        }

        /*for (int i:
                maxFreqArray) {
            System.out.println(i);
        }*/
        return maxOf(maxFreqArray);

    }

   /* public static void main(String[] args) throws IOException, WavFileException {
        long startTime = System.nanoTime();// Open the wav file
        WavFile wavFile = WavFile.openWavFile(new File("/Varshini_Data/G_DATA/ECE-Semester7/MajorProject/Handheld-Doppler-Analysis/HandheldRecorded/cw_adiveppa_4_19.wav"));
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
        PeakVelocity PV = new PeakVelocity();
        int maxFreq = PV.findMaxFrequency(data, fs);
        System.out.println(maxFreq);

    }*/
}

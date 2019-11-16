package com.company;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Main
{
    public static void main(String[] args)
    {

        try
        {
            long startTime = System.nanoTime();// Open the wav file
            phonecs.WavFile wavFile = phonecs.WavFile.openWavFile(new File("/home/kshama/Handheld-Doppler-Analysis/TryWav/HandheldRecorded/cw_adiveppa_4_19.wav"));

            // Display information about the wav file
            //wavFile.display();

            //Get the number of frames in the wav file
            int numFrames = (int) wavFile.getNumFrames();

            // Create a buffer of num frames
            double[] bufferArray = new double[numFrames];

            //Get sampling rate
            double sampleRate = wavFile.getSampleRate();

            // Read frames into bufferArray
            wavFile.readFrames(bufferArray, numFrames);
            //Signal processing algorithms

            double max = calculateMax(bufferArray);
            double mean = calculateMean(bufferArray);



            for(int i=0;i<numFrames;i++)
            {
                bufferArray[i]=(bufferArray[i]-mean)/max;
            }
            int window_length = (int) (0.010*sampleRate);
            int[] beats = new int[numFrames];
            double thresh = 0.04;
            double[] window = new double[window_length];
            double var_win;

            for(int j = 0; j< (numFrames/window_length) *window_length-window_length; j=j+window_length)
            {
                window=Arrays.copyOfRange(bufferArray,j,j+window_length);

                var_win=calculateMax(window) - calculateMin(window);


                if(var_win>thresh)
                {
                    for(int k=0;k<window_length;k++)
                        beats[j+k]=1;
                }
                else
                {
                    for(int k=0;k<window_length;k++)
                        beats[j+k]=0;
                }


            }
            int[] index = new int[256];
            int k=0;
            for(int j=0;j<beats.length;j++)
            {
                if(j!=0 && (beats[j]+beats[j-1]==1))
                {
                    index[k]=j;
                    k=k+1;
                }
            }
            k=0;
            int[] diff_indices = new int[256];
            for(int j=0;j<index.length;j=j+2)
            {
                diff_indices[k] = index[j + 1] - index[j];
                k = k + 1;
            }


            int threshold1 = Mean(diff_indices);
            int threshold2 = 2*threshold1;

            int duration;
            List<Integer> best_beat = new ArrayList<>();;
            for(int j=0;j<index.length;j++)
            {
                if(index[j]!=0)
                {

                    duration = index[j + 1] - index[j];
                    if (duration >= threshold1 && duration < threshold2) {
                        best_beat.add(index[j]);
                        best_beat.add(index[j + 1]);
                    }

                }
            }

            for(int i = 0; i < best_beat.size(); i++) {
                System.out.println(best_beat.get(i));
            }
            wavFile.close();

            System.out.print(best_beat.size());
        }
        catch (Exception e)
        {
            System.err.println(e);
        }
    }

    public static double calculateMax(double numArray[])
    {
        double max = Double.MIN_VALUE;
        for(int i=0; i < numArray.length ; i++)
        {
            if(Math.abs(numArray[i])>max)
                max=Math.abs(numArray[i]);
        }
        return max;

    }

    public static double calculateMean(double numArray[])
    {
        double sum=0.0;
        for(int i=0; i < numArray.length ; i++)
            sum = sum + numArray[i];
        //calculate average value
        double average = sum / numArray.length;
        return average;
    }
    public static double calculateMin(double numArray[])
    {
        double min = Double.MAX_VALUE;
        for(int i=0; i < numArray.length ; i++)
        {
            if(Math.abs(numArray[i])<min)
                min=Math.abs(numArray[i]);
        }
        return min;

    }
    public static int Mean(int numArray[])
    {
        int sum=0;
        int length =0;
        for(int i=0; i < numArray.length ; i++)
        {
            if(numArray[i]!=0)
            {
                sum = sum + numArray[i];
                length=length+1;
            }
        }
        //calculate average value

        int average =(int) sum /length;
        return average;
    }
}


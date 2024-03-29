package com.company;

import com.company.WavFile.WavFile;
import com.company.WavFileException.WavFileException;
import java.io.File;
import java.io.IOException;
import java.util.*;
import java.util.Arrays;




public class Try
{
    public static int findIndex(double arr[], double t)
    {

        // if array is Null
        if (arr == null) {
            return -1;
        }

        // find length of array
        int len = arr.length;
        int index = 0;

        // traverse in the array
        while (index < len) {

            // if the i-th element is t
            // then return the index
            if (arr[index] == t) {
                return index;
            }
            else {
                index = index + 1;
            }
        }
        return -1;
    }

    public static void main(String file_path) throws IOException,WavFileException
    {
        long startTime = System.nanoTime();// Open the wav file
        WavFile wavFile = WavFile.openWavFile(new File(file_path));

        // Display information about the wav file
        //wavFile.display();

        //Get the number of frames in the wav file
        int numFrames = (int) wavFile.getNumFrames();

        // Create a buffer of num frames
        double[] data = new double[numFrames];
        //Get sampling rate
        double fs = wavFile.getSampleRate();

        // Read frames into bufferArray
        wavFile.readFrames(data, numFrames);
        int len = data.length;
        //
        double max = calculateMax(data);
        double mean = calculateMean(data);



        for(int i=0;i<numFrames;i++)
        {
            data[i]=(data[i]-mean)/max;
        }
        int window_length = (int) (0.010*fs);
        int[] beats = new int[numFrames];
        double thresh = 0.04;
        double[] window = new double[window_length];
        double var_win;

        for(int j = 0; j< (numFrames/window_length) *window_length-window_length; j=j+window_length)
        {
            window=Arrays.copyOfRange(data,j,j+window_length);

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
        List<Integer> best_beats = new ArrayList<>();;
        for(int j=0;j<index.length;j++)
        {
            if(index[j]!=0)
            {

                duration = index[j + 1] - index[j];
                if (duration >= threshold1 && duration < threshold2) {
                    best_beats.add(index[j]);
                    best_beats.add(index[j + 1]);
                }

            }
        }
        int[] best_beat=new int[best_beats.size()];
        for(int i = 0; i < best_beats.size(); i++) {
            best_beat[i]=(best_beats.get(i));
        }

        k=0;
        double[] beat_energy = new double[best_beat.length/2]; int[] best_energy = new int[5]; int [] high_energy_indices = new int[10];
        for (int i=0; i<best_beat.length; i+=2)
        {
            double [] beat = Arrays.copyOfRange(data, best_beat[i], best_beat[i+1]);
            beat_energy[k]=0;
            for (int j=0; j<beat.length; j+=1)
            {
                beat_energy[k]+=beat[j]*beat[j];
            }
            k=k+1;
        }
        double [] beat_energy_copy = new double[beat_energy.length];
        System.arraycopy(beat_energy,0, beat_energy_copy, 0, beat_energy.length);
        Arrays.sort(beat_energy);
        //sort in descending order
        //Collections.reverse(Arrays.asList(beat_energy));
        for(int i=0; i<beat_energy.length/2; i++)
        {
            double temp = beat_energy[i];
            beat_energy[i] = beat_energy[beat_energy.length -i-1 ];
            beat_energy[beat_energy.length -i-1 ] = temp;
        }
        double [] beat_energy_5 = Arrays.copyOfRange(beat_energy, 0, 5);//sortedEnergy
        //System.out.printf("High energy beats\n");
        //for(int z=0;z<beat_energy_5.length;z++)
        //  System.out.printf("%f ",beat_energy_5[z]);
        k=0;
        double test;
        for( int i=0;i<beat_energy_5.length;i++)
        {
            best_energy[k] = findIndex(beat_energy_copy, beat_energy_5[i]); //finding the beat number
            k=k+1;
        }

        //System.out.printf("\nHigh energy indices\n");
        //for(int z=0;z<high_energy_indices.length;z++)
        //  System.out.printf("%d ",high_energy_indices[z]);

        wavFile.close();
        double [] energyPlusBeats = new double[11];
        energyPlusBeats[0] = beat_energy_5[0];
        k =1;
        for (int j = 0;j<best_energy.length;j++)
        {
            energyPlusBeats[k] = best_beat[(2*best_energy[j])];
            energyPlusBeats[k+1] = best_beat[2*best_energy[j]+1];
            k=k+2;
        }
        int[] indices = new int[10];
        for (int i=0;i<10;i++){
            indices[i] = (int)energyPlusBeats[i+1];
        }
        System.out.println(MaxFreq.freq("/Varshini_Data/G_DATA/ECE-Semester7/MajorProject/Handheld-Doppler-Analysis/HandheldRecorded/cw_adiveppa_4_19.wav",indices));


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

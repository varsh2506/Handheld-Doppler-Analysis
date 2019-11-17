package com.company;

import com.company.WavFileException;
import com.company.WavFile;
import java.io.File;
import java.io.IOException;
import java.util.*;
import java.util.Arrays;



class store{
    int []high_energy_in = new int[10] ;
    int [] best_energy = new int[20];
    public store(int[] high, int [] best_en)
    {
        this.high_energy_in = high;
        this.best_energy = best_en;
    }

}

public class Main
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
                System.out.printf("%d ",index);
                System.out.printf("%f ",arr[index]);
                return index;
            }
            else {
                index = index + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException,WavFileException
    {
        long startTime = System.nanoTime();// Open the wav file
        WavFile wavFile = WavFile.openWavFile(new File("C:\\Users\\admin\\Desktop\\WavFile\\cw_adiveppa_4_19.wav"));

        // Display information about the wav file
        wavFile.display();

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


        int k=0;
        int [] best_beat = {14566,16555,34500,37200,50500,52550};
        double[] beat_energy = new double[best_beat.length/2]; int[] best_energy = new int[5]; int [] high_energy_indices = new int[10];
        for (int i=0; i<best_beat.length; i+=2)
        {   //beat = new double [best_beat[i+1]-best_beat[i]];
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
        System.out.println("\n") ;
        Arrays.sort(beat_energy);
        //sort in descending order
        //Collections.reverse(Arrays.asList(beat_energy));
        for(int i=0; i<beat_energy.length/2; i++)
        {
            double temp = beat_energy[i];
            beat_energy[i] = beat_energy[beat_energy.length -i-1 ];
            beat_energy[beat_energy.length -i-1 ] = temp;
        }
        for(int z=0;z<beat_energy_copy.length;z++)
            System.out.printf("%f ",beat_energy_copy[z]);
        double [] beat_energy_5 = Arrays.copyOfRange(beat_energy, 0, 3);//sortedEnergy
        //System.out.println(beat_energy_5[1]);
        k=0;
        double test;
        for( int i=0;i<beat_energy_5.length;i++)
        {
            //System.out.printf("%f ",beat_energy_5[i]);
            best_energy[k] = findIndex(beat_energy_copy, beat_energy_5[i]); //finding the index of each beat
            k=k+1;
        }
        /*for(int z=0;z<best_energy.length;z++)
            System.out.printf("%d ",best_energy[z]);*/
        k=0;
        for (int j = 0;j<best_energy.length;j++)
        {
            high_energy_indices[k] = best_beat[(2*best_energy[j])];
            high_energy_indices[k+1] = best_beat[2*best_energy[j]+1];
            k=k+2;
        }
        //System.out.printf("%d %d\n", high_energy_indices[0],best_energy[0] );
        //return new store(high_energy_indices,best_energy);


    }
}

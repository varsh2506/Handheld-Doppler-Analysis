package com.company;

import java.io.File;
import java.io.IOException;

import static java.util.Arrays.copyOfRange;

import com.company.WavFileException.WavFileException;
import com.company.WavFile.WavFile;

public class MaxFreq {
    public static double freq(String file_path, int[] energyPlusBeats) throws IOException, WavFileException {
        long startTime = System.nanoTime();// Open the wav file
        WavFile wavFile = WavFile.openWavFile(new File(file_path));

        // Display information about the wav file
        //wavFile.display();

        //Get the number of frames in the wav file
        int numFrames = (int) wavFile.getNumFrames();

        // Create a buffer of num frames
        double[] data = new double[numFrames];
        //List<macrobase.datamodel.Datum> testCases = Arrays.asList(data)
        //Get sampling rate
        double fs = wavFile.getSampleRate();
        wavFile.readFrames(data, numFrames);

        int[] beat_max_freq = new int[5];
        peakVelocity PV = new peakVelocity();
        for (int i = 0; i < 10; i += 2) {
            double[] beat = copyOfRange(data, energyPlusBeats[i], energyPlusBeats[i + 1]);
            beat_max_freq[(int) (i / 2)] = PV.findMaxFrequency(beat, fs);

        }
        return PV.maxOf(beat_max_freq);


    }
}

package com.company;
import com.company.wavexception.WavFileException;
import com.company.wavfile.WavFile;
import macrobase.analysis.stats.Autocorrelation;

import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;


import static java.util.Arrays.*;


public class Main {
    public static int findPeaks(double[] autocorr, int minPeriod){
        int peaks = 0;
        for (int i=1; i<autocorr.length-1; i++){
            if (autocorr[i]>autocorr[i-1] && autocorr[i]>autocorr[i+1]&&i>=minPeriod){
                peaks = i;
                break;
            }
        }
        //System.out.print(autocorr[peaks]);
        return peaks;
    }

    public static void main(String[] args) throws IOException, WavFileException {
        long startTime = System.nanoTime();// Open the wav file
        WavFile wavFile = WavFile.openWavFile(new File("/Varshini_Data/G_DATA/ECE-Semester7/MajorProject/Handheld-Doppler-Analysis/HandheldRecorded/cw_anirudh_341.wav"));

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
        int len = data.length;
        int maxBPM = 100;
        int minBPM = 50;
        double maxf = maxBPM / 60.0;
        double minf = minBPM / 60.0;
        int minPeriod = (int) java.lang.Math.floor(fs / maxf);
        int maxPeriod = (int) java.lang.Math.ceil(fs / minf);

        Autocorrelation auto = new Autocorrelation(maxPeriod + 1);

        //System.out.print(autocorr[26460]);
        double[] DataSlice = copyOfRange(data, 0, (int) java.lang.Math.floor(len / 4));
        double[] autocorr = auto.evaluate(DataSlice);
        autocorr[0] = 1;
        int HeartRate = findPeaks(autocorr, minPeriod);
        System.out.print(HeartRate);
        //double[] aPoslag = Arrays.copyOfRange(autocorr, maxPeriod, autocorr.length);

    }

}

package com.dimowner.audiorecorder.debug;

import java.io.File;
import java.io.IOException;

import static java.util.Arrays.copyOfRange;

import com.dimowner.audiorecorder.debug.wavexception.WavFileException;
import com.dimowner.audiorecorder.debug.wavfile.WavFile;
import com.dimowner.audiorecorder.debug.stats.Autocorrelation;



public class HeartRate {
        public static int findPeaks(double[] autocorr, int minPeriod){
            int peak = 0;
            double peak_value = 0.0;
            for (int i=1; i<autocorr.length-1; i++){
                if (autocorr[i]>autocorr[i-1] && autocorr[i]>autocorr[i+1]&&i>=minPeriod){
                    if (autocorr[i]>peak_value) {
                        peak = i;
                        peak_value = autocorr[peak];
                    }
                }
            }
            return peak;
        }

        public static double main(String path) throws IOException, WavFileException {
            long startTime = System.nanoTime();// Open the wav file
            WavFile wavFile = WavFile.openWavFile(new File(path));

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
            int minPeriod = (int) Math.floor(fs / maxf);
            int maxPeriod = (int) Math.ceil(fs / minf);
            System.out.println(maxPeriod);
            Autocorrelation auto = new Autocorrelation(maxPeriod + 1);

            double[] DataSlice = copyOfRange(data, 0, (int) Math.floor(len / 4));
            double[] autocorr = auto.evaluate(DataSlice);
            autocorr[0] = 1;
            double HeartRate = 60/(findPeaks(autocorr, minPeriod)/fs);

            return HeartRate;
        }


    }



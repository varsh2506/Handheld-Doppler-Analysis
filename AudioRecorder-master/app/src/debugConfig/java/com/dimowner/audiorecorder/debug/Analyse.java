package com.dimowner.audiorecorder.debug;

import com.dimowner.audiorecorder.app.info.ActivityInformation;
import com.dimowner.audiorecorder.debug.HeartRate;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import com.dimowner.audiorecorder.R;
import com.dimowner.audiorecorder.debug.wavexception.WavFileException;

import java.io.IOException;

public abstract class Analyse extends AppCompatActivity {
    private TextView heart_rate;
    public void display_hr(String file_path) {
        //super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_analyse);
        heart_rate = findViewById(R.id.heart_rate);

        try {
            heart_rate.setText(Double.toString(HeartRate.main(file_path)));
        }
        catch(IOException e){
            System.out.println("IO Exception");
        }
        catch(WavFileException e){
            System.out.println("WavFileExeption");
        }
    }
    }
    /*private static final String KEY_LOCATION = "pref_location";

    public static Intent getStartIntent(Context context, String location) {
        Intent intent = new Intent(context, ActivityInformation.class);
        intent.putExtra(KEY_LOCATION, location);
        return intent;
    }*/


    //@Override
    /*protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_analyse);
        Bundle extras = getIntent().getExtras();

        TextView heart_rate = findViewById(R.id.heart_rate);

        if (extras != null) {
            if (extras.containsKey(KEY_LOCATION)) {
                try {
                    String path = extras.getString(KEY_LOCATION);
                    heart_rate.setText(Double.toString(HeartRate.main(path)));
                }
                catch(IOException e){
                    System.out.println("IO Exception");
                }
                catch(WavFileException e){
                    System.out.println("WavFileExeption");
                }
            }
        }
    }*/


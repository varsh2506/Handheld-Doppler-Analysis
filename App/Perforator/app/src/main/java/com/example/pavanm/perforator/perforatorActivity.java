package com.example.pavanm.perforator;

import android.content.Intent;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;



public class perforatorActivity extends AppCompatActivity {
    private static  String mRcordFilePath ;
    private Button computeVel;
    private Button recordWav;
    private Button bestWav;
    private TextView result;
    private TextView bestDisplay;
    int count = 1;
    double best_velocity;
    int best_record;
    @Override
    protected void onCreate(Bundle savedInstanceState) {


        super.onCreate(savedInstanceState);
       // View View = LayoutInflater.inflate(R.layout.activity_main, null);

        setContentView(R.layout.activity_main);


        recordWav = findViewById(R.id.record);
        recordWav.setText("RECORD" + count);
        recordWav.setOnClickListener(new View.OnClickListener() {
          @Override
           public void onClick(View v) {

                Intent launchIntent = getPackageManager().getLaunchIntentForPackage("com.kingbull.recorder");
                if (launchIntent != null) {
                   startActivity(launchIntent);//null pointer check in case package name was not found
              }



          }
       });

        computeVel = findViewById(R.id.button2);

        computeVel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mRcordFilePath = Environment.getExternalStorageDirectory() + "/recorded_audio.wav";
                double velocity = FindVelocity.findVel(mRcordFilePath,getApplicationContext());

                if(count==1)
                {
                    best_velocity = velocity;
                    best_record = count;
                }

                else
                {
                    if(velocity > best_velocity)
                    {
                        best_velocity = velocity;
                        best_record = count;
                    }
                }
                String vel = "VELOCITY = " +Double.toString(velocity);
                result = findViewById(R.id.textView3);
                result.setText(vel);

                count++;
                recordWav.setText("RECORD " + count);
                //Toast.makeText(perforatorActivity.this,mRcordFilePath, Toast.LENGTH_LONG).show();
            }
        });

        bestWav = findViewById(R.id.best);

        bestWav.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                bestDisplay = findViewById(R.id.textView4);
                String bestPerforator = "RECORD " + Double.toString(best_record) + ", Vel= " + Double.toString(best_velocity);
                bestDisplay.setText(bestPerforator);

            }
        });



    }
}

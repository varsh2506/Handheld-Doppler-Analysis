import java.io.*;
public class pepe {
  public static void main(String[] args) {
    int bytes, cursor, unsigned;
    try {
      FileInputStream s = new FileInputStream("cw_adiveppa_4_19.wav");
      BufferedInputStream b = new BufferedInputStream(s);
      byte[] data = new byte[128];
      b.skip(44);
      cursor = 0;
      while ((bytes = b.read(data)) > 0) {
        // do something
        for(int i=0; i<bytes; i++) {
                unsigned = data[i] & 0xFF; // Java..
                System.out.println(unsigned);
                cursor++;
        }
      }
      b.read(data);
      b.close();
    } catch(Exception e) {
      e.printStackTrace();
    }
  }
}

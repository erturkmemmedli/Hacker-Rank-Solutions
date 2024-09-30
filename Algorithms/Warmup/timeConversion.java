// Time Conversion


import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static String timeConversion(String s) {
        // Write your code here
        String[] time = s.split(":");
        String result;
        
        if (time[2].substring(2, 4).equals("AM")) {
            if (time[0].equals("12")) {
                result = "00" + ":" + time[1] + ":" + time[2].substring(0, 2);
                System.out.println(result);
            }  else {
                result = time[0] + ":" + time[1] + ":" + time[2].substring(0, 2);
                System.out.println(result);
            }
        } else {
            if (time[0].equals("12")) {
                result = "12" + ":" + time[1] + ":" + time[2].substring(0, 2);
                System.out.println(result);
            }  else {
                Integer hour = Integer.valueOf(time[0]) + 12;
                String hourStr = String.valueOf(hour);
                result = hourStr + ":" + time[1] + ":" + time[2].substring(0, 2);
                System.out.println(result);
            }
        }
        return result;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String result = Result.timeConversion(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

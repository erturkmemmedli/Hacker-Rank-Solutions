// Separate the Numbers


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
     * Complete the 'separateNumbers' function below.
     *
     * The function accepts STRING s as parameter.
     */
     
    public static long startNumber = -1;

    public static void separateNumbers(String s) {
        // Write your code here
        backtrack(s, 0);
        if (startNumber != -1 && !s.equals(""+startNumber)) {
            System.out.println("YES " + startNumber);
        } else {
            System.out.println("NO");
        }
        startNumber = -1;
    }
    
    public static boolean backtrack(String s, long val) {
        if (s.length() == 0) {
            return true;
        } 
        if (s.charAt(0) == '0') {
            return false;
        }
        for (int i = 0; i < s.length()/2+1; i++) {
            if (val == 0) {
                long num = Long.valueOf(s.substring(0, i+1));
                if (backtrack(s.substring(i+1), num)) {
                    startNumber = num;
                    return true;
                }
            } else {
                long newNum = val + 1;
                String numStr = ""+newNum;
                if (s.length() >= numStr.length() && s.substring(0, numStr.length()).equals(numStr)) {
                    if (backtrack(s.substring(numStr.length()), newNum)) {
                        return true;
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        return false;
    }
    
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                String s = bufferedReader.readLine();

                Result.separateNumbers(s);
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
    }
}

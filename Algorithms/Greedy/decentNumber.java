// Sherlock and The Beast


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
     * Complete the 'decentNumber' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void decentNumber(int n) {
        // Write your code here
        StringBuilder sb = new StringBuilder();
        
        if (n % 3 == 0) {
            for (int i = 0; i < n; i++) {
                sb.append(5);
            }
        } else if (n % 3 == 2 && n >= 5) {
            for (int i = 0; i < n - 5; i++) {
                sb.append(5);
            }
            for (int i = 0; i < 5; i++) {
                sb.append(3);
            }
        } else if (n % 3 == 1 && n >= 10) {
            for (int i = 0; i < n - 10; i++) {
                sb.append(5);
            }
            for (int i = 0; i < 10; i++) {
                sb.append(3);
            }
        }
        
        System.out.println((!sb.isEmpty()) ? sb : -1);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                int n = Integer.parseInt(bufferedReader.readLine().trim());

                Result.decentNumber(n);
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
    }
}

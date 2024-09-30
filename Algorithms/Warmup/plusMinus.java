// Plus Minus


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
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
        // Write your code here
        double numPositive = 0;
        double numNegative = 0;
        double numZero = 0;
        double total = arr.size();
        
        for (int val: arr) {
            if (val > 0) {
                numPositive++;
            } else if (val < 0) {
                numNegative++;
            } else {
                numZero++;
            }
        }
        
        double positiveRate = numPositive / total;
        double negativeRate = numNegative / total;
        double zeroRate = numZero / total;
        
        System.out.println(String.format("%.6f", positiveRate));
        System.out.println(String.format("%.6f", negativeRate));
        System.out.println(String.format("%.6f", zeroRate));
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}

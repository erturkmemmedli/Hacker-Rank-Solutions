// Repeated String


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
     * Complete the 'repeatedString' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     *  1. STRING s
     *  2. LONG_INTEGER n
     */

    public static long repeatedString(String s, long n) {
        // Write your code here
        List<Integer> index = new ArrayList<>();
        int l = s.length();
        long result = 0;
        
        for (int i = 0 ; i < l; i++) {
            if (s.charAt(i) == 'a') {
                index.add(i);
            }
        }
                
        result += (n / l) * index.size();
        long mod = n % l;
        result += binarySearch(index, mod, true);
        return result;
    }
    
    public static int binarySearch(List<Integer> array, long target, boolean flag) {
        int low = 0;
        int high = array.size() - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (array.get(mid) == target) {
                return mid;
            } else if (array.get(mid) > target) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }

        if (flag) {
            return binarySearch(array, target, false);
        }
        
        return low;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        long n = Long.parseLong(bufferedReader.readLine().trim());

        long result = Result.repeatedString(s, n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

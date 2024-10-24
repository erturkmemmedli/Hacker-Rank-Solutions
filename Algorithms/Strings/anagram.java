// Anagram


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
     * Complete the 'anagram' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING s as parameter.
     */

    public static int anagram(String s) {
        // Write your code here
        int n = s.length();
        if (n%2 == 1) return -1;
        
        String s1 = s.substring(0, n/2);
        String s2 = s.substring(n/2, n);
        
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (int i=0; i<n/2; i++) {
            char c1 = s1.charAt(i);
            map.put(c1, map.getOrDefault(c1, 0) + 1);
        }
        
        for (int i=0; i<n/2; i++) {
            char c2 = s2.charAt(i);
            if (map.containsKey(c2)) {
                map.put(c2, map.get(c2) - 1);
                if (map.get(c2) == 0) {
                    map.remove(c2);
                }
            }
        }
        
        int count = 0;
        
        for (int val: map.values()) {
            count += val;
        }
        
        return count;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                String s = bufferedReader.readLine();

                int result = Result.anagram(s);

                bufferedWriter.write(String.valueOf(result));
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

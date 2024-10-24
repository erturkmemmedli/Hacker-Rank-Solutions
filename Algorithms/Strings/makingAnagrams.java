// Making Anagrams


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
     * Complete the 'makingAnagrams' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. STRING s1
     *  2. STRING s2
     */

    public static int makingAnagrams(String s1, String s2) {
        // Write your code here
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (int i = 0; i < s1.length(); i++) {
            char c1 = s1.charAt(i);
            map.put(c1, map.getOrDefault(c1, 0) + 1);
        }
        
        
        for (int i = 0; i < s2.length(); i++) {
            char c2 = s2.charAt(i);
            map.put(c2, map.getOrDefault(c2, 0) - 1);
        }
        
        int count = 0;
        
        for (int val: map.values()) {
            count += Math.abs(val);
        }
        
        return count;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s1 = bufferedReader.readLine();

        String s2 = bufferedReader.readLine();

        int result = Result.makingAnagrams(s1, s2);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

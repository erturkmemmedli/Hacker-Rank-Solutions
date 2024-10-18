// Happy Ladybugs


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
     * Complete the 'happyLadybugs' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING b as parameter.
     */

    public static String happyLadybugs(String b) {
        // Write your code here
        if (b.length() == 1) {
            return (b.equals("_")) ? "YES" : "NO";
        }
        
        HashMap<Character, Integer> counter = new HashMap<>();
        boolean problemMayExist = false;
        boolean underscoreExists = false;
        
        for (int i = 0; i < b.length(); i++) {
            char c = b.charAt(i);
            if (c == '_') {
                underscoreExists = true;
            }
            counter.put(c, counter.getOrDefault(c, 0) + 1);
            if (i == 0 && c != b.charAt(i + 1)) {
                problemMayExist = true;
            }
            if (i == b.length() - 1 && c != b.charAt(i - 1)) {
                problemMayExist = true;
            }
            if (i > 0 && i < b.length() - 1 && c != b.charAt(i - 1) && c != b.charAt(i + 1)) {
                problemMayExist = true;
            }
        }
        
        for (Map.Entry<Character, Integer> entry: counter.entrySet()) {
            char key = entry.getKey();
            int val = entry.getValue();
            if (key != '_' && val == 1) {
                return "NO";
            }
        }
        
        if (underscoreExists) {
            return "YES";
        }
        if (problemMayExist) {
            return "NO";
        }
        return "YES";
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int g = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, g).forEach(gItr -> {
            try {
                int n = Integer.parseInt(bufferedReader.readLine().trim());

                String b = bufferedReader.readLine();

                String result = Result.happyLadybugs(b);

                bufferedWriter.write(result);
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

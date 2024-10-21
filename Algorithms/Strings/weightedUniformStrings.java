// Weighted Uniform Strings


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
     * Complete the 'weightedUniformStrings' function below.
     *
     * The function is expected to return a STRING_ARRAY.
     * The function accepts following parameters:
     *  1. STRING s
     *  2. INTEGER_ARRAY queries
     */

    public static List<String> weightedUniformStrings(String s, List<Integer> queries) {
        // Write your code here
        HashMap<Character, Integer> counter = new HashMap<>();
        HashSet<Integer> weights = new HashSet<>();
        List<String> resultSet = new ArrayList<>();
        char currentChar = s.charAt(0);
        int currentLength = 1;
        
        for (int i = 1; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == currentChar) {
                currentLength++;
            } else {
                counter.put(currentChar, Math.max(counter.getOrDefault(currentChar, 0), currentLength));
                currentChar = c;
                currentLength = 1;
            }
        }
        
        counter.put(currentChar, Math.max(counter.getOrDefault(currentChar, 0), currentLength));
        
        for (Map.Entry<Character, Integer> entry: counter.entrySet()) {
            char key = entry.getKey();
            int val = entry.getValue();
            int weight = (int) key - (int) 'a' + 1;
            
            for (int i = 1; i <= val; i++) {
                weights.add(weight * i);
            }
        }
        
        for (int query: queries) {
            resultSet.add((weights.contains(query)) ? "Yes" : "No");
        }
        
        return resultSet;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        int queriesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> queries = IntStream.range(0, queriesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        List<String> result = Result.weightedUniformStrings(s, queries);

        bufferedWriter.write(
            result.stream()
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}

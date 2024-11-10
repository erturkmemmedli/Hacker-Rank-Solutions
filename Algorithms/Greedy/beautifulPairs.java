// Beautiful Pairs


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
     * Complete the 'beautifulPairs' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY A
     *  2. INTEGER_ARRAY B
     */

    public static int beautifulPairs(List<Integer> A, List<Integer> B) {
        // Write your code here
        HashMap<Integer, int[]> map = new HashMap<>();
        int pairs = 0;
        
        for (int i = 0; i < A.size(); i++) {
            if (!map.containsKey(A.get(i))) {
                map.put(A.get(i), new int[2]);
            }
            map.get(A.get(i))[0]++;
        }
        
        for (int i = 0; i < B.size(); i++) {
            if (!map.containsKey(B.get(i))) {
                map.put(B.get(i), new int[2]);
            }
            map.get(B.get(i))[1]++;
        }
        
        for (Map.Entry<Integer, int[]> entry: map.entrySet()) {
            int[] val = entry.getValue();
            pairs += Math.min(val[0], val[1]);
        }
        map.forEach((k, v) -> System.out.print(v[0] + " " + v[1] + ", "));
        
        return (pairs == A.size()) ? pairs - 1 : pairs + 1;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> A = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        List<Integer> B = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int result = Result.beautifulPairs(A, B);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

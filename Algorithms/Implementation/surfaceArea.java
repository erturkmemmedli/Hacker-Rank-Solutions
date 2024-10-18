// 3D Surface Area


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
     * Complete the 'surfaceArea' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY A as parameter.
     */

    public static int surfaceArea(List<List<Integer>> A) {
        // Write your code here
        int m = A.size();
        int n = A.get(0).size();
        int area = 2 * m * n;
        
        for (int i = 0; i < m; i++) {
            area += A.get(i).get(0);
            for (int j = 1; j < n; j++) {
                area += Math.max(0, A.get(i).get(j) - A.get(i).get(j - 1));
            }
            area += A.get(i).get(n - 1);
            for (int j = n - 2; j >= 0; j--) {
                area += Math.max(0, A.get(i).get(j) - A.get(i).get(j + 1));
            }
        }
        
        for (int i = 0; i < n; i++) {
            area += A.get(0).get(i);
            for (int j = 1; j < m; j++) {
                area += Math.max(0, A.get(j).get(i) - A.get(j - 1).get(i));
            }
            area += A.get(m - 1).get(i);
            for (int j = m - 2; j >= 0; j--) {
                area += Math.max(0, A.get(j).get(i) - A.get(j + 1).get(i));
            }
        }

        return area;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int H = Integer.parseInt(firstMultipleInput[0]);

        int W = Integer.parseInt(firstMultipleInput[1]);

        List<List<Integer>> A = new ArrayList<>();

        IntStream.range(0, H).forEach(i -> {
            try {
                A.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = Result.surfaceArea(A);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

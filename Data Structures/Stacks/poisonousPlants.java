// Poisonous Plants


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
     * Complete the 'poisonousPlants' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY p as parameter.
     */

    public static int poisonousPlants(List<Integer> p) {
        // Write your code here
        Stack<int[]> stack = new Stack<>();
        int result = 0;
        
        for (int i = p.size() - 1; i >= 0; i--) {
            int temp = 0;
            
            while (!stack.isEmpty() && stack.peek()[0] > p.get(i)) {
                temp = Math.max(temp + 1, stack.pop()[1]);
            }
            
            result = Math.max(result, temp);
            stack.push(new int[] {p.get(i), temp});
        }

        return result;
    }

    public static int binarySearchLeft(List<Integer> p, int target) {
        int left = 0, right = p.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (p.get(mid) >= target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }

    public static int binarySearchRight(List<Integer> p, int target) {
        int left = 0, right = p.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (p.get(mid) <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return right + 1;
    }
    
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> p = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int result = Result.poisonousPlants(p);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

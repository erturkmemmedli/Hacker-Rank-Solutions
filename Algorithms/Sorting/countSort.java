// The Full Counting Sort


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
import java.util.concurrent.atomic.AtomicInteger;


class Result {

    /*
     * Complete the 'countSort' function below.
     *
     * The function accepts 2D_STRING_ARRAY arr as parameter.
     */

    public static void countSort(List<List<String>> arr) {
        // Write your code here
        TreeMap<Integer, List<String>> treeMap = new TreeMap<>();
        StringBuffer result = new StringBuffer();
        
        for (int i = 0; i < arr.size(); i++) {
            int key = Integer.parseInt(arr.get(i).get(0));
            String val = arr.get(i).get(1);
            
            List<String> list = treeMap.computeIfAbsent(key, k -> new ArrayList<>());
            if (i < arr.size() / 2) {
                list.add("-");
            } else {
                 list.add(val);
            }
        }
        
        int size = treeMap.size();
        AtomicInteger index = new AtomicInteger(0);
        
        treeMap.forEach((k, v) -> {
            result.append(v.stream().collect(Collectors.joining(" ")));
            if (index.incrementAndGet() < size) {
                result.append(" ");
            }
        });
        
        System.out.println(result);
    }

}


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<String>> arr = new ArrayList<>();

        IntStream.range(0, n).forEach(i -> {
            try {
                arr.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        Result.countSort(arr);

        bufferedReader.close();
    }
}

// The Bomberman Game


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
     * Complete the 'bomberMan' function below.
     *
     * The function is expected to return a STRING_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. STRING_ARRAY grid
     */

    public static List<String> bomberMan(int n, List<String> grid) {
        // Write your code here
        List<String> fullBombGrid = new ArrayList<>();
        List<String> afterBombGrid = new ArrayList<>();
        List<String> lastBombGrid = new ArrayList<>();
        
        for (int i = 0; i < grid.size(); i++) {
            fullBombGrid.add("O".repeat(grid.get(0).length()));
        }
        
        helper(grid.size(), grid.get(0).length(), grid, afterBombGrid);
        helper(grid.size(), grid.get(0).length(), afterBombGrid, lastBombGrid);
                
        if (n == 1) {
            return grid;
        } else if (n % 2 == 0) {
            return fullBombGrid;
        } else if (n % 4 == 3) {
            return afterBombGrid;
        } else {
            return lastBombGrid;
        }
    }
    
    public static void helper(int n, int m, List<String> grid, List<String> result) {
        HashSet<String> coordinates = new HashSet<>();
        String line;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid.get(i).charAt(j) == 'O') {
                    coordinates.add(i + "," + j);
                    if (i - 1 >= 0) coordinates.add((i - 1) + "," + j);
                    if (i + 1 < n) coordinates.add((i + 1) + "," + j);
                    if (j - 1 >= 0) coordinates.add(i + "," + (j - 1));
                    if (j + 1 < m) coordinates.add(i + "," + (j + 1));
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            line = "";
            for (int j = 0; j < m; j++) {
                line += (coordinates.contains(i + "," + j)) ? "." : "O";
            }
            result.add(line);
        }
    }
 
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int r = Integer.parseInt(firstMultipleInput[0]);

        int c = Integer.parseInt(firstMultipleInput[1]);

        int n = Integer.parseInt(firstMultipleInput[2]);

        List<String> grid = IntStream.range(0, r).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        List<String> result = Result.bomberMan(n, grid);

        bufferedWriter.write(
            result.stream()
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}

// Java String Tokens

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        
        List<String> output = splitTokens(s);
        System.out.println(output.size());
        
        for (String token: output) {
            System.out.println(token);
        }
        
        scanner.close();
    }
    
    public static List<String> splitTokens(String s) {
        List<String> tokens = new ArrayList<>();
        StringBuilder currToken = new StringBuilder();
        
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                currToken.append(s.charAt(i));
            } else if (currToken.length() > 0) {
                tokens.add(currToken.toString());
                currToken = new StringBuilder(); 
            } else {
                currToken = new StringBuilder(); 
            }
        }
        
        if (currToken.length() > 0) {
            tokens.add(currToken.toString());
        }
        
        return tokens;
    }
}

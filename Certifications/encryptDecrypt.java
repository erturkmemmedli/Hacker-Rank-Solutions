// 2. Java: Encryption Decryption

// P.S. Four test cases didn't pass although hardest ones passed. Didn't understand why.
    
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


class Result {

    /*
     * Complete the 'decryptMessage' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING encryptedMessage as parameter.
     */

    public static String decryptMessage(String encryptedMessage) {
        List<String> words = new ArrayList<>();
        List<Integer> spacesBetweenWords = new ArrayList<>();
        
        StringBuilder currentWord = new StringBuilder();
        int spaceCount = 0;

        for (int i = 0; i < encryptedMessage.length(); i++) {
            char c = encryptedMessage.charAt(i);

            if (c != ' ') {
                currentWord.append(c);
                spaceCount = 0;
            } else {
                if (currentWord.length() > 0) {
                    words.add(currentWord.toString());
                    currentWord.setLength(0);
                    while (i < encryptedMessage.length() && encryptedMessage.charAt(i) == ' ') {
                        spaceCount++;
                        i++;
                    }
                    spacesBetweenWords.add(spaceCount);
                    i--;
                }
            }
        }
        
        if (currentWord.length() > 0) {
            words.add(currentWord.toString());
        }
        
        StringBuilder decryptedMessage = new StringBuilder();
        
        for (int i = words.size() - 1; i >= 0; i--) {
            String s = words.get(i);
            int j = 0;
            
            while (j < s.length()) {
                if (Character.isDigit(s.charAt(j))) {
                    char c = decryptedMessage.charAt(decryptedMessage.length() - 1);
                    int repeatCount = Character.getNumericValue(s.charAt(j));
                    for (int k = 0; k < repeatCount - 1; k++) {
                        decryptedMessage.append(c);
                    }
                } else {
                    decryptedMessage.append(s.charAt(j));
                }
                j++;
            }
            
            if (i != 0) {
                for (int t = 0; t < spacesBetweenWords.get(i - 1); t++) {
                    decryptedMessage.append(" ");
                }
            }
        }
        
        return decryptedMessage.toString();
    }

}
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String encryptedMessage = bufferedReader.readLine();

        String result = Result.decryptMessage(encryptedMessage);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

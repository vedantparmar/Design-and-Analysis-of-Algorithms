public class LongestCommonSubsequence {

    // Function to find the length of the longest common subsequence
    public static int lcs(String str1, String str2) {
        int m = str1.length();
        int n = str2.length();

        // Create a 2D array to store lengths of longest common subsequence
        int[][] dp = new int[m + 1][n + 1];

        // Build the dp array from bottom up
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1.charAt(i - 1) == str2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1; // Characters match
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]); // Choose the maximum
                }
            }
        }

        return dp[m][n]; // Length of LCS
    }

    public static void main(String[] args) {
        String str1 = "AGGTAB";
        String str2 = "GXTXAYB";

        int lengthOfLCS = lcs(str1, str2);
        System.out.println("Length of Longest Common Subsequence: " + lengthOfLCS);
    }
}

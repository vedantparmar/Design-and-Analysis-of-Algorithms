public class MatrixChainMultiplication {

    // Function to perform matrix chain multiplication
    public static int matrixChainOrder(int[] p, int n) {
        // m[i][j] will store the minimum number of multiplications needed to multiply matrices Ai...Aj
        int[][] m = new int[n][n];

        // l is the chain length
        for (int l = 2; l <= n; l++) { // l is the chain length
            for (int i = 1; i <= n - l + 1; i++) {
                int j = i + l - 1; // Set the end index
                m[i][j] = Integer.MAX_VALUE; // Initialize to a large value

                // Try every possible split point
                for (int k = i; k < j; k++) {
                    // q is the cost of multiplying A[i..k] and A[k+1..j]
                    int q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                    if (q < m[i][j]) {
                        m[i][j] = q; // Update minimum cost
                    }
                }
            }
        }

        return m[1][n - 1]; // Return the minimum cost for multiplying A1..An
    }

    public static void main(String[] args) {
        // Dimensions of the matrices (A1: p[0] x p[1], A2: p[1] x p[2], ...)
        int[] dimensions = {30, 35, 15, 5, 10, 20, 25};

        int n = dimensions.length; // Number of matrices
        int minCost = matrixChainOrder(dimensions, n);

        System.out.println("Minimum number of multiplications: " + minCost);
    }
}

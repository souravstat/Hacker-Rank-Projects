Training File: http://hr-testcases.s3.amazonaws.com/2552/assets/training.txt
Sample Input : http://hr-testcases.s3.amazonaws.com/2552/assets/sampleInput.txt
Sample Output : http://hr-testcases.s3.amazonaws.com/2552/assets/sampleOutput.txt
My accuracy: 0.9333333373069763

Flipkart is a popular Indian e-commerce portal. One of the most common actions performed by users of the portal, is to use the search box and query for a brand, product or product-line. The search box then returns the best matching products which it can find - along with their prices, details, descriptions, etc.

We have different search queries (specified below), and made a list of some of the product names which were returned in response to them. We are provided with a list of N names of products from this list. The task is to guess, which search query each of them was returned in response to.
e.g.-
1)In response to which of these queries, was the product 'Dell Vostro 2520 Laptop (2nd Gen PDC/ 2GB/ 320GB/ Linux...' (most likely) returned? 
Answer:dell laptops
2)In response to which of these queries, was the product 'Calvin Klein One Eau de Toilette - 200 ml' (most likely) returned? 
Answer:calvin klein

Instructions:(https://www.hackerrank.com/challenges/guess-the-flipkart-query/problem)

Input Format
The first line contains an integer N. 
This is followed by N lines each containing the name of a product.

Input Constraints

1 <= N <= 200 
The product names will not exceed 200 characters in length. Sometimes, when the product name is long and descriptive, after the first 55 characters, there are likely to be a series of dots, such as the examples below. Please handle them appropriately (strip them off, or ignore them).

Laptops: AMD Mobile Platform, AMD Vision, Barebook, Cen...
Dell Vostro 2520 Laptop (2nd Gen PDC/ 2GB/ 320GB/ Linux...
Dell Inspiron 15R 5521 Laptop (3rd Gen Ci7/ 8GB/ 1TB/ W...
Output Format

The output should contain exactly N lines. 
The ith line should contain the query (your best guess) which returned the ith product name in the input file. The query should strictly be from one of the twenty queries specified above, as is. Please do not add any leading or trailing spaces or any extra punctuation. Also ensure that the case remains the same.
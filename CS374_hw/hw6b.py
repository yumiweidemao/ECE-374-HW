def largestNumOfChickens(A):
    n = len(A)

    # maxChicken[i][j][k] is the maximum number of chickens Mr.Fox can get when he 
    # is at booth i with j consecutive "Ring!"s and k consecutive "Ding!"s before he
    # reaches booth i.
    maxChicken = [[[-99999 for _ in range(4)] for _ in range(4)] for _ in range(n)]
    maxChicken[0][1][0] = A[0]
    maxChicken[0][0][1] = -A[0]
    for i in range(1, n):
        maxChicken[i][0][1] = max(maxChicken[i-1][1][0],maxChicken[i-1][2][0],maxChicken[i-1][3][0]) - A[i]
        maxChicken[i][1][0] = max(maxChicken[i-1][0][1],maxChicken[i-1][0][2],maxChicken[i-1][0][3]) + A[i]
        for j in range(2, 4):
            maxChicken[i][j][0] = maxChicken[i-1][j-1][0] + A[i]
        for k in range(2, 4):
            maxChicken[i][0][k] = maxChicken[i-1][0][k-1] - A[i]
    
    # find maximum in maxChicken[n-1]
    res = []
    for item in maxChicken[n-1]:
        res.extend(item)
    return max(res)

A = [3, 4, 5, 6, 7]
print(largestNumOfChickens(A))
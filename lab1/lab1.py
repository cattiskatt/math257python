def A_subset(A,n):
    sum = 0;  #initializes the variable 'sum'
    for i in A: #loops through the array and add the next element to the what's already been added previously
        sum += i #adds to the existing sum

    A_sub = A[:n] # we only want parts of the array, which is the first n entries. this extracts all entries of A up until n

    return (sum, A_sub) #returns the value of sum along with our array 'A-sub'
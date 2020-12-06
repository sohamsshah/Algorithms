def rotateArr(arr,d,n):
    def gcd(a, b):
        if b == 0:
            return a;
        else:
            return gcd(b, a % b)
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
        # move i-th values of blocks 
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
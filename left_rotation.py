# here we have rotate the values of array in left direction
# arr is the array to be rotated and n is number of the values to be moved in order to rotate
# we can check this by taking a sample input array and different values for n either positive or negative


def left_rotation(arr,n):
    print(arr)
    print(n)
    # if the rotaion value is positive
    if n>0:
        a = arr[0:n]
        b=arr[n:]
        print(a)
        print(b)
        for i in a:
            b.append(i)
        print(b)
    #if the rotaion value is negative
    else:
        a=arr[-len(arr):n]
        b=arr[n:]
        print(a)
        print(b)
        for i in a:
            b.append(i)
        print(b)

#sample test cases
a=[1,2,3,4,5,6]
n=-1
left_rotation(a,n)

a=[1,2,3,4,5,6]
n=3
left_rotation(a,n)
import numpy as np
def task1():
    b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
    print(type(b))
    print(b.dtype)
    a = np.array([10, 2, 30, 40,50])
    a[1]=20
    print(a)
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    evenArr=arr[1:8:2]
    print(evenArr)
    c = np.array([10, 20, 30, 40, 50, 60, 70])
    print(c.size)
    print(c.ndim)
    print(c.shape)
    mean = a.mean()
    print(mean)
    print(a.std())
    z = np.array([-10, 201, 43, 94, 502])
    print(z.max(),z.min())
    arr1 = np.array([10, 11, 12, 13, 14, 15])
    arr2 = np.array([20, 21, 22, 23, 24, 25])
    arr3=np.add(arr1,arr2)
    print(arr3)
    arr4 = np.array([10, 20, 30, 40, 50, 60])
    arr5 = np.array([20, 21, 22, 23, 24, 25])
    arr6=np.subtract(arr4,arr5)
    arr7=arr4-arr5
    print(arr6,arr7)
    print(np.pi,np.sin(0))
    print(np.linspace(-2, 2, num=9))
    u = np.array([1, 0])
    v = np.array([0, 1])
    p=u-v
    print(p)
    print(-2*np.array([2, 4]))
    print(np.array([1, 2, 3, 4, 5])*np.array([1, 0, 1, 0, 1]))
def task2():
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    A=np.array(a)
    print(A.size)
    print(A[0,0:2])
    B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
    C=np.dot(A,B)
    print(C)

if __name__=='__main__':
    task1()
    task2()
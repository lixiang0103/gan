import numpy as np

if __name__ == '__main__':
    a = np.array([[[1,1,1],[1,1,1],[1,1,1]],[[2,2,2],[2,2,2],[2,2,2]]])
    print a.shape
    b = np.array([[[2,2,2],[2,2,2],[2,2,2]],[[2,2,2],[2,2,2],[2,2,2]]])
    result = np.append(a, b,axis = 0)
    print result.shape
    print "hello world"
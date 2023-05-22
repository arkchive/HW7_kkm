# Q1
# 1. 다음 정사형 배열의 고윳값, 고유벡터 그리고 행렬식을 구하시오(use np.linalg.???)
# 2. 주어진 두개의 벡터의 외적을  계산하시오
# 3. 다음 일차 방정식을 구하시오(use np.linalg.???)

import numpy as np

def main():
    arr = np.array([[1,2],[3,4]])
    w, v = np.linalg.eig(arr)
    det = np.linalg.det(arr)

    print('Eigenvalues:', w)
    print('Eigenvectors:\n', v)
    print('Determinant:', det)

    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    
    print('Cross Product:', np.cross(vec1, vec2))

    a = np.array([[1, 2, -2], [2, 1, -5], [1, -4, 1]])
    b = np.array([[-15], [-21], [18]])
    x = np.linalg.solve(a, b)
    print('Solution:\n', x)

if __name__ == '__main__':
    main()

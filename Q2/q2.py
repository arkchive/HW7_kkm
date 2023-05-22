# Q2
# 2차원 Matrix 형태로 표현된 3개의 문서와 1차원 벡터 형태의 질의 사이의
# 코사인 유사도를 계산하시오 (소수점 둘째자리까지 출력, use numpy)

import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def main():
    docs = np.array([[1,1,0,1,0,1], [1,1,1,0,1,0], [1,1,0,1,0,0]])
    query = np.array([1,1,0,0,1,0])

    doc1 = docs[0, :]
    doc2 = docs[1, :]
    doc3 = docs[2, :]

    print('doc1=%.2f' %cos_sim(doc1, query))
    print('doc2=%.2f' %cos_sim(doc2, query))
    print('doc3=%.2f' %cos_sim(doc3, query))

def cos_sim(a, b):
    return dot(a, b)/(linalg.norm(a)*linalg.norm(b))

if __name__ == '__main__':
    main()

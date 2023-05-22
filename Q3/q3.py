# Q3
# 총 가격이 가장 비싼 가계를 출력하는 프로그램(use pandas)
# - 단가(unit price)와 개수(number)로 이루어진 데이터 프레임 생성 및 출력
# - 단가와 개수를 곱한 총 가격(total price)이 추가된 데이터 프레임 생성 및 출력
# - 총 가격이 가장 비싼 가계순으로 2개 출력

import pandas as pd

def main():
    data = [[1000, 25],[280, 120],[900, 30]]
    df = pd.DataFrame(data, index=['store1', 'store2', 'store3'], columns=['unit price', 'number'])
    print('단가와 개수로 이루어진 데이터 프레임')
    print(df, '\n')
    
    df['total price'] = df['unit price'] * df['number']
    print('단가와 개수를 곱한 총 가격이 추가된 데이터 프레임')
    print(df, '\n')
    
    df2 = df.sort_values(by=['total price'], ascending=False)
    print('총 가격이 가장 비싼 가계순으로 2개 출력된 데이터 프레임')
    print(df2.head(2))

if __name__ == '__main__':
    main()

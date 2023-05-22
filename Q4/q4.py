# Q4
# 인구통계 출력 프로그램(use pandas)
# gender2.csv를 pd.read_csv()로 읽어오시오(use encoding, index_col)
# 총 인구수(Total), 남(Male), 여(Female) columns를 선택하여 new DataFrame 생성
# columns의 이름 변경 -> Total, Male, Female
# 최종 DataFrame 전체 출력

import numpy as np
import pandas as pd

def main():
    data = pd.read_csv('C:\dev\opensw\HW7_kkm\Q4/gender2.csv', encoding='CP949', index_col=0)

    df = pd.DataFrame(data, columns=['2022년_계_총인구수', '2022년_남_총인구수', '2022년_여_총인구수'])
    df.columns = ['Total', 'Male', 'Female']

    print(df)

if __name__ == '__main__':
    main()

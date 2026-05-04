import pandas as pd

class Walter:             # 클래스: 물건의 정체 - 관습적으로 대문자로 씀.
    def __init__(self):   # 메서드: 그 물건이 할수있는 일 
        pass              # 알고리즘: 그 일을 수행하는 방법 

    def get_data(self):
        df = pd.read_csv("Titanic-Dataset.csv")
        print(df.head(10)) 


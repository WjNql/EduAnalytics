import pandas as pd
import numpy as np

class GradeCleaner:
    def __init__(self, raw_path='demo_grades.csv'):
        self.raw_data = pd.read_csv(raw_path)
        
    def handle_outliers(self, df, subject):
        """使用IQR方法处理异常值"""
        Q1 = df[subject].quantile(0.25)
        Q3 = df[subject].quantile(0.75)
        IQR = Q3 - Q1
        df.loc[df[subject] > Q3 + 1.5*IQR, subject] = Q3
        df.loc[df[subject] < Q1 - 1.5*IQR, subject] = Q1
        return df
        
    def pipeline(self):
        df = self.raw_data.copy()
        # 处理缺失值
        df.fillna({'math': 0, 'physics': 0}, inplace=True)
        # 处理异常值
        for subject in ['math', 'physics']:
            df = self.handle_outliers(df, subject)
        # 添加总分列
        df['total'] = df[['math', 'physics']].sum(axis=1)
        return df

# 测试运行
if __name__ == "__main__":
    cleaner = GradeCleaner()
    cleaned_df = cleaner.pipeline()
    cleaned_df.to_parquet('cleaned_grades.parquet', index=False)
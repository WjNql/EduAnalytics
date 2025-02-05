import pandas as pd
from matplotlib import pyplot as plt

class GradeAnalyzer:
    def __init__(self, data_path='data/processed/cleaned_grades.parquet'):
        self.df = pd.read_parquet(data_path)
    
    def class_comparison(self):
        return self.df.groupby('class').agg({
            'math': ['mean', 'std'],
            'physics': ['mean', 'std'],
            'total': 'median'
        })
    
    def plot_correlation(self):
        plt.figure(figsize=(8,6))
        plt.scatter(self.df['math'], self.df['physics'], alpha=0.5)
        plt.title('Math vs Physics Score Correlation')
        plt.xlabel('Math Score')
        plt.ylabel('Physics Score')
        plt.savefig('reports/figures/correlation.png')
        plt.close()

# 测试运行
if __name__ == "__main__":
    analyzer = GradeAnalyzer()
    print(analyzer.class_comparison())
    analyzer.plot_correlation()
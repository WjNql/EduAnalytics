import pandas as pd
import numpy as np

grades_data = {
    'student_id': [f'S{1000+i}' for i in range(50)],
    'math': [np.clip(np.random.normal(75, 15), 0, 100) for _ in range(50)],
    'physics': [np.clip(np.random.normal(70, 12), 0, 100) for _ in range(50)],
    'class': ['A班' if i<25 else 'B班' for i in range(50)]
}
df = pd.DataFrame(grades_data)
df.to_csv('data/raw/demo_grades.csv', index=False)
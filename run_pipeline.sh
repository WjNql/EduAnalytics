# 创建自动化脚本run_pipeline.sh
# '#!/bin/bash' 是一个 shebang，用于指定脚本的解释器。它告诉操作系统使用 /bin/bash 程序来执行脚本。通过使用 shebang，你可以直接运行脚本文件，而不需要显式调用解释器。
#!/bin/bash
source /home/ubuntu/anaconda3/bin/activate edu_analytics
python data_cleaner.py
mv cleaned_grades.parquet data/processed/
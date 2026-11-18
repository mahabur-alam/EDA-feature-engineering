import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport


df = pd.read_csv('../datasets/titanic_data_updated.csv')

# generate the profiling report
report = ProfileReport(df, title="Titanic Profiling Report")

# save the report as an HTML file
report.to_file("titanic_profiling_report.html")
print("Report saved to titanic_profiling_report.html")

import pandas as pd

df = pd.DataFrame(columns = ['image_name','action'],index = False)
df.to_csv('dataset.csv')
import numpy as np
import pandas as pd
import pingouin as pg
import matplotlib as plplot

# load data
df = pd.read_csv('rawdata.csv')

# rename one column
df.rename(columns = {'male':'Gender'}, inplace = True)
# ratio of gender
gender_ratio=df['Gender'].value_counts(ascending=True)
print(gender_ratio)
# ration was 1820/2420=.75
#Chi iddependence test
expected, observed, stats = pg.chi2_independence(df, x='Gender', y='TenYearCHD')
# Expected contingency tabel
our_exp=expected
print(our_exp)
# observed contingency table
data_obs=observed
print(data_obs)
#round up test statiscs
chitest= stats.round(3)
print(chitest)

print("hello world")

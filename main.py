import datetime as dt
import pandas as pd
import polars as pl
import numpy as np

random_data = np.random.rand(10000, 10)

pandas_df = pd.DataFrame(random_data)
polars_df = pl.DataFrame(random_data)


pd_time_start = dt.datetime.now()
[pandas_df.corr() for i in range(1, 100)]
pd_time_end = dt.datetime.now()

pl_time_start = dt.datetime.now()
[polars_df.corr() for i in range(1, 100)]
pl_time_end = dt.datetime.now()

pandas_elapsed = pd_time_end - pd_time_start
polars_elapsed = pl_time_end - pl_time_start
print(f"Time elapsed: {pandas_elapsed}")
print(f"Time elapsed: {polars_elapsed}")
print(f"Pandas took {round(pandas_elapsed / polars_elapsed, 2)} times longer!")

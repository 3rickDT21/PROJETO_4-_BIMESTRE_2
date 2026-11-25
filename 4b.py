import pandas as pd
from mendeleev.fetch import fetch_table

df = fetch_table('elements')
series_df = fetch_table('series').set_index('id')['name'].to_dict()

print(series_df)
print(df)
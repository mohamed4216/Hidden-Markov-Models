import pandas as pd
import numpy as np

hdf = pd.HDFStore('dataset.h5', 'w', format='table')
for x in [11, 13, 15]:
	df_lbl = pd.read_csv('RLAlabels_' + str(x) + '.csv').astype(np.int64)
	df_lbl.columns = [n.replace('_resample', '') for n in df_lbl.columns]
	df_data = pd.read_csv('RLAdata_' + str(x) + '.csv')
	df_data.columns = [n.replace('_resample', '') for n in df_data.columns]
	hdf.put('participant_' + str(x) + '/segments', df_lbl, format='table')
	hdf.put('participant_' + str(x) + '/samples', df_data, format='table')
hdf.close()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import os 
from sklearn.preprocessing import StandardScaler
import datetime
Today_date=datetime.datetime.now().strftime("%Y%m%d")
import matplotlib.cm as cm
import glob

path='/home/a/ap744/scratch_alok/UKEAP_data/UKEAP_AcidGases_Aerosol/UKEAP_particulate_nitrate/'
NO3files=glob.glob(path + '28-UKA0*-2016_particulate_nitrate_*.csv')

#sites = pd.read_csv('/home/a/ap744/scratch_alok/UKEAP_data/DEFRA_UKEAP_sites_details/UKEAP_AcidGases_Aerosol_sites_details.csv', encoding= 'unicode_escape')
sites = pd.read_csv('/home/a/ap744/scratch_alok/UKEAP_data/DEFRA_UKEAP_sites_details/UKEAP_AcidGases_Aerosol_sites_details.csv', encoding= 'unicode_escape')
#print (sites.head(10))
ID = sites["UK-AIR_ID"]
#print (ID)

x= []

for f in NO3files:
	df = pd.read_csv(f)  
	print (df.head(10))
	#print (len(NO3files))
	sitesA = sites.copy()

	mean_A= df["Measurement"].mean()
	#print (mean_A, f[91:99])
	sitesA["nitrate_annual_mean"] = mean_A
	print (sitesA.head(10))
	
	x.append(
	{
		'UK-AIR_ID':f[91:99],
		'nitrate_annual_mean':mean_A
		}
		)
	
	#print (x)
id_mean = pd.DataFrame(x)

print (id_mean.head(10))

df_merge_col = pd.merge(sites, id_mean, on='UK-AIR_ID', how ='right')

print (df_merge_col.head(25))

#df_merge_col.to_excel(r'/home/a/ap744/scratch_alok/python_work/merge_file_nitrate_mean.xlsx',index =False)
df_merge_col.to_csv(r'/home/a/ap744/scratch_alok/python_work/nitrate_annual_mean.csv')
	

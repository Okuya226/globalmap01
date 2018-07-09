import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

#データ読み込み
main_df=pd.read_table( 'Okuya_N1bar_landProxima_map.txt', sep='\s+', header=None)

#mainカラムに名前をつける
main_df.columns   
main_df.columns =["month","x","y","Temp"]   



from mpl_toolkits.basemap import Basemap
#地図の描画
map = Basemap(projection='robin',lat_0=0, lon_0=0, resolution='c')
#map.drawcoastlines(color="white")
map.drawmeridians(np.arange(-150, 180, 60))
map.drawparallels(np.arange(-80, 90, 40))


lon, lat = map(main_df['x'].values, main_df['y'].values)
#z = main_df["Temp"]

map.scatter(lon,lat,c=main_df["Temp"])

fnameF='fig02.png'
plt.savefig(fnameF, bbox_inches="tight", pad_inches=0.2)
plt.show()


exit()



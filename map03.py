import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

#データ読み込み
main_df=pd.read_table( 'Okuya_N1bar_landProxima_map.txt', sep='\s+', header=None)

#mainカラムに名前をつける
main_df.columns   
main_df.columns =["month","x","y","Temp"]   


#緯度、経度を配列の要素に変換
longitude=main_df["x"]+180
latitude=main_df["y"]+90
longi=map(round,longitude)
lati=map(round,latitude)
longi=map(int,longi)
lati=map(int,lati)                                             #偶数値の場合roundからのintで四捨五入可能
lons, lats = np.meshgrid(list(longi), list(lati))  #listしないと、iteratorという型で読まれてしまう


#地図の描画
#from mpl_toolkits.basemap import Basemap
#map = Basemap(projection='robin',lat_0=90, lon_0=180, resolution='c')
#map.drawcoastlines(color="white")
#map.drawmeridians(np.arange(30, 360, 60))
#map.drawparallels(np.arange(10, 180, 40))

z=main_df["Temp"]
#zz = np.reshape(z, (46, 91))
z=lons+latsf

plt.contourf(lons,lats,z)
plt.show()




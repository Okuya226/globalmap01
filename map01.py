import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
map = Basemap(projection='robin',lat_0=0, lon_0=0,
              resolution='c')
map.drawcoastlines(color="white")
map.drawmeridians(np.arange(-150, 180, 60))
map.drawparallels(np.arange(-80, 90, 40))
fnameF='fig_basemap.png'
plt.savefig(fnameF, bbox_inches="tight", pad_inches=0.2)
plt.show()


exit()
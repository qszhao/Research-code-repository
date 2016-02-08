
# coding: utf-8

# In[328]:

from skimage import io
import numpy as np


# In[329]:

# Read
f142000 = io.imread('/Users/qszhao/Dropbox/AGU research/NTL-intercalibration1/F152007.v4b_web.stable_lights.avg_vis_clip.tif')
f152000 = io.imread('/Users/qszhao/Dropbox/AGU research/NTL-intercalibration1/F162007.v4b_web.stable_lights.avg_vis_clip.tif')
f14152000 = np.zeros((173,272))


# In[330]:

column = len(f142000[0])
print column


# In[331]:

row = len(f142000)
print row


# In[332]:

for i in range(row):
    for j in range(column):
        f14152000[i][j] = (f152000[i][j] + f142000[i][j])/2
        if f152000[i][j] == 0 and f142000[i][j] != 0:
            f14152000[i][j] == 0
        if f152000[i][j] == 0 and f142000[i][j] == 0:
            f14152000[i][j] == 0
            
print f14152000


# In[333]:

np.max(f14152000)


# In[334]:

io.imsave('/Users/qszhao/Dropbox/AGU research/NTL-intercalibration2/F15162007.v4b_web.stable_lights.avg_vis_clip.tif',f14152000)


# In[ ]:




# In[ ]:




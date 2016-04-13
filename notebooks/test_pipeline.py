
# coding: utf-8

# # are you in the right git branch?
# As long as the dynamic min_samples feature is not merged into `master`, make sure your code
# is at the right branch before trying to test dynamic samples.

# In[ ]:

cd ~/Dropbox/CTX_to_jpg/pipeline_check/


# In[ ]:

from glob import glob

fnames = glob('*.pdf')

ids = [i.split('_')[0] for i in fnames]
ids[:5]


# In[ ]:

from planet4 import clustering, io, markings, helper_functions as hf
from pathlib import Path


# In[ ]:

path = Path("/Users/klay6683/data/planet4/ice_free_check")
path.mkdir(exist_ok=True)
cm = clustering.ClusteringManager(fnotched_dir=path,
                                 include_angle=True, include_distance=False, 
                                 include_radius=False, eps=10, min_distance=20)


# In[ ]:

cm.cluster_image_name('ESP_022699_0985')


# In[ ]:

from planet4 import plotting


# In[ ]:

db = io.DBManager()


# In[ ]:

data = db.get_image_name_markings('ESP_022699_0985')


# In[ ]:

data.info()


# In[ ]:

data[data.marking=='blotch'].info()


# In[ ]:




# In[ ]:

from ipyparallel import Client
c = Client()


# In[15]:

def process_imgid(id_):
    import matplotlib.pyplot as plt
    from planet4 import plotting, clustering
    from pathlib import Path
    path = Path("/Users/klay6683/data/planet4/pipelinecheck3")
    cm = clustering.ClusteringManager(fnotched_dir=path)
    cm.cluster_image_id(id_)
    plotting.plot_image_id_pipeline(id_, datapath=path, save=True)
#     plt.close('all')
    return id_


# In[16]:

get_ipython().magic('matplotlib nbagg')


# In[17]:

process_imgid('1f0')


# In[18]:

p1 = (221.79, 508.936)
p2 = (232, 517)


# In[19]:

from scipy.linalg import norm


# In[23]:

dp = np.array(p1) - np.array(p2)


# In[24]:

dp


# In[25]:

norm(dp)


# In[ ]:

recheck_ids = ['1dn','1k3','1e4','1fe','1aa','225','1pr','19g']
for imid in recheck_ids:
    print(imid)
    cm.cluster_image_id(imid)
    plotting.plot_image_id_pipeline(imid, datapath=path, save=True)


# In[ ]:

db = io.DBManager()
data = db.get_image_id_markings('1fe')


# In[ ]:

data.classification_id.nunique()


# In[ ]:

plotting.plot_finals(imid, _dir=path)


# In[ ]:

plotting.plot_raw_blotches(imid)


# In[ ]:

from planet4.plotting import blotches_all, fans_all


# In[ ]:

import seaborn as sns
sns.set_context('notebook')
blotches_all(imid)


# In[ ]:

fans_all(imid)


# In[ ]:

lbview = c.load_balanced_view()


# In[ ]:

import nbtools.multiprocessing as mptools


# In[ ]:

results = lbview.map_async(process_imgid, ids)


# In[ ]:

mptools.nb_progress_display(results, ids)


# In[ ]:




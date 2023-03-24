#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Memory reference string
mem_ref_str = [2, 4, 6, 8, 1, 1, 2, 9, 2, 8, 4, 6, 8, 9, 2, 1, 1, 9, 8, 1]

# Number of pages in memory
num_pages = 3

opt_buffer = []
opt_hits = 0
for i, page in enumerate(mem_ref_str):
    if page in opt_buffer:
        opt_hits += 1
    elif len(opt_buffer) < num_pages:
        opt_buffer.append(page)
    #else:
        #furthest_page = max((p, mem_ref_str[i:].index(p)) for p in opt_buffer)[0]
        #opt_buffer[opt_buffer.index(furthest_page)] = page
opt_hit_ratio = opt_hits / len(mem_ref_str)

print('OPT hit ratio',opt_hit_ratio)


# In[ ]:





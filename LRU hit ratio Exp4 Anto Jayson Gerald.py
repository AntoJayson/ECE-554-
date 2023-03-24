#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Memory reference string
mem_ref_str = [2, 4, 6, 8, 1, 1, 2, 9, 2, 8, 4, 6, 8, 9, 2, 1, 1, 9, 8, 1]

# Number of pages in memory
num_pages = 3

# lru replacement scheme
lru_buffer = []
lru_hits = 0
for page in mem_ref_str:
    if page in lru_buffer:
        lru_hits += 1
        lru_buffer.remove(page)
        lru_buffer.append(page)
    elif len(lru_buffer) < num_pages:
        lru_buffer.append(page)
    else:
        lru_buffer.pop(0)
        lru_buffer.append(page)
lru_hit_ratio = lru_hits / len(mem_ref_str)

# Print result
print("LRU hit ratio:", lru_hit_ratio)


# In[ ]:





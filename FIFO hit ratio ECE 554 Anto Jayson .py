#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Memory reference string
mem_ref_str = [2, 4, 6, 8, 1, 1, 2, 9, 2, 8, 4, 6, 8, 9, 2, 1, 1, 9, 8, 1]

# Number of pages in memory
num_pages = 3

# FIFO replacement scheme
fifo_buffer = []
fifo_hits = 0
for page in mem_ref_str:
    if page in fifo_buffer:
        fifo_hits += 1
    elif len(fifo_buffer) < num_pages:
        fifo_buffer.append(page)
    else:
        fifo_buffer.pop(0)
        fifo_buffer.append(page)
fifo_hit_ratio = fifo_hits / len(mem_ref_str)

# Print result
print("FIFO hit ratio:", fifo_hit_ratio)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[5]:


nama = "Ody Frans Wijaya"

#menghitung jumlah huruf pada nama lengkap
jumlah_huruf = len(nama.replace(" ",""))
print("Jumlah huruf dari nama lengkap (Ody Frans Wijaya) adalah : ", jumlah_huruf)

#menghitung jumlah huruf vokal pada nama lengkap
huruf_vokal = "aiueoAIUEO"
jumlah_vokal = len([char for char in nama if char in huruf_vokal])
print("Jumlah huruf vokal dari nama lengkap (Ody Frans Wijaya) adalah : ", jumlah_vokal)

#menghitung jumlah huruf konsonan pada nama lengkap
huruf_konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
jumlah_konsonan = len([huruf for huruf in nama if huruf in huruf_konsonan])

print("Jumlah huruf konsonan dari nama lengkap (Ody Frans Wijaya) adalah : ", jumlah_konsonan)


# In[ ]:





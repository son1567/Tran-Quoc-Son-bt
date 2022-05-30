#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = input('Nhập vào 2 số bất kỳ: ')
a = a.split(' ')
if int(a[1]) < int(a[0]):
    print('Số kết thúc cần lớn hơn số bắt đầu')
else:
    for i in range(int(a[0]),int(a[1])+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 5 == 0 and i % 3 != 0:
            print('Buzz')
        else:
            print(i)
            


# In[ ]:





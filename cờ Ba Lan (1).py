#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
tl=turtle.Turtle()
tl.speed(3)
width=480
height=360

tl.forward(width)
tl.right(90)
tl.forward(height)
tl.right(90)
tl.forward(width)
tl.right(90)
tl.forward(height)
tl.right(180)
tl.forward(height/2)
tl.fillcolor('red')
tl.begin_fill()
tl.left(90)
tl.forward(width)
tl.right(90)
tl.forward(height/2)
tl.right(90)
tl.forward(width)
tl.right(90)
tl.forward(height/2)
tl.end_fill()
tl.begin_fill()
turtle.done()


# In[ ]:





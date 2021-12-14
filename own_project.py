import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]


img = plt.imread('data/image_03.jpg')
fig, ax = plt.subplots()
ax.imshow(img, extent=[-5, 80, -5, 30])
ax.scatter(x, y, color="#ebb734")
st.pyplot(fig)


# img = plt.imread("rain.jpg")
# fig, ax = plt.subplots()
# ax.imshow(img, extent=[-5, 80, -5, 30])
# ax.scatter(TMIN, PRCP, color="#ebb734")
# plt.show()
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import altair as alt #pip install altair

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)
# st.line_chart(data)
# st.area_chart(data)
# st.bar_chart(data)
# plt.scatter(data['a'],data['b'])
# plt.title("Scatter")
# st.pyplot()

chart = alt.Chart(data).mark_circle().encode(
    x = 'a',y='c',tooltip =['a','c']
)
st.altair_chart(chart,use_container_width=True)

# st.graphviz_chart("""
# digraph(
# watch -> like
# like -> share
# share -> subscribe
# share -> watch                  
# )
# """)
# st.altair_chart(chart,use_container_width =True)

city = pd.DataFrame({
    'awesome cities' : ['Seoul', 'Busan'],
    'lat' : [37.5642135, 35.1379222],
    'lon' : [127.0016985, 129.05562775]
})


st.map(city)

# st.graphviz_chart("""
# digraph{
# watch -> like
# like -> share
# share -> subscribe
# share -> watch

# }

# """)

# st.altair_chart(chart,use_container_width =True)

# plt.scatter(data['a'],data['b'])
# plt.title("scatter")
# st.pyplot()

# st.line_chart(data)

# st.area_chart(data)

# st.bar_chart(data)

st.image("kpi.jpg")

# st.audio("data//demo.wav")

st.video("https://www.youtube.com/watch?v=9a1NDDcDQ7c")
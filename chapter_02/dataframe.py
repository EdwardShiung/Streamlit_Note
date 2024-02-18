import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt

# Writing Title
st.title("Text and Table Elements ")

# Header: Dataframe
st.header("Dataframe Display")

# Caption
st.caption("To show the basic method and display variable")

st.subheader("Data Preparation")

# Create one column of data
data = np.random.randn(30,10)
# print(data)

st.code('''
# Create one column of data

data = np.random.randn(1,10)
print(data)

    streamlit run dataframe.py [ARGUMENTS]
[[-0.35237825 -0.01602586  0.6202796   0.71229271 -0.67243104  2.08409883
   1.22476863 -1.10712136  1.99265185 -0.92390059]]

Explain np.random.randn

Numpy is very useful library, which has lots of modules, such as random.
- Random modules include other funcitons:
    - randn : 它會返回一個或多個樣本，具有標準常態分佈（平均值為0，標準差為1）。在這個特定的程式碼中，
    - np.random.randn(1,10)生成了一個1行10列的NumPy陣列，其中的元素是從標準常態分佈中隨機取樣得到的

其餘常見 functions:
    - random.random(): 返回一個隨機浮點數，範圍在0.0到1.0之間（包含0.0但不包含1.0）。
    - random.randint(a, b): 返回一個位於a和b之間（包含a和b）的隨機整數。
    - random.uniform(a, b): 返回一個位於a和b之間的隨機浮點數，包含a但不包含b。
    - random.choice(seq): 從非空序列seq中隨機返回一個元素。
    - random.shuffle(seq): 將序列seq中的元素隨機排列。

''')

## Dataframe
st.subheader("Dataframe")

st.text("Streamlit can display dataframe")

columns = ('col_no %d' % i for i in range(10))

# print(columns)

st.code('''
    columns = ('col_no %d' % i for i in range(10))
''')

df = pd.DataFrame(
    data,
    columns=columns
)

st.dataframe(df)

st.text("Streamlit also can hightlight the min value in each column")

# Hightlight the min in each column
st.dataframe(df.style.highlight_min(axis=0))

## Table
st.subheader("Table")
st.caption("The Table is very useful to display the data")

st.table(df)

st.text("The biggest difference is there is no option for scrolling and changing the dimensions of the table within the UI like we saw with data frames.")

## Metrics
st.subheader("Metrics")
st.caption("Streamlit also can display data with indicators using the metric() function.")
st.caption("This indicator helps user see any changes in the data easily.")

st.metric(label="Temperature", value="31", delta = "1.2")

## JSON
st.subheader("JSON")
data_json = { "Books" :
    [{
    "BookName" : "Python Testing with Selenium",
    "BookID" : "1",
    "Publisher" : "Apress",
    "Year" : "2021",
    "Edition" : "First",
    "Language" : "Python",
    },
    {
        "BookName": "Beginners Guide to Streamlit with Python",
        "BookID" : "2",
        "Publisher" : "Apress",
        "Year" : "2022",
        "Edition" : "First",
        "Language" : "Python"
    }]
}

st.json(data_json)

## Display Chart

# chart_data = np.random.logistic(10, 5, size=5)
# chart, ax = plt.subplots()
# ax.hist(chart_data, bins=15)
# "chart", chart

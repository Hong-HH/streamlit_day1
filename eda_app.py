# 여기에는 main이 안들어간다.
# 메인은 웹 페이지에서 단 하나만 들어간다.

import streamlit as st
import pandas as pd

# 파일을 분리했을때는 함수를 하나쓰고 거기에 작성하는 구나
def run_eda_app() :

    st.subheader('EDA 화면입니다.')

    df = pd.read_csv('data/iris.csv')

    st.dataframe(df)

    #상관계수 표시해보자
    st.dataframe( df.corr() )
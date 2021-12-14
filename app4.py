import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('data/iris.csv')

    # if st.button('데이터 보기') :
    #     st.dataframe(df)

    # name = 'Mike'

    # if st.button('대문자로') :
    #     st.write(name.upper())
    # if st.button('소문자로') :
    #     st.write(name.lower())

    st.dataframe(df)
    # 내가 누른것에 대한 정보는 변수로 받아주어야 한다.
    # 화면은 무조건 st가 담당하므로 찍어라. 
    status = st.radio('정렬을 선책하세요.', ['오름차순정렬', '내림차순정렬'])
    if status == '오름차순정렬' :
        st.dataframe(df.sort_values('petal_length'))
    elif status == '내림차순정렬' :
        st.dataframe(df.sort_values('petal_length', ascending=False))

    if st.checkbox("show / hide") :
        st.dataframe(df.head())
    else :
        st.write('데이터가 없습니다.')

    language = ['Python', 'C', 'Java','Go']
    # selectbox를 선택하면 그 함수자체가 선택한 결과값이 된다 예 'Go'
    my_choice = st.selectbox('좋아하는 언어를 선택하세요', language)
    if my_choice == 'C' :
        st.write('저는 C가 좋아요')
    elif my_choice == 'Python' :
        st.write('Python이 최고다!')

    # 여러개를 선택해보자
    choice_list = st.multiselect("여러개를 선택할 수 있습니다", language )
    # 웹브라우저에 출력
    #st.write(choice_list)
    # 여러분들이 디버깅을 하고싶으면, 파이썬의 print함수를 이용하면
    # 아래의 터미널에 출력이 됩니다.
    #print(choice_list)

    choice_list = st.multiselect('컬럼을 선택하세요', df.columns)
    #print(choice_list)
    #print(df[choice_list])
    st.dataframe(df[choice_list])
    # value 는 기본값이다. 
    age = st.slider('나이', 1, 100, value=30 )
    st.write('선택한 나이는 {}입니다'.format(age))

    # 일단은 with 뒤에 있는것을 처리하면 아래 문구도 실행하라
    # 차라리 함께라고 해석해도 좋다, 옆 문구를 실행하면 함께 아래 문구도 실행해라
    with st.expander('Hello') :
        st.text('안녕하세요')


## 새로고침 할때마다 실행된다.

if __name__ == '__main__' :
    #print(__name__)
    main()
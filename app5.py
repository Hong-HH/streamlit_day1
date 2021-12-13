# 위의 라이브러리는 설치치했으므로, 임포트만 하면 된다
import streamlit as st

# 웹 대시보드 개발 라이브버리인 스트림릿은 main 함수가 있어야한다.
def main() :
    st.title('Hello Streamlit. 웹 대시보드')
    st.title('헬로우')

    st.header('이 영역은 헤더 영역')

    st.success('성공했을 때의 메세지 영역')

if __name__=='__main__':
    main()
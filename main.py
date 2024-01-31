import streamlit as st # streamlit
import os
import tempfile

def get_price(file, price):
     # 파일이 업로드된 임시 경로 가져오기
    bytes_data = file.getvalue()
    filebite = len(bytes_data)

    tokens = filebite / 4
    ktoken_bucket = tokens / 1000
    total_price = ktoken_bucket * price
    return total_price


st.title("🤖GPT 활용 툴")

st.write("---")
st.header("GPT fine tuning 예상 비용 계산기")
st.write("📈토큰 당 비용은 변동될 수 있습니다. 현 시점(2024-01-31) 토큰당 가격은 다음과 같습니다")
st.write("1 토큰 = 4 byte로 계산하였으므로, 실제 비용과 차이가 있을 수 있습니다.")

price = st.number_input("토큰 당 비용을 입력해주세요 (단위 : $)", value=0.008)
file = st.file_uploader("학습시킬 파일을 업로드 해주세요",type=["json", "jsonl"])

if file is not None:
    if st.button("계산하기"):
        with st.spinner("잠시만 기다려주세요"):
            pred_price = get_price(file, price)
            
            st.write("예상 비용은 **%0.2f $**입니다."%pred_price)
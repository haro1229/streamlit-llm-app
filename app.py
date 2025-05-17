from dotenv import load_dotenv
import os
import streamlit as st
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.title("Lesson21: Streamlitを活用したWebアプリ開発")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["運動に関する相談", "睡眠に関する相談"]
)

st.divider()

if selected_item == "運動に関する相談":
    input_message = st.text_input(label="運動に関する相談内容を入力してください。")
    if st.button("相談を開始する") and input_message:
        with st.spinner("回答を生成中..."):
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "あなたは運動に関するアドバイザーです。安全なアドバイスを提供してください。"},
                    {"role": "user", "content": input_message}
                ],
                temperature=0.5
            )
            st.write("アドバイス:")
            st.write(completion.choices[0].message.content)

if selected_item == "睡眠に関する相談":
    input_message = st.text_input(label="睡眠に関する相談内容を入力してください。")
    if st.button("相談を開始する") and input_message:
        with st.spinner("回答を生成中..."):
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "あなたは睡眠に関するアドバイザーです。安全なアドバイスを提供してください。"},
                    {"role": "user", "content": input_message}
                ],
                temperature=0.5
            )
            st.write("アドバイス:")
            st.write(completion.choices[0].message.content)
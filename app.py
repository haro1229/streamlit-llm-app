from dotenv import load_dotenv
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# ローカル環境用の.env読み込み
try:
    load_dotenv()
except:
    pass

# APIキーの取得試行
api_key = os.environ.get("OPENAI_API_KEY")

# APIキーが設定されているか確認
if not api_key:
    st.error("OpenAI APIキーが設定されていません。")
    st.info("Streamlit Cloudをご利用の場合は、アプリの設定でシークレット'OPENAI_API_KEY'を追加してください。")
    st.stop()

st.title("Lesson21: Streamlitを活用したWebアプリ開発")

# LangChainを使って専門家に相談する関数
def ask_expert(input_text, expert_type):
    # LLMの初期化
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    
    # 専門家の種類に応じたシステムメッセージを設定
    if expert_type == "運動に関する相談":
        system_content = "あなたは運動に関するアドバイザーです。安全なアドバイスを提供してください。"
    else:  # 睡眠に関する相談
        system_content = "あなたは睡眠に関するアドバイザーです。安全なアドバイスを提供してください。"
    
    # メッセージの作成
    messages = [
        SystemMessage(content=system_content),
        HumanMessage(content=input_text)
    ]
    
    # LLMを呼び出して回答を生成
    result = llm(messages)
    
    return result.content

# UI部分
selected_item = st.radio(
    "動作モードを選択してください。",
    ["運動に関する相談", "睡眠に関する相談"]
)

st.divider()

# 選択された専門家に応じた入力フォームを表示
input_label = f"{selected_item}内容を入力してください。"
input_message = st.text_input(label=input_label)

if st.button("相談を開始する") and input_message:
    with st.spinner("回答を生成中..."):
        # 関数を呼び出して回答を取得
        response = ask_expert(input_message, selected_item)
        
        # 回答を表示
        st.write("アドバイス:")
        st.write(response)
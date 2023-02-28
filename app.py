import openai_secret_manager
import openai
import streamlit as st

# 配置OpenAI API Key
openai.api_key = openai_secret_manager.get_secret("openai")["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"]
MODEL_ID = "davinci"

# Streamlit应用程序
st.set_page_config(page_title="Chatbot Demo")

st.title("Chatbot Demo")

# 定义聊天框
st.sidebar.subheader("Chat")
user_input = st.sidebar.text_input("You", "")
bot_output = st.sidebar.empty()

# 与OpenAI模型进行交互，获取回复
if st.sidebar.button("Send"):
    # 调用OpenAI模型生成回复
    response = openai.Completion.create(
        engine=MODEL_ID,
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # 提取回复
    bot_response = response.choices[0].text.strip()
    # 更新聊天框
    bot_output.text(bot_response)

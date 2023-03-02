import openai
import streamlit as st

# 设置OpenAI API密钥
openai.api_key = "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"

# 定义应用程序标题和文本输入框
st.title("OpenAI文本生成应用程序")
input_text = st.text_area("请输入文本", "")

# 处理提交按钮点击事件
if st.button("提交"):
    # 调用OpenAI API
    prompt = input_text.strip()
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60
    )
    # 显示生成的文本
    st.write("生成的文本：")
    st.write(response.choices[0].text.strip())

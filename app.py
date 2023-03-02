import streamlit as st
import openai
openai.api_key = "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"

# 定义输入框和提交按钮
input_text = st.text_area("请输入文本", "")
submit_button = st.button("提交")

# 处理提交按钮点击事件
if submit_button:
    # 调用OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text,
        max_tokens=60
    )
    # 显示结果
    st.write("生成的文本：")
    st.write(response.choices[0].text)

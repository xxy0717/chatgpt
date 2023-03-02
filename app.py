import streamlit as st
import openai
import toml

# 读取 secrets.toml 文件中的 OpenAI API 密钥
secrets = toml.load("secrets.toml")
openai.api_key = secrets["openai"]["api_key"]


# 设置OpenAI API密钥
#if "OPENAI_API_KEY" not in st.secrets:
#    st.error("请在Streamlit Secrets中设置OpenAI API密钥")
#else:
#    openai.api_key = st.secrets["OPENAI_API_KEY"]

# 输入框
text = st.text_input("请输入文本：")

# 提交按钮
if st.button("提交"):
    try:
        # 调用OpenAI API生成文本
        response = openai.Completion.create(
            engine="davinci",
            prompt=text,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # 输出结果
        st.write(response.choices[0].text)
    except openai.Error as e:
        st.error("OpenAI API调用错误：" + str(e))
    print("OpenAI API调用错误：", e)

        

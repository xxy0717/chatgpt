import openai
import streamlit as st

# 设置OpenAI API密钥
openai.api_key = "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"

# 定义主函数
def main():
    # 设置应用程序标题
    st.title("Chat with GPT-3")

    # 显示输入框，以获取用户输入
    prompt = st.text_input("You: ", "")

    # 当用户点击“Send”按钮时，调用OpenAI API，并显示响应
    if st.button("Send"):
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=60
            )
            message = response.choices[0].text.strip()
            st.text_area("GPT-3:", message)
        except Exception as e:
            st.error(e)

# 调用主函数
if __name__ == "__main__":
    main()

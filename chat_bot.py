import requests
import json

# 你的API Key（替换成你自己的）
API_KEY = "key密钥"

# 智谱AI的API地址
URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# 用于保存对话历史
messages = []


def get_access_token():
    """获取访问令牌（智谱API需要）"""
    # 智谱使用JWT认证，这里简化处理
    # 直接使用API Key作为Bearer Token
    return API_KEY


def chat_with_glm(user_input):
    """调用智谱API，发送消息并获取回复"""

    # 将用户输入加入对话历史
    messages.append({"role": "user", "content": user_input})

    # 请求头
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # 请求体
    data = {
        "model": "glm-4-flash",  # 免费模型
        "messages": messages,
        "stream": False
    }

    try:
        # 发送POST请求
        response = requests.post(URL, headers=headers, json=data, timeout=30)

        # 检查状态码
        if response.status_code == 200:
            result = response.json()
            # 提取AI的回复
            ai_reply = result["choices"][0]["message"]["content"]
            # 将AI回复加入对话历史
            messages.append({"role": "assistant", "content": ai_reply})
            return ai_reply
        else:
            return f"错误：{response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"网络错误：{e}"


def main():
    """主函数：命令行聊天机器人"""
    print("=" * 50)
    print("🤖 智谱AI 命令行聊天机器人")
    print("=" * 50)
    print("输入 'quit' 或 'exit' 退出")
    print("输入 'clear' 清空对话历史")
    print("-" * 50)

    while True:
        # 获取用户输入
        user_input = input("\n👤 你: ").strip()

        # 退出条件
        if user_input.lower() in ['quit', 'exit']:
            print("👋 再见！")
            break

        # 清空历史
        if user_input.lower() == 'clear':
            messages.clear()
            print("✅ 对话历史已清空")
            continue

        # 空输入跳过
        if not user_input:
            continue

        # 调用AI并显示回复
        print("🤖 AI: ", end="", flush=True)
        reply = chat_with_glm(user_input)
        print(reply)


if __name__ == "__main__":
    main()
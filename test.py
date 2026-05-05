from zhipuai import ZhipuAI

# 把下面这行引号里的内容换成你的API Key
client = ZhipuAI(api_key="1017a85ed2874e23983ac4ec8b17f951.FvXi975NPHkrEgQq")

response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "user", "content": "你好，请用一句话介绍你自己"}
    ],
)

print(response.choices[0].message.content)
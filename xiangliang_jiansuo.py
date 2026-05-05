from zhipuai import ZhipuAI
import numpy as np

client=ZhipuAI(api_key='1017a85ed2874e23983ac4ec8b17f951.FvXi975NPHkrEgQq')

#把文档转成向量存起来
#创建一个空列表，存储文档
documents=[
    "苹果手机怎麽样",
    "香蕉好吃吗",
    "如何修理电脑"
]
#创建空列表，存储文档与它对应的向量，格式为字典
corpus=[]

#开始循环
for doc in documents:
    #调用智谱api的embedding.create方法，将当前文档的doc发送给智谱服务器
    response=client.embeddings.create(
        #指定用哪个嵌入模型，-3也可以
        model="embedding-2",
        #要转成向量的文本
        input=doc

    )
    #取出第一个结果向量
    vector=response.data[0].embedding
    #将当前文档与它的向量打包成字典添加到corpus
    corpus.append({"text":doc,"vector":vector})
    print(f"已存入：{doc}")


#写余弦相似度函数
#定义函数，接受两个参数
def cosine_similarity(vec_a, vec_b):
    """计算两个向量的余弦相似度，值越接近1越相似"""
    #把传入的普通数据转换为numpy数组格式，便于直接用数学函数
    vec_a = np.array(vec_a)
    vec_b = np.array(vec_b)
    #计算点积
    dot = np.dot(vec_a, vec_b)
    #计算两个向量的模长
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    #防错处理，模长为0则返回0
    if norm_a == 0 or norm_b == 0:
        return 0.0
    #余弦相似度核心公式（点积/（模长a*模长b））
    return dot / (norm_a * norm_b)



#写检索函数
#定义函数，接受两个参数，(用户输入的查询文本，返回两个相似结果)
def search(query_text, top_k=2):
    # 1. 把查询转成向量
    #调用智谱api,把query_text发送过去
    response = client.embeddings.create(
        #用此模型转成向量
        model="embedding-2",
        input=query_text
    )
    #从返回结果中取出向量，存入query_vec
    query_vec = response.data[0].embedding

    # 2. 遍历所有文档算相似度
    #创建空列表，准备存放结果
    results = []
    #循环取出corpus里的每个文档
    for item in corpus:
        #调用余弦相似度函数，比较查询向量和当前文档向量的相似度
        sim = cosine_similarity(query_vec, item["vector"])
        #把文档原文和计算出的相似度打包成字典存入results
        results.append({"text": item["text"], "similarity": sim})

    # 3. 按相似度从高到低排序
    results.sort(key=lambda x: x["similarity"], reverse=True)

    # 4. 返回前top_k个
    return results[:top_k]



#测试运行
#定义变量，存储要搜索的问题文本
query = "华为手机好用吗"
#调用函数，查询query，返回最相似的两个结果
results = search(query, top_k=2)

print(f"\n搜索: {query}")
print("-" * 30)

#从列表依次取出每个结果（字典）
for r in results:
    print(f"文档: {r['text']}")#打印文本原文
    print(f"相似度: {r['similarity']:.4f}\n")#打印相似度
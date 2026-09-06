import streamlit as st
import requests
import os
import base64
import time

# 智谱 API Key
ZHIPU_API_KEY = os.getenv('ZHIPU_API_KEY', '1017a85ed2874e23983ac4ec8b17f951.FvXi975NPHkrEgQq')


def generate_image(prompt):
    """调用智谱 CogView 生成图片"""
    if not ZHIPU_API_KEY:
        return None, "请先设置 ZHIPU_API_KEY"

    try:
        url = "https://open.bigmodel.cn/api/paas/v4/images/generations"
        headers = {
            "Authorization": f"Bearer {ZHIPU_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "cogview-3-plus",
            "prompt": prompt,
            "size": "1024x1024"
        }

        response = requests.post(url, headers=headers, json=data, timeout=60)

        if response.status_code != 200:
            error_data = response.json()
            error_msg = error_data.get("error", {}).get("message", f"API 错误: {response.status_code}")
            return None, error_msg

        result = response.json()

        # CogView 返回 base64 图片数据
        if "data" in result and len(result["data"]) > 0:
            image_data = result["data"][0]
            if "url" in image_data:
                return image_data["url"], None
            elif "b64_json" in image_data:
                return image_data["b64_json"], None

        return None, "未获取到图片数据"
    except requests.exceptions.Timeout:
        return None, "生成超时，请重试（AI 生图通常需要 10-30 秒）"
    except Exception as e:
        return None, str(e)


def enhance_prompt(keyword):
    """根据关键词生成更适合公众号的提示词"""
    # 公众号配图风格模板
    templates = [
        f"一幅适合微信公众号配图的插画，主题是{keyword}，清新文艺风格，色彩柔和，简洁大方",
        f"微信公众号头图，{keyword}主题，扁平插画风格，现代简约，色彩温暖",
        f"一幅关于{keyword}的精美插画，适合文章配图，清新自然，构图简洁",
        f"中国风插画，{keyword}主题，水墨风格与现代设计结合，适合公众号推送",
    ]
    return templates


def main():
    st.set_page_config(
        page_title="公众号配图助手 - AI 生图",
        page_icon="🎨",
        layout="wide"
    )

    # 自定义样式
    st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🎨 公众号配图助手 - AI 生图")
    st.markdown("**输入文章主题，AI 自动生成原创配图，零版权问题**")
    st.markdown("---")

    # 检查 API Key
    if not ZHIPU_API_KEY:
        st.warning("⚠️ 请先设置智谱 API Key")
        st.markdown("""
        """)
        st.stop()

    # 输入区域
    keyword = st.text_input(
        "📝 输入文章主题",
        placeholder="例如：校园生活、毕业季、青春回忆...",
        label_visibility="visible"
    )

    # 风格选择
    st.markdown("**选择配图风格：**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        style1 = st.button("🌸 清新文艺", key="style1")
    with col2:
        style2 = st.button("🎨 扁平插画", key="style2")
    with col3:
        style3 = st.button("🖌️ 中国风", key="style3")
    with col4:
        style4 = st.button("📷 写实摄影", key="style4")

    # 自定义提示词（可选）
    custom_prompt = st.text_area(
        "✏️ 自定义提示词（可选，留空则自动生成）",
        placeholder="描述你想要的图片效果，越详细越好...",
        height=80
    )

    # 快捷标签
    st.markdown("**快捷主题：**")
    quick_tags = ["校园生活", "毕业季", "青春回忆", "友情时光", "学习奋斗", "四季风景", "节日祝福", "美食分享"]
    cols = st.columns(len(quick_tags))
    for i, tag in enumerate(quick_tags):
        with cols[i]:
            if st.button(tag, key=f"tag_{i}"):
                st.session_state['keyword'] = tag
                st.rerun()

    # 同步关键词
    if 'keyword' in st.session_state:
        keyword = st.session_state['keyword']
        del st.session_state['keyword']

    # 生成按钮
    generate_clicked = st.button("🎨 生成配图", type="primary")

    if keyword and generate_clicked:
        # 确定提示词
        if custom_prompt:
            prompt = custom_prompt
        else:
            # 根据风格选择模板
            if style1:
                prompt = f"一幅适合微信公众号配图的插画，主题是{keyword}，清新文艺风格，色彩柔和温暖，水彩画质感，简洁大方"
            elif style2:
                prompt = f"微信公众号头图，{keyword}主题，扁平插画风格，现代简约设计，色彩明快，构图饱满"
            elif style3:
                prompt = f"中国风插画，{keyword}主题，水墨画与现代设计融合，意境优美，适合公众号推送配图"
            elif style4:
                prompt = f"一张关于{keyword}的高质量摄影照片，自然光线，构图精美，适合微信公众号文章配图"
            else:
                prompt = f"一幅适合微信公众号配图的插画，主题是{keyword}，清新文艺风格，色彩柔和，简洁大方"

        # 显示使用的提示词
        st.info(f"🤖 提示词：{prompt}")

        # 生成图片
        with st.spinner("🎨 AI 正在生成配图，通常需要 10-30 秒..."):
            start_time = time.time()
            image_url, error = generate_image(prompt)
            elapsed = time.time() - start_time

        if error:
            st.error(f"生成失败：{error}")
        elif image_url:
            st.success(f"✅ 生成成功！耗时 {elapsed:.1f} 秒")
            st.markdown("---")

            # 显示图片
            if image_url.startswith("http"):
                st.image(image_url, use_container_width=True)
                st.markdown(f"### 📥 [点击下载原图]({image_url})")
            else:
                # base64 格式
                img_data = base64.b64decode(image_url)
                st.image(img_data, use_container_width=True)
                st.download_button(
                    label="📥 下载图片",
                    data=img_data,
                    file_name=f"{keyword}_配图.png",
                    mime="image/png"
                )

            st.markdown("---")
            st.caption("💡 如果不满意，可以修改提示词重新生成，或换一种风格试试")

            # 一键重新生成
            if st.button("🔄 换一张"):
                with st.spinner("🎨 重新生成中..."):
                    image_url, error = generate_image(prompt)
                if image_url:
                    if image_url.startswith("http"):
                        st.image(image_url, use_container_width=True)
                    else:
                        st.image(base64.b64decode(image_url), use_container_width=True)

    # 使用说明
    st.markdown("---")
    with st.expander("📌 使用说明"):
        st.markdown("""
        ### 关于 AI 生成图片
        1. **完全原创**：AI 生成的图片，零版权问题
        2. **风格可控**：通过提示词控制图片风格
        3. **生成时间**：通常 10-30 秒

        ### 提示词技巧
        - 越具体越好：`校园里樱花树下的学生，春天，阳光明媚`
        - 指定风格：`水彩画风格`、`扁平插画`、`中国风水墨`
        - 指定色调：`暖色调`、`冷色调`、`莫兰迪色系`
        - 指定构图：`横版构图`、`居中对称`、`留白`

        """)
if __name__ == "__main__":
    main()
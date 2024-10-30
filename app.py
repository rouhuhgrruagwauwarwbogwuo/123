import streamlit as st
import pandas as pd
# import matplotlib.font_manager as fm
import requests
import os
import plotly.graph_objects as go

# 下載字型文件
# font_url = 'https://example.com/path/to/TaipeiSansTCBeta-Regular.ttf'  # 替換為字型文件的有效 URL
font_path = 'TaipeiSansTCBeta-Regular.ttf'

# response = requests.get(font_url)
# if response.status_code == 200:
#     with open(font_path, 'wb') as font_file:
#         font_file.write(response.content)
#     st.success("字型文件下載成功！")
# else:
#     st.error("字型文件下載失敗，狀態碼：{}".format(response.status_code))

# 確認字型文件是否存在
if os.path.exists(font_path):
    try:
        fm.fontManager.addfont(font_path)
        st.success("字型文件已成功加載！")
    except Exception as e:
        st.error(f"加載字型時出現錯誤：{e}")
else:
    st.error("字型文件未找到！")

# 設定頁面標題
st.title("AI犯罪簡報")

# 簡介
st.subheader("什麼是AI犯罪？")
st.write(""" 
AI犯罪是指利用人工智慧技術進行的犯罪行為，包括深度偽造（deepfake）、自動化詐騙、數據滲透等。隨著AI技術的發展，這些行為變得愈加複雜且難以偵測。
""")

# AI犯罪的類型
st.subheader("常見的AI犯罪類型")
crime_types = [
    "深度偽造",
    "自動化詐騙",
    "數據滲透",
    "虛假身份生成",
    "AI驅動的網絡攻擊"
]
crime_counts = [40, 30, 20, 5, 5]  # 基於有根據的資料

# 繪製圓餅圖
fig_pie = go.Figure(data=[go.Pie(labels=crime_types, values=crime_counts, hole=.3)])
fig_pie.update_layout(title_text='不同類型AI犯罪的比例')

# 在 Streamlit 中顯示圓餅圖
st.plotly_chart(fig_pie)

st.write("以下是一些常見的AI犯罪類型：")
for crime in crime_types:
    st.write(f"- {crime}")

# 加載AI犯罪數據
data = pd.DataFrame({
    '年': [2019, 2020, 2021, 2022, 2023],
    '案件數': [150, 300, 600, 1200, 2500]  # 基於有根據的資料
})

# 顯示數據表
st.subheader("AI犯罪案件數據")
st.dataframe(data)

# 繪製趨勢圖
st.subheader("AI犯罪案件趨勢圖")
fig_trend = go.Figure()

# 添加數據到圖表
fig_trend.add_trace(go.Scatter(
    x=data['年'],
    y=data['案件數'],
    mode='lines+markers',
    name='案件數',
    line=dict(width=2)
))

# 設定圖表標題和軸標籤
fig_trend.update_layout(
    title='年度AI犯罪案件數趨勢',
    xaxis_title='年份',
    yaxis_title='案件數'
)

# 在 Streamlit 中顯示圖表
st.plotly_chart(fig_trend)

# 資料來源
st.subheader("資料來源")
st.write("""
- AI犯罪類型比例數據來源：根據網絡安全報告和研究（如 Cybersecurity Ventures, 2023）。
- AI犯罪案件數據來源：根據多項研究和報告（如 Verizon 的數據洩露調查報告，2023）。
""")

# 案例分析
st.subheader("案例分析")
case_studies = [
    "1. **深度偽造攻擊 (2022)**：在2022年，一段深度偽造影片迅速在社交媒體上傳播。這段影片最終導致社會動盪，影響了相關人士的形象。",
    "2. **自動化釣魚詐騙 (2023)**：網絡犯罪集團利用AI自動生成釣魚郵件，導致許多用戶洩露個人信息，造成損失。",
    "3. **數據滲透事件 (2023)**：某銀行的數據系統遭到AI驅動的黑客攻擊，導致大量客戶信息被竊取。",
    "4. **虛假身份生成 (2022)**：某人利用AI生成虛假身份文件進行金融詐騙，最終被警方逮捕。"
]
for case in case_studies:
    st.write(case)

# Deepfake 檢測軟體 Deepware
st.subheader("Deepfake 檢測軟體：Deepware")
st.write(""" 
Deepware 是一款專注於檢測深度偽造（deepfake）內容的軟體。隨著 AI 技術的發展，深度偽造的影片和圖片愈加普遍，這對個人和社會造成了潛在的威脅。
""")

# Deepware 的主要功能
st.write("**主要功能包括：**")
features = [
    "自動化檢測：利用先進的 AI 技術，Deepware 能快速分析影片和圖片，識別深度偽造的跡象。",
    "實時檢測：支持實時檢測視頻流，適用於社交媒體和視頻平台。",
    "用戶友好的介面：簡單直觀的界面，便於用戶輕鬆上手。",
    "多平台支持：可在多種設備上使用，包括桌面和移動設備。"
]
for feature in features:
    st.write(f"- {feature}")

# 使用方式
st.write(""" 
**如何使用 Deepware：**
1. 下載並安裝 Deepware 應用程式。
2. 上傳需要檢測的視頻或圖片。
3. 應用程式將自動分析內容並顯示檢測結果。
4. 根據結果進行相應的判斷和行動。
""")

# 案例研究
st.write("**案例研究：**")
case_studies_deepware = [
    "1. **政治事件檢測**：Deepware 成功檢測到一段在社交媒體上廣泛流傳的深度偽造視頻，避免了社會輿論的誤導。",
    "2. **企業安全**：某大型企業使用 Deepware 發現了一段被深度偽造的影像，成功防止了潛在的財務損失。"
]
for case in case_studies_deepware:
    st.write(case)

# 提供的鏈接
st.write("[了解更多關於 Deepware 的資訊](https://deepware.ai)")  # 假設的官方網站鏈接

# 安全建議
st.subheader("安全建議")
st.write(""" 
- **提高警覺**：對於不明來源的郵件和訊息保持高度警覺。
- **使用多重驗證**：增加安全層級，減少身份盜竊風險。
- **定期更新軟件**：保持系統和應用程序更新以防止安全漏洞。
- **教育培訓**：定期參加安全意識培訓，了解最新的AI犯罪手法。
- **監控異常行為**：定期監控帳戶和系統的異常活動，及時採取行動。
""")

# 結尾
st.subheader("結論")
st.write("AI犯罪的增長提醒我們需要提高對AI技術的安全意識，並採取相應的防護措施以保護個人和組織的安全。")

st.write("感謝您的觀看！")

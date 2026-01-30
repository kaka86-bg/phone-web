import streamlit as st
from docx import Document
import io

# --- 🔐 パスワード認証機能 ---
# ここで「金庫の中のパスワード」と「入力されたパスワード」を照合します
password = st.text_input("パスワードを入力してください", type="password")
if password != st.secrets["MY_PASSWORD"]:
    st.warning("正しいパスワードを入力するとアプリが使えます。")
    st.stop()  # ここで処理を強制ストップ（これより下のコードは動きません）

# ------------------------------
# 👇 ここから下に、いつものアプリのコードを書く
# ------------------------------

st.title("📄 スマホでWord作成アプリ")
st.write("認証成功！ようこそ！")

# ユーザー入力欄
user_name = st.text_input("お名前", "山田 太郎")
report_content = st.text_area("報告内容", "ここに今週の業務報告を入力してください。")

# Wordを作る機能
def create_word_file(name, text):
    doc = Document()
    doc.add_heading('業務報告書', 0)
    doc.add_paragraph(f'作成者：{name}')
    doc.add_heading('【内容】', level=1)
    doc.add_paragraph(text)
    
    bio = io.BytesIO()
    doc.save(bio)
    return bio.getvalue()

# ボタン
if st.button('Wordファイルを作成！'):
    word_data = create_word_file(user_name, report_content)
    st.download_button(
        label="📥 Wordをダウンロード",
        data=word_data,
        file_name="my_report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

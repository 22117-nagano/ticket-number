import json
import os
import streamlit as st

st.set_page_config(
    page_title="整理番号ご案内 (150円)", page_icon="🍢", layout="centered"
)

DATA_FILE = "counter_150.json"


def load_counter():
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
      return json.load(f)
  return {"current": 1000}


def save_counter(data):
  with open(DATA_FILE, "w") as f:
    json.dump(data, f)


if "my_number_150" not in st.session_state:
  st.session_state.my_number_150 = None

st.title("🍢 1本（150円）整理番号")

if st.session_state.my_number_150:
  st.markdown("---")
  st.markdown(
      f"<h1 style='text-align: center; color: #ff4b4b; font-size:"
      f" 90px;'>{st.session_state.my_number_150}</h1>",
      unsafe_allow_html=True,
  )
  st.markdown("---")
  st.success("🎉 整理番号の発行が完了しました！")
  st.warning(
      "⚠️ **この画面をスクリーンショット保存してください**\n"
      "商品の受け取りの際、この番号画面を受付にご提示ください。"
  )
else:
  st.write("下のボタンを押すと、あなたの整理番号（1000番台）が発行されます。")
  st.info("※誤タップによる重複を防ぐため、ボタンは一度だけ押してください。")
  st.markdown("---")

  if st.button("🎫 整理番号を発行する", use_container_width=True):
    data = load_counter()
    data["current"] += 1
    save_counter(data)
    st.session_state.my_number_150 = data["current"]
    st.rerun()

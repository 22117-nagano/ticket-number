import json
import os
import streamlit as st

st.set_page_config(
    page_title="イベント前売り券 予約システム", page_icon="🎫", layout="centered"
)

# 整理番号のカウンターを保存するファイル名
DATA_FILE = "ticket_counter.json"


def load_counter():
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
      return json.load(f)
  # 初期値：150円は1000（次が1001）、250円は2000（次が2001）、300円は3000（次が3001）
  return {"150": 1000, "250": 2000, "300": 3000}


def save_counter(data):
  with open(DATA_FILE, "w") as f:
    json.dump(data, f)


# このブラウザ（このお客さん）ですでに番号を発行したか管理する
if "my_ticket" not in st.session_state:
  st.session_state.my_ticket = None

st.title("🎫 イベント前売り券 予約ページ")

# 【パターンA】すでに番号が発行されている場合（誤タップ防止のためボタンを非表示）
if st.session_state.my_ticket:
  st.success("🎉 ご予約（番号の発行）が完了しました！")
  st.info(
      f"### あなたの整理番号：**{st.session_state.my_ticket['number']}**\n"
      f"選択商品: **{st.session_state.my_ticket['item_name']} ({st.session_state.price}円)**"
  )
  st.warning(
      "⚠️ **次のステップ**\n"
      "1. この画面（整理番号）を**スクリーンショット保存**してください。\n"
      "2. 主催者からの案内に沿って決済をお進めください。"
  )

  if st.button("最初に戻る（※誤って発行し直す場合はこちら）"):
    st.session_state.my_ticket = None
    st.rerun()

# 【パターンB】まだ商品を選んでいない場合
else:
  st.write("ご希望の商品を選んでください。")
  st.info("※誤タップによる重複を防ぐため、ボタンは一度だけ押してください。")
  st.markdown("---")

  # 150円 (1スタート)
  st.subheader("🐓 1本（150円）")
  if st.button("1本で申し込む", key="btn_150"):
    data = load_counter()
    data["150"] += 1
    save_counter(data)
    st.session_state.my_ticket = {
        "number": str(data["150"]),
        "item_name": "1本",
        "price": 150,
    }
    st.rerun()

  st.markdown("---")

  # 250円 (2スタート)
  st.subheader("🐓 もも3本（250円）")
  if st.button("もも3本で申し込む", key="btn_250"):
    data = load_counter()
    data["250"] += 1
    save_counter(data)
    st.session_state.my_ticket = {
        "number": str(data["250"]),
        "item_name": "もも3本",
        "price": 250,
    }
    st.rerun()

  st.markdown("---")

  # 300円 (3スタート)
  st.subheader("🐓 三種3本（300円）")
  if st.button("三種3本で申し込む", key="btn_300"):
    data = load_counter()
    data["300"] += 1
    save_counter(data)
    st.session_state.my_ticket = {
        "number": str(data["300"]),
        "item_name": "三種3本",
        "price": 300,
    }
    st.rerun()

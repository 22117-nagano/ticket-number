import streamlit as st

st.set_page_config(
    page_title="前売り券 (1本)", page_icon="🐓", layout="centered"
)

st.title("🎫 デジタル前売り券（お引換券）")
st.markdown("---")

# 商品名を大きく表示
st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b; font-size:"
    " 45px;'>🐓 もも1本 前売り券</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 20px; color: #666;'>金額: 150円</p>",
    unsafe_allow_html=True,
)

st.markdown("---")
st.success("✅ 決済確認済み（有効なチケット）")
st.warning(
    "⚠️ **受取時のご注意**\n"
    "この画面を当日の受付スタッフにご提示ください。"
)

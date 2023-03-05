import streamlit as st
import spacy
from spacy import displacy

st.sidebar.title("文章解析アプリ")
st.sidebar.write("SpaCyを使って文章を解析します。")

st.sidebar.write("")

text = st.text_area("解析する文章", "文章を入力してください。")
nlp = spacy.load("ja_ginza")
doc = nlp(text)

method = st.sidebar.radio("解析方法を選択してください。",
                          ("文章ごとに分割", "名詞の抽出", "品詞と依存関係", "依存関係の可視化", "固有表現の抽出"))

if method == "文章ごとに分割":
    for sentence in doc.sents:
        st.caption(sentence)

elif method == "名詞の抽出":
    for noun in doc.noun_chunks:
        st.caption(noun)

elif method == "品詞と依存関係":
    for token in doc:
        st.caption(token.text + " / " + token.pos_ + " / " + token.dep_)

elif method == "依存関係の可視化":
    svg = displacy.render(doc, style="dep")
    st.image(svg)

elif method == "固有表現の抽出":
    html = displacy.render(doc, style="ent")
    st.markdown(html, unsafe_allow_html=True)

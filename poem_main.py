import streamlit as st
from poem_generator import generate_poem, rewrite_poem

st.set_page_config(page_title="AI Poem Generator", page_icon="📝")

st.title("📝 GenAI Poem Generator")

# -------- INPUT SECTION --------
theme = st.text_input("Theme", "Nature")
emotion = st.selectbox("Emotion", ["Love", "Sadness", "Hope", "Joy", "Melancholy"])
poem_type = st.selectbox("Poem Type", ["Free Verse", "Haiku", "Sonnet"])
language = st.selectbox("Language", ["English", "Kannada", "Hindi"])
kannada_meter = None
if language == "Kannada":
    kannada_meter = st.selectbox(
        "Kannada Poetic Meter (ಛಂದಸ್ಸು)",
        ["Vachana Style", "Traditional Rhythmic", "Modern Free Verse"]
    )
length = st.selectbox("Length", ["Short", "Medium", "Long"])

# GENERATE POEM 
if st.button("Generate Poem"):
    with st.spinner("Writing your poem..."):
        poem = generate_poem(theme, emotion, poem_type, language, length)
        st.session_state.poem = poem
        st.text_area("Generated Poem", poem, height=300)

# Display
if "poem" in st.session_state:
    st.subheader("✨ Generated Poem")
    st.text_area("", st.session_state.poem, height=250)

    st.download_button(
        "Download Poem",
        st.session_state.poem,
        file_name="poem.txt"
    )

#Rewrite
if "poem" in st.session_state:
    st.markdown("---")
    st.subheader("🔁 Rewrite Poem")

    style = st.selectbox(
        "Rewrite Style",
        ["More Emotional", "More Romantic", "More Classical", "More Modern"]
    )

    if st.button("Rewrite Poem"):
        with st.spinner("Rewriting poem..."):
            rewritten = rewrite_poem(st.session_state.poem,language, style)        
            st.text_area("Rewritten Poem", rewritten, height=300)
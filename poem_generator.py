import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm= ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

prompt_template = PromptTemplate(
    input_variables=["theme", "emotion", "poem_type", "language", "length"],
    template="""
    You are a skilled poet.

    Write a {poem_type} poem in {language}.
    Theme: {theme}
    Emotion: {emotion}
    Length: {length} stanzas.

    Instructions:
    - If language is English:
    - Use vivid imagery
    - Natural rhythm
    - Elegant poetic expressions

    - If language is Kannada:
    - Follow Kannada poetic rhythm (ಛಂದಸ್ಸು)
    - Use short rhythmic lines
    - Maintain internal rhyme (ಪ್ರಾಸ)
    - Use traditional Kannada poetic tone
    - Poem should be meaningful and deep
    - Avoid English words completely

    Make the poem emotionally rich and aesthetically pleasing.
    Return only the poem.
    """
)


def generate_poem(theme, emotion, poem_type, language, length):
    chain = prompt_template | llm
    response = chain.invoke({
        "theme": theme,
        "emotion": emotion,
        "poem_type": poem_type,
        "language": language,
        "length": length
    })
    return response.content

REWRITE_PROMPT = PromptTemplate(
    input_variables=["poem", "style"],
    template="""
    Rewrite the following poem in {style} style.
    Preserve the meaning but change tone and expression.

    Poem:
    {poem}
    Language: {language}

    Only return the rewritten poem.
    """
)

def rewrite_poem(poem, language, style):
    chain = REWRITE_PROMPT | llm
    response = chain.invoke({
        "poem": poem,
        "style": style,
        "language": language
    })
    return response.content
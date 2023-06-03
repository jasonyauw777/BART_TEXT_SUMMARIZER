import streamlit as st 
from transformers import pipeline

# def summarizeText(summarizer, txt):
#     summarized_text = summarizer(txt)[0]["summary_text"]
#     return summarized_text
@st.cache(ttl=60)
def load_summarizer():
    return pipeline("summarization", model = "jasonsurya0/BART_TWELVE")

def main():
    st.set_page_config(page_title="Automatic Text Summarizer With BART")
    # BART MODEL DEVELOPED 
    summarizer = load_summarizer()
    # ----HEADER
    st.subheader("Text Summarizer Built With BART")

    #-----Text Area
    txt = st.text_area('Input Text to Summarize', '''
        Amanda: I baked cookies. Do you want some? 
        Jerry: Sure! 
        Amanda: I'll bring you tomorrow :-) 
        ''', height = 180)

    if st.button('Summarize'):
        st.write("TEST")
        #st.write(summarizeText(summarizer, txt))
        #st.text_area('Summarized Text', summarizeText(summarizer, txt), height = 140)

if __name__=="__main__":
    main()



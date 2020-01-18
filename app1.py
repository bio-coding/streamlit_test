import streamlit as st

#NLP Pkgs

#Pkgs

def main():
    """NLP App with Streamlit"""
    st.title("Hello strealint")
    st.subheader("Natural processing")
    #Tokenization
    if st.checkbox("Show Tokens"):
        st.subheader("Tokenize your text")
        st.subheader("Tokenize 2")
        message = st.text_area("Enter your text", "Type here")
        if st.button("Analyse"):
            st.success(message.title())


    #Named Entry
    #Sentiment analysis
    #Text Sumarization


if __name__ == '__main__':
	main()



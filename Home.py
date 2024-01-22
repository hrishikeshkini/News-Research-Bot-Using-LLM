import streamlit as st

def main():

    st.set_page_config(
        page_title="FinScribe",
        page_icon="💵",
    )

    st.title("FinScribe Analytics Suite")

    st.subheader("Uncover Financial Insights from News Articles")
    st.write(
        "NewsAnalyzer is your intelligent financial news research assistant, designed to swiftly analyze news articles and provide dynamic insights through a chat interface."
    )

    st.subheader("Extract Knowledge from Financial PDFs with Ease")
    st.write(
        "PDFChatBot is a virtual companion within the FinScribe Analytics Suite, empowering you to upload financial PDFs, ask questions, and receive detailed responses to expedite your equity research."
    )

    st.subheader("Choose a Project")

    st.write(f'''
            <style>
                .button-container {{
                    display: flex;
                    justify-content: space-around;
                    margin-left: -100px;
                }}
                .project-button {{
                    padding: 15px 50px;
                    font-size: 20px;
                    background-color: #9b4caf;
                    color: white;
                    border: none;
                    border-radius: 35px;
                    cursor: pointer;
                }}
            </style>
            <div class="button-container">
                <a target="_self" href="https://personal-analyst.onrender.com/URL">
                    <button class="project-button">
                        News Analyzer
                    </button>
                </a>
                <a target="_self" href="https://personal-analyst.onrender.com/PDF">
                    <button class="project-button">
                        PDF Chat Bot
                    </button>
                </a>
            </div>
            ''',
            unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()

import streamlit as st
from utils.github_loader import download_repo
from utils.document_parser import load_and_split
from utils.vector_store import create_vectorstore
from utils.chatbot_chain import get_chain
from dotenv import load_dotenv

load_dotenv()

st.title("🤖 REPOT: Chat with any GitHub Repo")

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# To track if repo is indexed
if "repo_indexed" not in st.session_state:
    st.session_state.repo_indexed = False

repo_url = st.text_input("Enter GitHub Repository URL:")

# Clear previous state if new repo entered
if repo_url and not st.session_state.repo_indexed:
    if "vectorstore" in st.session_state:
        del st.session_state.vectorstore
    if "qa_chain" in st.session_state:
        del st.session_state.qa_chain
    st.session_state.chat_history = []
    st.session_state.repo_indexed = False

# Index repo and create chain if not done yet
if repo_url and not st.session_state.repo_indexed:
    try:
        with st.spinner("🔽 Downloading and indexing repo..."):
            repo_path = download_repo(repo_url)
            docs = load_and_split(repo_path)

            st.write(f"📄 Loaded {len(docs)} documents")
            for doc in docs:
                st.markdown(f"### Document: {doc.metadata['source']}")
                st.code(doc.page_content[:1000])  # Limit to 1000 chars for readability

            st.session_state.vectorstore = create_vectorstore(docs)
            st.write(f"🗃️ Vectorstore size: {st.session_state.vectorstore.index.ntotal}")

            st.session_state.qa_chain = get_chain(st.session_state.vectorstore)

            # Run initial summary query and display it with sources
            test_result = st.session_state.qa_chain(
                {
                    "question": "What is this repository about?",
                    "chat_history": [],
                }
            )
            st.markdown("## 📚 Repository Summary")
            st.write(test_result["answer"])

            st.markdown("### Sources for summary:")
            for doc in test_result["source_documents"]:
                st.markdown(f"- {doc.metadata.get('source', 'unknown')}")
                st.code(doc.page_content[:500])  # Show a snippet from source docs

            st.session_state.repo_indexed = True
            st.success("✅ Repo indexed! You can now ask questions below.")
    except Exception as e:
        st.error(f"Error loading repo: {e}")

# Show chat input box only after indexing is done
if st.session_state.repo_indexed:
    user_input = st.text_input("Ask a question about the repo:")

    if user_input:
        with st.spinner("Generating answer..."):
            result = st.session_state.qa_chain(
                {
                    "question": user_input,
                    "chat_history": st.session_state.chat_history,
                }
            )
            answer = result.get("answer", "No answer returned.")
            st.session_state.chat_history.append((user_input, answer))

            st.write("**Bot:**", answer)

            st.markdown("### Sources:")
            for doc in result.get("source_documents", []):
                st.markdown(f"- {doc.metadata.get('source', 'unknown')}")

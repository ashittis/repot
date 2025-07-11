from langchain_community.llms import LlamaCpp
from langchain.chains import ConversationalRetrievalChain


def get_chain(vectorstore):
    llm = LlamaCpp(
        model_path="models/mistral-7b-instruct-v0.1.Q4_0.gguf",
        temperature=0.7,
        max_tokens=512,
        n_ctx=2048,
        verbose=True,
    )
    # Enable returning source docs for transparency
    return ConversationalRetrievalChain.from_llm(
        llm, vectorstore.as_retriever(), return_source_documents=True
    )

from langchain.document_loaders import PyPDFLoader # for loading the pdf
from langchain.embeddings import OpenAIEmbeddings # for creating embeddings
from langchain.vectorstores import Chroma # for the vectorization part
from langchain.chains import ChatVectorDBChain # for chatting with the pdf
from langchain.llms import OpenAI # the LLM model we'll use (CHatGPT)

# from agent.agent import chat_with_agent
from utils.config import load_config, setup_environment_variables

# Load configuration from config.yml
config = load_config()

# Set up the environment variables
setup_environment_variables(config)
print("Loading the embedder...")

pdf_path = "./test.pdf"
loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()
print(pages[0].page_content)

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(pages, embedding=embeddings,
                                 persist_directory=".")
vectordb.persist()

pdf_qa = ChatVectorDBChain.from_llm(OpenAI(temperature=0.9, model_name="gpt-3.5-turbo"),
                                    vectordb, return_source_documents=True)

query = "What is the VideoTaskformer?"
result = pdf_qa({"question": query, "chat_history": ""})
print("Answer:")
print(result["answer"])

import os
from app.core.config import settings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document


openai_api_key = settings.OPENAI_API_KEY

if not openai_api_key:
    raise ValueError("OpenAI API key not set. Please set it in the .env file")

try:
    # Read the file
    text = ""
    data_directories = ["../data/product", "../data/reviews"]
    for directory in data_directories:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf8") as file:
                text += file.read() + "\n"

    # Split the text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    split_texts = text_splitter.split_text(text)


    # Create document objects
    docs = [Document(page_content=chunk) for chunk in split_texts]
    
    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    # Initialize Chroma vector store
    persist_directory = "./chroma_db"
    vectorstore = Chroma.from_documents(docs, embedding=embeddings, persist_directory=persist_directory)

except Exception as e:
    print(f"An error occurred: {e}")
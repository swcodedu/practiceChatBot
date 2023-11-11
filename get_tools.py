from    langchain.schema.vectorstore        import ( VectorStore, VectorStoreRetriever )
from    langchain.agents.agent_toolkits     import create_retriever_tool
from    utils   import ( load_vectordb_from_file )


def get_personal_retriever() -> VectorStoreRetriever:
  personal_texts = [
    "내 이름은 홍길동입니다.",
    "내가 제일 좋아하는 색은 보라색입니다.",
    "내 꿈은 최고의 인공지능 활용 어플리케이션 개발자가 되는 것입니다.",
    "내 고향은 제주도입니다.",
    "나는 남성입니다",
    "나는 1972년에 태어났습니다.",
  ]
  personal_retriever = FAISS.from_texts(personal_texts, OpenAIEmbeddings()).as_retriever()
  if not isinstance(personal_retriever, VectorStoreRetriever):
    raise ValueError("personal_retriever is not VectorStoreRetriever")
  return personal_retriever


def get_freelancer_guidelines() -> VectorStoreRetriever:
  retriever = load_vectordb_from_file(PDF_FREELANCER_GUIDELINES_FILE).as_retriever()
  if not isinstance(retriever, VectorStoreRetriever):
    raise ValueError("it's not VectorStoreRetriever")
  return retriever

def get_outdoor_clothing_catalog() -> VectorStoreRetriever:
  retriever = load_vectordb_from_file(CSV_OUTDOOR_CLOTHING_CATALOG_FILE).as_retriever()
  if not isinstance(retriever, VectorStoreRetriever):
    raise ValueError("it's not VectorStoreRetriever")
  return retriever



def get_tools() :
  tools = [
    create_retriever_tool(
      get_freelancer_guidelines(),
      "freelancer_guidelines",
      "Good for answering questions about the different things you need to know about being a freelancer",
    ),
    create_retriever_tool(
      get_outdoor_clothing_catalog(),
      "outdoor_clothing_catalog",
      "Good for answering questions about outdoor clothing names and features",
    ),
    create_retriever_tool(
      get_personal_retriever(),
      "personal",
      "Good for answering questions about me",
    )
  ]
  return tools
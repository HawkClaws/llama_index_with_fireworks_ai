from llama_index import ServiceContext
from llama_index.llms import  OpenAI
from llama_index.schema import Document
from llama_index import SummaryIndex

API_BASE = "https://api.fireworks.ai/inference/v1"
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
MODEL = "accounts/fireworks/models/elyza-japanese-llama-2-7b-fast-instruct"

import tiktoken

tiktoken.model.MODEL_TO_ENCODING[MODEL] = "cl100k_base"

import llama_index.llms.openai_utils

llama_index.llms.openai_utils.ALL_AVAILABLE_MODELS[MODEL] = 2048

llm = OpenAI(api_base=API_BASE, api_key=API_KEY, model=MODEL, max_tokens=50)
service_context = ServiceContext.from_defaults(
    llm=llm,
    context_window=2048,
    num_output=256,
)

# Indexの読み込み
index = SummaryIndex.from_documents(
    [Document(text="太郎はの好きな色は赤色で、好きな動物は猿です")],
    service_context=service_context,
    show_progress=True,
)

query_engine = index.as_query_engine()
query1 = "太郎の好きな動物は？"
res = query_engine.query(query1)
print("============QUERY===============")
print(query1)
print("============RESPONSE===============")
print(res.response)
print("============END===============")

query2 = "太郎の好きな色は？"
res = query_engine.query(query2)
print("============QUERY===============")
print(query2)
print("============RESPONSE===============")
print(res.response)
print("============END===============")

from tavily import TavilyClient
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
response = tavily.search(query="자율적 에이전트 요약", search_depth="advanced")
pprint(response)
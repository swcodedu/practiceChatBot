


"""
파이썬으로 백엔드 서버 프로그램을 만드는 중.

각각 uri 별로 request 값과 result 값이 아래와 같은 서버 프로그램 코드를 작성하고  스웨거를 적용시켜줘.
flask-restx 를 사용 할 것

/new_token

request : {
  db : integer
}
result : {
  token: string
}


/prompt

request : {
  token: string
  prompt: string
}

result : {
  result: string
}

"""
import threading
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import uuid
import asyncio

'''
##########################################################################
Add by Jasmine Kim from Mr.Hong's code
##########################################################################
'''

import  os
import  sys
import  openai
from    langchain.chat_models           import  ChatOpenAI
from    dotenv                          import  load_dotenv

from    langchain_E_retrieval_tool      import  get_tools
from    langchain.agents.agent_toolkits import  create_conversational_retrieval_agent
from    fastapi.responses               import  HTMLResponse
from    fastapi                         import FastAPI, Request, BackgroundTasks

load_dotenv()


openai.api_key      = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("ORGANIZATION")
sys.path.append(os.getenv("PYTHONPATH"))
llm_model = "gpt-3.5-turbo"

llm = ChatOpenAI(model_name=llm_model, temperature=0)

'''
##########################################################################
Add finished
##########################################################################
'''

is_debug = True
app = FastAPI(debug=is_debug, docs_url="/api-docs")


class TokenOutput(BaseModel):
  token: str


class PromptRequest(BaseModel):
  token: str
  prompt: str


class PromptResult(BaseModel):
  result: str


# @app.get("/")
# async def serve_html():
#   return FileResponse('./html-docs/index.html')


tokens = {

}

@app.get("/api/new_token")
async def new_token(db: int):
  # 원하는 db 처리 로직을 여기에 추가하실 수 있습니다.

  token   = str(uuid.uuid4())
  tools   = get_tools()
  agent_executor  = create_conversational_retrieval_agent(llm, tools, verbose=True)
  tokens [token] = agent_executor

  #
  # 쇼핑몰 카탈로그를 선택한 경우에 대한 안내 메시지 추가
  if db == 2:
    introduction_message = "안녕하세요, 아웃도어 전문 매장입니다. 현재 저희는 여러 아웃도어 제품을 보유하고 있습니다. 아래에는 몇 가지 인기 상품의 요약 정보가 있습니다."
    agent_response = agent_executor({"input": introduction_message})
    introduction_message = agent_response["output"]
    #return jsonable_encoder(TokenOutput(token=token, introduction=introduction_message))
    return jsonable_encoder(PromptResult(result=result["output"]))
  else:
    return jsonable_encoder(TokenOutput(token=token, introduction=""))
  #'''    
  
  #return jsonable_encoder(TokenOutput(token=token))
  #return jsonable_encoder(TokenOutput(token=str(uuid.uuid4())))

request_idx = 0

@app.post("/api/prompt")
async def process_prompt(request: PromptRequest):
  # 비동기적으로 처리할 내용을 여기에 구현합니다.
  # 예를 들어, 외부 API 호출이나 무거운 계산 작업 등을 비동기로 수행할 수 있습니다.
  global request_idx
  idx = request_idx
  request_idx = request_idx + 1

  executor  = tokens[request.token]
  if not executor:
    raise ValueError("Token is not available. (토큰이 없습니다.)")
  
  '''
  # 쇼핑몰 카탈로그를 선택한 경우에 대한 안내 메시지 추가
  if "안녕하세요, 아웃도어 전문 매장입니다." in request.prompt:
    introduction_message = "현재 저희는 여러 아웃도어 제품을 보유하고 있습니다. 아래에는 몇 가지 인기 상품의 요약 정보가 있습니다."
    agent_response = executor({"input": introduction_message})
    introduction_message = agent_response["output"]
    return jsonable_encoder(PromptResult(result=introduction_message))
  else:
    result = executor({"input": request.prompt})
        
    # 브라우저 채팅창에 노출되도록 수정
    return HTMLResponse(content=f'<div class="message user-message">{request.prompt}</div><div class="message server-message">{result["output"]}</div>', status_code=200)
  '''
  result = executor({"input": request.prompt})

  if is_debug:
    current_thread = threading.current_thread()
    print(f"{idx}.{request.token} 현재 스레드: {current_thread.name} reqeust.")
    print(f"{idx}.{request.token} reqeust.")
  await asyncio.sleep(10)  # 예시를 위한 비동기 작업 (1초 대기)

  if is_debug:
    print(f"{idx}.{request.token} end.")

  #return jsonable_encoder(PromptResult(result=f"Processed: {request.prompt}"))
  return jsonable_encoder(PromptResult(result=result["output"]))

app.mount("/", StaticFiles(directory="./html-docs", html=True), name="static")

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=5000)

import fastapi

app = fastapi()

# 서버 시작
@app.on_event("startup")
async def startup():
    await init_state

# 서버 종료
@app.on_event("shutdown")
async def shutdown():
    await server_down()

@app.get("/")
def func_name():

    return
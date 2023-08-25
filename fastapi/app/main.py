from fastapi import FastAPI, UploadFile, Form

app = FastAPI()

# 서버 시작
@app.on_event("startup")
async def startup():
    #await init_state
    return

# 서버 종료
@app.on_event("shutdown")
async def shutdown():
    #await server_down()
    return

@app.get("/")
def func_name():

    return

# initiate a specific dir
# : delete and create the dir
import shutil
import os

@app.post("/dir/reset")
async def reset_dir():
    try:
        UPLOAD_DIR = "./dir_name" # dir name
        shutil.rmtree(UPLOAD_DIR)
        os.mkdir(UPLOAD_DIR)
    except:
        pass

    return "All infomation is removed!"

# input
### one file
@app.post("/input/oneFile")
async def input_one_file(file: UploadFile):
    content = await file.read() # file.file.read()
    # csv ###
    # s = str(content, "CP949")
    # data = io.StringIO(s)
    # df = pd.read_csv(dta)

    # xlsx ###
    # data = io.BytesIO(content)
    # df = pd.read_excel(data, engine = 'openpyxl')
    return 

### multiple files
@app.post("/input/multiFile")
async def input_multi_file(files: list[UploadFile]):
    return {"filename": [file.filename for file in files]}


### one variable
from typing import Annotated
@app.post("/input/oneVar")
async def input_one_var(var_name: Annotated[str, Form()]):
    return {"var_name": var_name}

### multiple variable
@app.post("/input/multiVar")
async def input_multi_var(var1: Annotated[str, Form()],
                          var2: Annotated[str, Form()],
                          var3: Annotated[str, Form()]):
    return {"var1":var1, "var2":var2, "var3":var3}



# pickle ###
### save the input as a pickle file
### : with one input
import pickle
from fastapi.responses import JSONResponse
@app.post("/pickle/save")
async def pickle_save(meta_data: str):
    info = meta_data
    UPLOAD_DIR = "./dir_name" # dir name
    if ~os.path.isdir(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR, exist_ok=True)
    try:
        with open(f"{UPLOAD_DIR}/pck_file.pickle", "wb") as f:
            pickle.dump(info, f)
        return JSONResponse(content={"message": "Inforamtion saved to pickle file"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": "Error saving inforamtion to pickle file", "error": str(e)}, status_code=500)


### read the pickle file
@app.post("/pickle/read")
async def pickle_read(pickle_file:str):
    UPLOAD_DB = "./dir_name" # set the target directory

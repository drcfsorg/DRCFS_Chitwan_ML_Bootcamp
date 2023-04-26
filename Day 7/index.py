



from fastapi import FastAPI
from fastapi.responses import HTMLResponse



app=FastAPI()

with open("randomfile.txt", 'r') as f:
    content=f.read()

print(content)

@app.get("/")
async def homepage():
    return HTMLResponse("Hello guys this is homepage!!")


@app.get("/testing")
async def randomtesting():
    return HTMLResponse(content)
 


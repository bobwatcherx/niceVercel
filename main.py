from nicegui import *
from os import getenv
import os
ui.label("test").style("font-size:50px;font-weight:bold")
with ui.row().classes("bg-red-300 w-full p-10 justify-between"):
    ui.button("sample test")
    counter = ui.label(0)
    ui.button("Sa")

# port = int(os.environ.get("PORT", 3000))
# app = ui.run(reload=False,title="Edy Channel", port=port)
app = ui.run(reload=False,title="mor")

if __name__ == "__main__":
    port = int(getenv("PORT",3000))
    uvicorn.run(app,host="0.0.0.0",port=port,reload=True)

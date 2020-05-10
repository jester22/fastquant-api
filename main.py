from fastapi import FastAPI
from fastquant import DisclosuresPSE
import json
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def read_root():
  return RedirectResponse(url='/docs')

@app.get("/disclosures")
def read_disclosure(symbol: str, start_date: str, end_date: str, disclosure_type:str = "all"):
  dpse = DisclosuresPSE(symbol=symbol, start_date=start_date, end_date=end_date, disclosure_type=disclosure_type)
  str = dpse.disclosures_combined.to_json(orient='records')
  return {"data": json.loads(str)}

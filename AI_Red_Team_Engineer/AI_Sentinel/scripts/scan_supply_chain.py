import json
from supply_chain.scanner import scan_path
if __name__=="__main__":
    result=scan_path(".")
    with open("reports/supply-chain-results.json","w",encoding="utf-8") as handle: json.dump(result,handle,indent=2)
    print(json.dumps(result["summary"],indent=2))

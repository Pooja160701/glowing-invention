import json
from red_team.runner import run_red_team
if __name__=="__main__":
    print(json.dumps(run_red_team(output_path="reports/redteam-results.json"),indent=2))

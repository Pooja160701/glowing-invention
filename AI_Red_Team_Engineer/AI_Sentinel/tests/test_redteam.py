from red_team.runner import run_red_team

def test_full_red_team_suite_runs():
    result=run_red_team()
    assert len(result["results"])==6
    assert result["summary"]["total_findings"]==0

# Sample pick selection pseudo-implementation (prototype)
from typing import List, Dict
def confidence_score(proj, line, recent_form, matchup_rank, usage_change, venue_score):
    # normalize subscores to [0,1]
    line_delta = proj - line
    line_score = 1 / (1 + 2.718**(-line_delta/2.0))  # logistic
    recent_score = max(0, min(1, (recent_form - line)/10.0 + 0.5))
    matchup_score = 1 - matchup_rank/30.0
    usage_score = max(0, min(1, usage_change/0.15 + 0.5))
    weights = {'recent':0.30,'matchup':0.20,'line':0.25,'usage':0.15,'venue':0.10}
    combined = (weights['recent']*recent_score + weights['matchup']*matchup_score +
                weights['line']*line_score + weights['usage']*usage_score +
                weights['venue']*venue_score)
    return int(round(combined*100))

# Example use:
# confidence = confidence_score(24.8, 21.5, recent_form=24.8, matchup_rank=12, usage_change=0.05, venue_score=0.5)
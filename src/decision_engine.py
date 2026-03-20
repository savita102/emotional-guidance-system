def decide_action(state, intensity, stress, energy):
    
    if stress >= 8:
        return "box_breathing"
    
    if energy <= 2:
        return "rest"
    
    if state in ["anxious", "overwhelmed"]:
        return "grounding"
    
    if state == "sad":
        return "journaling"
    
    if state == "calm" and energy >= 4:
        return "deep_work"
    
    if state == "restless":
        if intensity <= 2:
            return "box_breathing"
        else:
            return "grounding"
    
    return "light_planning"


def decide_timing(state, intensity, stress, energy, time_of_day):
    
    if stress >= 8:
        return "now"
    
    if energy <= 2:
        return "within_15_min"
    
    if state == "calm" and energy >= 4:
        return "now"
    
    if time_of_day == "night":
        return "tonight"

    if state == "restless":
        return "within_15_min"
    
    return "later_today"
def compute_uncertainty(confidence, stress, energy):
    
    if confidence < 0.5:
        return 1
    
    if abs(stress - energy) > 6:
        return 1
    
    return 0
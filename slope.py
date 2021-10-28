def calculate_slope(results):
    slope =  (results.exit_amps-results.enter_amps) / (results.exit_depth - results.enter_depth)
    offset = (results.depths_normalized*slope) + results.enter_amps
    amps_new = results.amps_drill-offset

    results.amps_new = amps_new
    results.slope = slope
    return results
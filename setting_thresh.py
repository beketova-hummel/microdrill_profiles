import numpy as np
import moving_ave

def apply_thresholds(results, csv_filename, threshold1=0.3, threshold2=0.3):
    filename_in = csv_filename
    #print(f'reading csv: {filename_in}')
    measurement_table = np.genfromtxt(filename_in, delimiter=',', skip_header=1, missing_values='', filling_values=0.)
    drill_depths = measurement_table[:,0]
    amp_column = 1
    drill_amps = measurement_table[:,amp_column]
    feed_amp_column = 2
    feed_amps = measurement_table[:,feed_amp_column]

    smooth_amps_drill = moving_ave.smooth(drill_amps)
    #print (smooth_amps_feed[-10:])

    # relative threshold
    #threshold1 = smooth_amps_drill[0]*1.1 + 1
    #threshold2 = smooth_amps_drill[-1]*1.1 + 1

    range_begin = np.amin(np.where (drill_amps > threshold1))
    range_end = np.amax(np.where(drill_amps>threshold2))
    enter_depth = drill_depths[range_begin]
    exit_depth = drill_depths[range_end]
    enter_amps = drill_amps[range_begin]
    exit_amps = drill_amps[range_end]

    amps_drill = drill_amps[range_begin:range_end+1]
    smooth_amps_drill = moving_ave.smooth(amps_drill) 
    depths_normalized = drill_depths[range_begin:range_end+1] - (enter_depth)
    assert depths_normalized.shape == (len(amps_drill),)
    distance = round(100.*(exit_depth - enter_depth)) / 100.

    results.smooth_amps = smooth_amps_drill
    results.range_begin = range_begin 
    results.range_end = range_end
    results.enter_depth = enter_depth 
    results.exit_depth = exit_depth
    results.enter_amps = enter_amps 
    results.exit_amps = exit_amps
    results.amps_drill = amps_drill
    results.depths_normalized = depths_normalized
    results.distance = distance
    results.depths_original = drill_depths
    results.drill_amps_original = drill_amps
    results.feed_amps = feed_amps
    results.smooth_amps_drill = smooth_amps_drill

    return results
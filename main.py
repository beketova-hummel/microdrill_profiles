import os
import types
import rpd
import fix_csvfile
import setting_thresh
import plot_fig
import slope

def process_rpd(rpd_file_name, parameters):
    results = types.SimpleNamespace()
    results.profile_name, _ = os.path.splitext(rpd_file_name)

    #1. load .rgp and convert to .csv; plot original graph and produce a .csv - rpd.py
    csv_filename = rpd.convert_rgp(rpd_file_name)
    print(f'csv_filename from convert_rgp: {csv_filename}')
    #1a. if needed, fix csv file - fix_csvfile.py
    fix_csvfile.fix_csvfile(csv_filename)

    #2. define smooth line / moving average - moving_ave.py

    #3. thresholds and cutting 0-oes - setting_thresh.py
    results = setting_thresh.apply_thresholds(results, csv_filename, 
        threshold1=parameters.threshold1, 
        threshold2=parameters.threshold2)
    #print(results)

    #4. calculating slope
    results = slope.calculate_slope(results)
    #print(results)

    #5. plotting averages and histogram and saving figures - plot_fig.py
    figs = plot_fig.prepare_plots(results)

    return figs, results

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Analyze RGP measurements.')
    parser.add_argument('rpd_filename', type=str,
                        help='RPD measurement file')
    parser.add_argument('--threshold1', type=float, default=0.3,
                        help='left threshold')
    parser.add_argument('--threshold2', type=float, default=0.3,
                        help='right threshold')
    
    args = parser.parse_args()
    parameters = args

    figs, results = process_rpd(args.rpd_filename, parameters)
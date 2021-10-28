import json
import csv
import numpy as np

def convert_rgps(rgp_file_names):
    for rgp_file_name in rgp_file_names:
        convert_rgp(rgp_file_name)

def convert_rgp(rgp_file_name):
    rpd_measurement_id = rgp_file_name.rsplit(".", maxsplit=1)[0]

    with open (rgp_file_name) as read_file:
        data = json.load(read_file)

    drill_amp = np.array(data["profile"]['drill'])
    feed_amp = np.array(data["profile"]['feed'])
    feed_resol = data['header']['resolutionFeed']

    depth = np.arange(0, len(drill_amp), 1)/feed_resol

    ###create a write file with the output of used data
    csv_filename = rpd_measurement_id +".csv"
    with open (csv_filename, "w") as write_file:
        csvwriter = csv.writer(write_file, delimiter=',',quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['depth (mm)', 'drill amplitude (%)', 'feed amplitude (%)'])
        csvwriter.writerows(zip(depth, drill_amp, feed_amp))
    
    #Plot depth vs drill and feed
    # plt.plot(depth, drill_amp, label = 'Drill Amp (%)')
    # plt.plot(depth, feed_amp, label = 'Feed Amp (%)')

    # plt.title('Drilling Resistance ' + rpd_measurement_id)
    # plt.xlabel('Depth (mm)')
    # plt.ylabel('Amplitude (%)')
    # plt.legend(loc = 'best')

    #plt.savefig(rpd_measurement_id + ".png")
    #plt.clf()
    #plt.show()
    #break
    return csv_filename

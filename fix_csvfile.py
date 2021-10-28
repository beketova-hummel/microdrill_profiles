import csv

def compress_columns_vertically(infilename, outfilename):
    columns = []
    nrows = 0
    with open(infilename, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for irow, row in enumerate(reader):
            nrows += 1
            if len(columns) < len(row):
                nadditional = len(row) - len(columns)
                for i in range(nadditional):
                    columns.append(list())
            for icol, entry in enumerate(row):
                if entry != '' or irow == 0:
                    columns[icol].append(entry)

    ncolumns = len(columns)

    with open(outfilename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for irow in range(nrows):
            row = []
            if not any([len(column) > irow for column in columns]):
                break
            for column in columns:
                if len(column) <= irow:
                    row.append('')
                else:
                    row.append(column[irow])
            writer.writerow(row)

def fix_csvfile(csvfile):
    outfile = csvfile
    #print(f'{csvfile} -> {outfile}')
    compress_columns_vertically(csvfile, outfile)
import csv
import re

with open("rosalind.csv", 'rU') as csvIN:
    outCSV=(line for line in csv.reader(csvIN, dialect='excel'))
    
    header = next(outCSV)
    
    for row in outCSV:
        problem = re.sub(r'.*\/([a-zA-Z0-9]+)\/?', r'\1', row[-2])
        
        infile = open('inputs/sample_%s.txt' % problem, 'w')
        infile.write(row[0])
        infile.close()
        
        outfile = open('outputs/sample_%s.txt' % problem, 'w')
        outfile.write(row[-1])
        outfile.close()

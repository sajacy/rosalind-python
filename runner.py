#!/usr/bin/env python

""" A simple runner for Rosalind solutions
"""
import importlib
import os.path
import argparse
import re

def runner(modulename, inputfile, compare_output):
    try:
        # Import the solution from the solutions package
        solution = importlib.import_module('.%s' % modulename, package='solutions')

        # The graded input files are named rosalind_[module].txt by default.
        filename = 'inputs/rosalind_%s.txt' % modulename
        
        # If the rosalind input exists, use it, otherwise fallback to the sample input file.
        inputfile = filename if os.path.exists(filename) else inputfile or ('inputs/sample_%s.txt' % modulename)
        outputfile = 'outputs/%s.txt' % modulename

        # Open the files
        infile = open(inputfile, 'r')
        outfile = open(outputfile, 'w')

        # Assume the solution has a `main(inputfile)` function
        print "Using %s" % inputfile
        solution.main(infile, outfile)

        # Cleanup
        infile.close()
        outfile.close()

        # Compare sample outputs (if flagged)
        if compare_output and re.match(r'.*sample_.*', inputfile):
            print '\nYour output:'
            print open(outputfile, 'r').read()
            print '\nSample output:'
            print open('outputs/sample_%s.txt' % modulename).read()

    except Exception as e:
        print 'Could not run the solution: %s' % e


# This parses inputs and calls our runner() function above
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Runs a given Rosalind solution')
    parser.add_argument('problem_id', help='Rosalind problem ID, e.g. "dna"')
    parser.add_argument('-c', action='store_true', dest='compare_output', help='compare output to sample output')
    parser.add_argument('-i', '--input_file', help='a custom input file name')

    args = parser.parse_args()
    runner(args.problem_id, args.input_file, args.compare_output)


Getting Started with Rosalind and Python
==================================

Easily write [Rosalind.info](http://rosalind.info) solutions in Python.

I wrote this to organize my solutions, and to streamline the testing against sample inputs.

To get started, simply `git clone` this repo to your local machine, and start writing your Python code in the `solutions` directory.

### Workflow 

1. Write: save your code in the `solutions` directory, following the [Solution Template](#solution-template) below. 
2. Test: run `./runner.py -c dna`, and it will show you the output.
3. Download: When you are satisfied with the tests against the sample input, download the "real" inputs from Rosalind into the `inputs` directory.
4. Submit: Execute the runner again, `./runner.py dna`, and it will automatically detect the newly downloaded `rosalind_dna.txt` input 
and generate the submittable output file, e.g. `outputs/dna.txt`, ready to be uploaded.

### Preloaded with samples

This repo is preloaded with the sample inputs and outputs from all problem sets (except Armory, since its purpose is to teach external tools), 
so you don't have to worry about copy-pasting. The sample inputs will be used by default to test your solutions, until you download the actual `rosalind_*.txt` files to be evaluated.

You can specify the `-c` option when using `runner.py` to compare your output to the expected sample output, for example:

```
$ ./runner.py -c dna
Using inputs/sample_dna.txt

Your output:
20 12 17 21

Sample (expected) output:
20 12 17 21
```

I think this alone should be valuable. (I wish someone had done this for *me*!)

**NOTE** You must still download actual datasets from Rosalind to be graded. Do not commit gradeable datasets. I don't support cheating in any form.

##### Additional resources

Certain problems (`GAFF`, `GLOB`, etc.) require a scoring matrix.  The following matrices are provided in the `inputs` directory:

- `BLOSUM62.txt`
- `PAM250.txt`
- `DNAfull.txt`

**TODO**: Extra datasets (for example, for [BA1A](http://rosalind.info/problems/ba1a/)

### Solution Template

Write your solution in a file named with the problem ID, e.g. `dna.py`, with a `def main(infile, outfile):` function.

The `infile` and `outfile` parameters are [file objects](http://learnpythonthehardway.org/book/ex16.html).

```
def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    output = infile.read().count

    # For debugging, print something to console
    print output

    # Write the output.
    outfile.write(output)
```

**NOTE:** Please do **NOT** commit solutions.  It is against the [rules](http://rosalind.info/faq/#can-i-post-my-solutions-somewhere)!

To help ensure this, the repo has been configured to ignore all files in `solutions`. If you want to save your solutions - copy them somewhere else!

### Runner Usage

```
usage: runner.py [-h] [-c] [-i INPUT_FILE] problem_id

Runs a given Rosalind solution

positional arguments:
  problem_id            Rosalind problem ID, e.g. "dna"

optional arguments:
  -h, --help            show this help message and exit
  -c                    compare your output to sample output
  -i INPUT_FILE, --input_file INPUT_FILE
                        a custom input file name
```

### Tools (for scraping new problems)

To update the list of sample inputs/outputs you'll need the [WebScraper](http://webscraper.io/) Chrome Extension.

Procedure:

1. Install WebScraper, open the Developer Tools > Web Scraper tab, and click "Create new sitemap" >  "Import sitemap".
2. You can find the Sitemap definition in the `tools/webscraper_sitemap.json` file.  Paste it into the Sitemap JSON field and click the "Import Sitemap" button.
3. Click the "Sitemap (rosalind)" > Scrape menu item.  Click "Start scraping".  This will open a new popup and should start navigating all the problem pages.
4. After it finishes, click the "Sitemap (rosalind)" > "Export data as CSV" menu item and download the CSV to your rosalind repo directory.
5. From the `rosalind` repo root, run `python tools/parser.py` to generate new `sample_%s.txt` files in both the `inputs` and `outputs` directories.


### License

The MIT License (MIT)
Copyright (c) 2016 Jeffrey Yang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

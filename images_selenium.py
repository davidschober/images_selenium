def main(filetype, inputfile):

    import selenium.webdriver as webdriver
    from selenium.common.exceptions import TimeoutException
    import csv
    from time import sleep
    
    if filetype == "ga":
        prefix = "http://images.library.northwestern.edu"
    elif filetype == "pids":
        prefix = "http://images.library.northwestern.edu/multiresimages/"
    else:
        print "no filetype"
        print "bad filtype, you can only use ga or pids" 
        sys.exit(2)  
    
    # General setup 
    csv_file = open(inputfile, "r")
    urls = [prefix+row[0] for row in csv.reader(csv_file)]
    browser = webdriver.Chrome()
    #switch for filtype
    for url in urls:
        try:
            browser.get(url)
            print "working on %s" %url
            sleep(15)
        except TimeoutException:
            # something times outs, just move along
            pass

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--filetype')
    parser.add_argument('-i', '--inputfile')
    parser.add_help
    args = parser.parse_args()
    if args.filetype and args.inputfile:
        filetype = args.filetype
        inputfile = args.inputfile
        main(filetype, inputfile)
    else:
        parser.print_help()
   

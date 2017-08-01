def main(filetype, inputfile, wait):

    import selenium.webdriver as webdriver
    from selenium.common.exceptions import TimeoutException
    import csv
    from time import sleep
    csv_file = open(inputfile, "r")
    if filetype == "ga":
        prefix = "http://images.library.northwestern.edu"
        #scrub for empty lines and make sure that they start with "/"
        urls = [prefix+row[0] for row in csv.reader(csv_file) if row and row[0].startswith('/')]
    elif filetype == "pids":
        prefix = "http://images.library.northwestern.edu/multiresimages/"
        urls = [prefix+row[0] for row in csv.reader(csv_file)]
    else:
        print "no filetype"
        print "bad filtype, you can only use ga or pids" 
        sys.exit(2)  
    
    # General setup 
    browser = webdriver.Chrome()
    #switch for filtype
    for url in urls:
        try:
            browser.get(url)
            print "working on %s" %url
            sleep(int(wait))
        except TimeoutException:
            # something times outs, just move along
            pass

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--filetype')
    parser.add_argument('-i', '--inputfile')
    parser.add_argument('-w', '--wait')
    parser.add_help
    args = parser.parse_args()
    if args.filetype and args.inputfile and args.wait:
        main(args.filetype, args.inputfile, args.wait)
    else:
        parser.print_help()
   

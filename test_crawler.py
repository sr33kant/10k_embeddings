
import time
from sec_crawl import SecCrawler
from comp_data import comp_codes
def get_filings():
    t1 = time.time()

    # create object
    seccrawler = SecCrawler()

    # companyCode = 'COIN'  # company code for apple
    # cik = '1366340'  # cik code for apple
    # date = '2015101'#date from which filings should be downloaded
    # count = '90'#  no of filings
    for k,v in comp_codes.items():
        seccrawler.filing_10Q(str(k), str(v), str('2015101'), str('90'))
        seccrawler.filing_10K(str(k), str(v), str('2015101'), str('90'))


    t2 = time.time()
    print("Total Time taken: "),
    print(t2 - t1)


if __name__ == '__main__':
    get_filings()
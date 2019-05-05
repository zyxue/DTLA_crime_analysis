import os
import logging
import time

import requests
import numpy as np


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s|%(levelname)s|%(message)s')

years = range(2019, 2015, -1)
weeks = range(1, 53)

url_base = 'http://maps.latimes.com/neighborhoods/neighborhood/'


neighborhoods = []
with open('./neighborhoods.csv', 'rt') as inf:
    for line in inf:
        neighborhoods.append(line.strip())

for neig in neighborhoods:
    for year in years:
        for week in weeks:
            outdir = f'by_neighborhood/{neig}/{year}/{week}'
            out = os.path.join(outdir, f'{week:02}.html')
            if os.path.exists(out):
                logging.warning(f'{out} already exists')
                continue

            url = f'{url_base}/{neig}/crime/by-week/{year}/{week:02}'
            logging.info(url)

            try:
                resp = requests.get(url)
            except Exception as err:
                logging.exception(err)
                continue

            logging.info(resp.status_code)
            if resp.status_code != 200:
                continue

            if not os.path.exists(outdir):
                os.makedirs(outdir)

            logging.info(f'writing {out}')
            with open(out, 'wt') as opf:
                opf.write(resp.text)

            time.sleep(np.random.random())

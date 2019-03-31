import os
import requests

years = range(2018, 2008, -1)
weeks = range(1, 53)

url_base = 'http://maps.latimes.com/neighborhoods/neighborhood/downtown/crime/by-week'

for year in years:
    outdir = str(year)
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    for week in weeks:
        url = f'{url_base}/{year}/{week:02}'
        print(url)
        resp = requests.get(url)
        print(resp.status_code)

        out = os.path.join(outdir, f'{week:02}.html')
        with open(out, 'wt') as opf:
            opf.write(resp.text)

# Scrape


Extracting different attributes of a specific site, and showing results by using pandas( DataFram).


How to run :
```
pip install -r requirments.txt
python project.py
```


exmaple:
```
 python project.py
 Enter your url please: 
 https://www.imdb.com
```
 
 output:
 
 ```
    page_encoding  page_status           page_elapsed                                              links
0           utf-8          200 0 days 00:00:00.925340                                     /?ref_=nv_home
1           utf-8          200 0 days 00:00:00.925340      https://www.imdb.com/calendar/?ref_=nv_mv_cal
3           utf-8          200 0 days 00:00:00.925340                  /chart/moviemeter/?ref_=nv_mv_mpm
4           utf-8          200 0 days 00:00:00.925340                      /feature/genre/?ref_=nv_ch_gr
..            ...          ...                    ...                                                ...
160         utf-8          200 0 days 00:00:00.925340  https://advertising.amazon.com/resources/ad-sp...
161         utf-8          200 0 days 00:00:00.925340              https://www.amazon.jobs/en/teams/imdb
162         utf-8          200 0 days 00:00:00.925340                            /conditions?ref_=ft_cou
163         utf-8          200 0 days 00:00:00.925340                               /privacy?ref_=ft_pvc
164         utf-8          200 0 days 00:00:00.925340         https://www.amazon.com/b/?&node=5160028011
```

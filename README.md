# task

DB/db_init.py - database initialization (data for connecting to the database is stored indev.env)
![изображение](https://user-images.githubusercontent.com/106768300/181867541-4d7585f3-f10c-4933-82e5-527bb2aeb7bb.png)


(URL for parsing are stored in dev.env)
Parser/run_scraper.py --dry_run false  - create new records in the collected_data table in the database
![изображение](https://user-images.githubusercontent.com/106768300/181867480-454dd428-873c-4b8b-9a01-b713c9436605.png)

Parser/run_scraper.py (--dry_run true) - result as a table to the console

![изображение](https://user-images.githubusercontent.com/106768300/181867464-9cbaabbb-a25b-4086-98c2-8fc2497d223d.png)

Server/run_api.py 

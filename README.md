# Background Project
Project ini merupakan akumulasi dari apa sudah dipelajari sebelumnya. Dimana project menjelaskan batch pipeline yang mana datasource news scrape yang diambil dari Finnhub APi yg kita load ke mongodb. Dari Mongodb, data kita ambil lalu dilakukan sentiment analysis yang akan kita simpan ke postgres sebagai data_warehousenya.

# Steps :
1. Run Airflow using `docker-compose up`
2. Inside Plugins Folder create:
    - Finnhub loader
    - MongoDB loader
    - Sentiment Analysis
    - Postgres loader
3. Create python code to extract from Finnhub and load to MongoDB
4. Create Python code that Get data from MongoDB and do Sentiment Analysis then load the result to Postgres
5. Create Python Environment `python -m venv env`
6. Activate `env/Scripts/activate`
7. Run `pip install -r requirements.txt`
8. Run `python finhub_mongodb_loader.py`
9. Run `pip install psycopg2-binary`
10. Create Database `Enter docker desktop -> postgres image -> terminal -> psql -Uairflow -> create database data_warehouse; -> \du -> \l ` or `docker exec it <postgres images id> bash -> psql -Uairflow -> create database data_warehouse; -> \du -> \l` 
11. Run `python sentiment_analysis_loader.py`
12. Check the newly entered database `\c data_warehouse -> \d -> select * from sentiment_news_analysis limit 20;` or check through dbeaver. 

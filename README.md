# coinMENA
coinMENA is REST API with Python django rest api framework.

## Steps for running

Clone project 
```bash
git clone https://github.com/naseemnoble/coinMENA.git
```
Change directory to root folder
```
cd coinMENA/alphavantage
```
Build Dockerfile
```buildoutcfg
docker build .
```
Compose Docker yaml file
```buildoutcfg
docker-compose up
```
## Note
Django rest API key is '**8lXXuD7E.Y5JMk864MngArHLQGZpnyCfMDDCMdh3F**'. 

You can config your own **Alphavantage API KEY** in **.env** file (Refer .env_template)
## APIs
POST requesting of the price from alphavantage.
```buildoutcfg
curl --location --request POST 'http://127.0.0.1:8000/instrument/exchangerate/' \
--header 'Authorization: Api-Key 8lXXuD7E.Y5JMk864MngArHLQGZpnyCfMDDCMdh3F' \
--form 'from_currency="BTC"' \
--form 'to_currency="USD"' \
--form 'interval_min="60"'
```
GET return Exchange rate
```buildoutcfg
curl --location --request GET 'http://127.0.0.1:8000/instrument/exchangerate/' \
--header 'Authorization: Api-Key 8lXXuD7E.Y5JMk864MngArHLQGZpnyCfMDDCMdh3F' \
--form 'from_currency="BTC"' \
--form 'to_currency="USD"'
```
## Data
SQLite database file db.sqlite3

Tables : instruments_exchangerate, instruments_pricerequest
```buildoutcfg
$ sqlite3 db.sqlite3 
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .mode column
sqlite> select * from instruments_exchangerate;
1           BTC                 Bitcoin             USD               United States Dollar  57684.07       2021-05-02 02:51:01  UTC         57680.88    57680.89
```

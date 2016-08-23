![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)

# Twitter-Streaming
Stream tweets to MySQL. 

## Introduction
* **Connect MySQL with Python script**
    * Use **mysql.connector** module
    * Create 'tweet' database
* **Set up a Twitter stream listener**
    * Aggregate data on a **search term**
    * Fetch search term from **table source**
    * Modify StreamListener **on_data** method
    * Convert **JSON** data object to a python dictionary
    * **Stop** the listener when we have enough tweets
* **Import the data into MySQL database**
    * Modify StreamListener **on_data** method
    * Insert tweets into **table text**

## Tables
### source

### text

## Libraries Used
* [tweepy](http://www.tweepy.org/)
* [mysql.connector](https://dev.mysql.com/downloads/connector/python/)
* [time](https://docs.python.org/3/library/time.html)
* [json](https://docs.python.org/3/library/json.html)

## License

## Resources
* [How to get text from Twitter feeds](http://www.tulane.edu/~howard/CompCultES/twitter.html)
* [Streaming Tweets from Twitter to Database](https://pythonprogramming.net/mysql-live-database-example-streaming-data/)
* [Streaming Twitter to MySQL using Python](http://miningthedetails.com/blog/python/TwitterStreamsPythonMySQL/)

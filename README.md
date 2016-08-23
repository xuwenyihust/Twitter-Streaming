![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)

# Twitter-Streaming
Stream tweets to MySQL. 

## Introduction
### **Connect MySQL with Python script**
* Use **mysql.connector** module
* Create database 'tweet'
    * Create table 'source'
    * Create table 'text'

### **Set up a Twitter stream listener**
* Aggregate data on a **search term**
    * Fetch search term from **table source**
* Modify StreamListener **on_data** method
    * Convert **JSON** data object to a python dictionary
    * **Stop** the listener when we have enough tweets

### **Import the data into MySQL database**
* Modify StreamListener **on_data** method
* Insert tweets into **table text**

## Tables
### source

  | Column | Descriptions |
  | -------|--------------|
  | id     | Unique keyword id |
  | keyword | Keyword for search 
|
  ```python
  ('id', 'int(13)', 'YES', '', None, '')
  ('keyword', 'varchar(20)', 'YES', '', None, '')
  ```
### text

  | Column | Descriptions |
  | -------|--------------|
  | time   | Tweet post time |
  | username | User name |
  | tweet | Text part of the tweet |

  ```python
  ('time', 'int(13)', 'YES', '', None, '')
  ('username', 'varchar(20)', 'YES', '', None, '')
  ('tweet', 'varchar(140)', 'YES', '', None, '')
  ```

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

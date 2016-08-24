![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)

# Twitter-Streaming
Stream tweets to MySQL. 

**Collection, storage and cleaning.**

## Introduction
### **Connect MySQL with Python script**
* Use **mysql.connector** module
* Create database 'Twitter'
    * Create **table 'source'**

### **Set up a Twitter stream listener**
* Aggregate data on a **search term**
    * Fetch search term from **table source**
    * Create different tables for each search term to store infomation we need.
* Modify StreamListener **on_data** method
    * Convert **JSON** data object to a python dictionary
    * **Stop** the listener when we have enough tweets

### **Import the data into MySQL database**
* Modify StreamListener **on_data** method
* Extract **different fields** of tweets into different tables

## Tables
### source

| Column | Descriptions |
| -------|--------------|
| id     | Unique keyword id |
| keyword | Keyword for search |

```python
('id', 'int(13)', 'YES', '', None, '')
('keyword', 'varchar(20)', 'YES', '', None, '')
```
### tweet_term 

| Column   | Type    |	
| -------- |-------- |
| id       | VARCHAR |  
| time     | INT     |
| username | VARCHAR |
| tweet    | VARCHAR |

### hashtag_term

| Column   | Type    |
| -------- |-------- |
| id       | VARCHAR |
| tag      | VARCHAR |

### url_term

| Column   | Type    |
| -------- |-------- |
| id       | VARCHAR |
| url      | VARCHAR |

### mention_term
| Column   | Type    |
| -------- |-------- |
| id       | VARCHAR |
| mentioned_id      | VARCHAR |
| mentioned_name 	| VARCHAR |

## Tweets
### JSON Format of tweets

| Field  |     Type     |
| -------|--------------|
| ...    | ... |
| text   | string |
| source | string |
| id     | int64  |
| created_at | string |
| ...    | ... |

## Libraries Used
* [tweepy](http://www.tweepy.org/)
* [mysql.connector](https://dev.mysql.com/downloads/connector/python/)
* [time](https://docs.python.org/3/library/time.html)
* [json](https://docs.python.org/3/library/json.html)

## Appendix
### The Emoji Problem 
The native MySQL UTF-8 character set can hold only 3 bytes, but the whole range of UTF8 characters, including Emoji, requires 4 bytes. So the relational columns should be created with the **utf8mb4** collection.
### Stop Listening
The original tweepy.streaming.StreamListener class doesn't support stopping listening even when we've got enough infomation we need. We need to modify the StreamListener class by ourselves, adding a **counter** in the 'on_data' method.

## License

## Resources
* [How to get text from Twitter feeds](http://www.tulane.edu/~howard/CompCultES/twitter.html)
* [Streaming Tweets from Twitter to Database](https://pythonprogramming.net/mysql-live-database-example-streaming-data/)
* [Streaming Twitter to MySQL using Python](http://miningthedetails.com/blog/python/TwitterStreamsPythonMySQL/)
* [Twitter JSON Formats](https://dev.twitter.com/overview/api/tweets)
* [The Emoji Problem](http://miningthedetails.com/blog/python/TwitterStreamsPythonMySQL/)

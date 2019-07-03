# Reporting Tool 

This tool is use to report 3 areas of intrest: the top articles, the top authors, and days where requests errors are more than 1%. The Python script uses psycopg2 to query a mock PostgreSQL database for a fictional news website. 

## Getting Started

Step 1 : Start your Vagrant VirtualBOX via your terminal using 'vagrant up' (Please refer to 'Built With' below for all software download links.)
Step 2 : Once it is up a running log into your VirtualBox using 'vagrant ssh'
Step 3 : You must then use 'cd /vagrant' to navigate to the shared folder hosting the newsdata.sql file is. 
Step 4 : Once there, use 'psql -d news -f newsdata.sql' to instal file to said directory. Click here to download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file
Step 5 : As a tip (Please have psycopg2 install for use with Python and Python3)
Step 6 : Finally, run the file using the 'python(3) newsdata.py' command.

### Prerequisites

------I've used three querys for this project-----

''' 1. What are the most popular three articles of all time? '''

    Q1 = \
        '''
        SELECT title, COUNT(status) as views
          FROM articles
            INNER JOIN log
              ON path = CONCAT('/article/', slug)
          GROUP BY title, slug, path
          ORDER BY views DESC
          LIMIT 3;
        '''

''' 2. Who are the most popular article authors of all time? '''

    Q2 = \
        '''
        WITH
          stats AS
            (SELECT name, COUNT(path) AS views
              FROM authors
                INNER JOIN articles
                  ON authors.id = articles.author
                INNER JOIN log
                  ON path = CONCAT('/article/', slug)
              GROUP BY name, path
              ORDER BY views DESC)
        SELECT name, SUM(views) AS hits
          FROM stats
          GROUP BY name
          ORDER BY hits DESC;
        '''

''' 3. On which days did more than 1% of requests lead to errors? '''

    Q3 = \
        '''
        WITH
          stats1 AS
            (SELECT time::date AS date,
                COUNT(status) AS total
              FROM log
              GROUP BY date
              ORDER BY total DESC),
          stats2 AS
            (SELECT time::date AS date,
                ROUND(100 * COUNT(status) :: NUMERIC) AS errors
              FROM log
              WHERE status LIKE '404%'
              GROUP BY date
              ORDER BY errors DESC)
        SELECT TO_CHAR(stats1.date, 'FMMonth DD, YYYY') date,
                ROUND(errors / total, 2) AS err_pct
          FROM stats1 INNER JOIN stats2
            ON stats1.date = stats2.date
          WHERE ROUND(errors / total, 1) > 1
          ORDER BY err_pct DESC;
        '''

## Built With

* [PYTHON](http://www.python.org/) - General-purpose programming language
* [PostgreSQL](http://www.postgresql.org/) - The object-relational database system
* [Vagrant](https://www.vagrantup.com) - The virtual machine environment
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) - Used for x86 virtualization

## Authors

* **Kareem A. Henry** - *Initial work* 

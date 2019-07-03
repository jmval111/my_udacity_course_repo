#! /usr/bin/python3.5m
# -*- coding: utf-8 -*-

import psycopg2

try:
    dbs = psycopg2.connect(database='news')
    crs1 = dbs.cursor()
    crs2 = dbs.cursor()
    crs3 = dbs.cursor()
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
    crs1.execute(Q1)
    crs2.execute(Q2)
    crs3.execute(Q3)

    # Project Title
    print('''
          \nREPORTING TOOL PROJECT FOR THE UDACITY FULL STACK NANODEGREE
          \n\t   by
          \n\tKareem A. Henry
          ''')

    # Q1
    print ('''
      1. What are the most popular three articles of all time?''')
    article = crs1.fetchall()
    for row in article:
        print (
          '\n\t' + u'\u2022 ' + '"{article}" - {count} views'.format(
              article=row[0], count=row[1]
            )
        )

    # Q2
    print ('''

      2. Who are the most popular article authors of all time?''')
    author = crs2.fetchall()
    for row in author:
        print (
          '\n\t' + u'\u2022 ' + '{author} - {count} views'.format(
              author=row[0], count=row[1]
            )
        )

    # Q3
    print ('''

      3. On which days did more than 1% of requests lead to errors?''')
    errors = crs3.fetchall()
    for row in errors:
        print (
          '\n\t' + u'\u2022 ' + '{month} - {err_pct}% errors'.format(
              month=row[0], err_pct=row[1]
            )
        )

except (Exception, psycopg2.Error) as error:
    print ('Error occured while trying to connect to PostgreSQL', error)

finally:
    # signal close of database session
    if dbs:
        dbs.close()
    # Project Closure
    print('''

    REPORTING TOOL HAS ENDED

    Have A Great Day!
          ''')

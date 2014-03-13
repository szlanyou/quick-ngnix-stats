quick-ngnix-stats
=================

Generates quick stats from ngnix access log files

Usage:

    python2.7 genstats.py <filename>

This generates a <filename>.json file as an output.  It is an array of dictionaries that look like this:

    {
      "ip": "74.125.228.14",
      "datetime": "2014-03-12 00:00:42-04:00",
      "url": "/hourly.php?eventtypeid=44&date=2008-03-12"
    }
    
This expects each line in the ngnix log to look like this:

    66.249.64.234 - - [11/Mar/2014:06:49:06 -0400] "GET /hourly.php?eventtypeid=30&date=2011-07-24 HTTP/1.1" 200 1643 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"        66.249.66.19 - - [12/Mar/2014:06:40:16 -0400] "GET /hourly.php?eventtypeid=5&date=2008-08-06 HTTP/1.1" 200 1647 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    
Well tested pull requests welcome.  Licensed under GPLv3

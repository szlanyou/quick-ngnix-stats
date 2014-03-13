quick-ngnix-stats
=================

Generates quick stats from ngnix access log files

Usage:

    python2.7 genstats.py <filename>

This generates a <filename>.json file as an output.  It is an array of dictionaries that look like this:

    {
      "ip": "66.249.64.234",
      "datetime": "2014-03-11 06:49:06-04:00",
      "url": "/hourly.php?eventtypeid=30&date=2011-07-24"
    }
    
This expects each line in the ngnix log to look like this:

    66.249.64.234 - - [11/Mar/2014:06:49:06 -0400] "GET /hourly.php?eventtypeid=30&date=2011-07-24 HTTP/1.1" 200 1643 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    
Well tested pull requests welcome.  Licensed under GPLv3

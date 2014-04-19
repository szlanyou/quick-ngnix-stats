quick-ngnix-stats
=================

Generates quick stats from ngnix access log files

Usage:

    python2.7 genstats.py <filename>

This generates a <filename>.json file as an output.  It is an array of dictionaries that look like this:

    {
        "Apr 18 2014": [
            {
                "url": "/hourly.php?eventtypeid=18&date=2005-12-07", 
                "ip": "66.249.66.19",
                "bot": true,
                "datetime": "2014-04-18 06:39:25-04:00"
            }
        ],
        "Apr 19 2014": [
            {
                "url": "/hourly.php?eventtypeid=25&date=2003-09-17",
                "ip": "66.249.66.19",
                "bot": false,
                "datetime": "2014-04-19 00:00:45-04:00"
            }
        ]
    }

    // Note: the 'bot' field is mearly a guess and is simply looking for 'bot' in the line.
    //       if you want more robust bot checking, you should be using more regex or a lookup
    //       for the IP.
    
    
    
This expects each line in the ngnix log to look like this:

    66.249.64.234 - - [11/Mar/2014:06:49:06 -0400] "GET /hourly.php?eventtypeid=30&date=2011-07-24 HTTP/1.1" 200 1643 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    
Well tested pull requests welcome.  Licensed under GPLv3

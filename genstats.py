import json
import sys
import re
import dateutil.parser
import datetime

def readfile(filename):
    lines = []
    with open(filename,'r') as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "Usage:\n\tpython2.7 genstats.py <filename>\n\n"
    else:

        filename = sys.argv[1]

        lines = readfile(filename)

        PATTERN = re.compile(r'''((?:[^;"']|"[^"]*"|'[^']*')+)''')

        ips = []

        hits = []
        for line in lines:
            index = line.index('"')
        
            first = line[0:index]
            second = line[index:]

            parts = PATTERN.split(second)[1::2]

            url = parts[0].split(' ')[1]

            first = first.replace(' - - ','').replace(']','')
            ip = first.split('[')[0]
            dt = str(first.split('[')[1])
           
            day = dt.split('/')[0]
            month = dt.split('/')[1]
            year = dt.split('/')[2].split(':')[0]
            
            hours = dt.split('/')[2].split(':')[1]
            minutes = dt.split('/')[2].split(':')[2]
            seconds = dt.split('/')[2].split(':')[3].split(' ')[0]
            
            timezone = dt.split('/')[2].split(':')[3].split(' ')[1]

            datetimestring = "{0}-{1}-{2} {3}:{4}:{5}{6}".format(year,month,day,hours,minutes,seconds,timezone)

            eventdatetime = dateutil.parser.parse(datetimestring)

            if year == '2014' and month == 'Mar' and day == '12': 
                hits.append( { 'ip':ip, 'datetime': str(eventdatetime), 'url': url } )

            if ip not in ips:
                ips.append(ip)

    with open("{0}.json".format(filename),'w') as f:
        f.write(json.dumps(hits))

    print "Number of hits: {0}".format(len(hits))
    print "Unique IP addresses: {0}".format(len(ips))



from shodan import WebAPI

SHODAN_API_KEY = ""

api = WebAPI(SHODAN_API_KEY)

# This example search a specific keyword in Shodan databae, and print the results.
try:
        # Search Shodan
        #results = api.search('web camera')
        results = api.search('webcam -www-authenticate +last-modified')
        print results
        
        import csv
        writer= csv.writer(open("./data/extra/webcam.csv", "wb"))
        
        #orig_stdout =sys.stdout
        f = file('out.txt', 'w')
        writer.writerow(['City','Country Name', 'IP', 'latitude', 'Longitude','Country Code', 'ISP', 'Organization'])
        print 'City',',','Country Name',',', 'IP',',', 'latitude',',', 'Longitude',',','Country Code',',', 'ISP',',', 'Organization'
        for result in results['matches']:
                #print 'IP: %s' % result['ip']
                #print result['data']
                print result
                #writer.writerow(result['ip'])
                writer.writerow([result['city'],result['country_name'], result['ip'], result['latitude'], result['longitude'], result['country_code'], result['isp'], result['org']])
                #print api.host(result['ip'])
                
                #print str(tuple([str(e) for e in result]))
                #print str(tuple(map(str, result)))
                #print result['city'] ,',', result['country_name'],',', result['ip'],',',result['latitude'],',',result['longitude'],',',result['country_code3'],',',result['isp'],',',result['org']
        
        print "printed !"
        
        
        #resultsAfterregex =re.compile('\'u\'city\': u\'([A-Z a-z]*)\'')
                #re.findall('\'u\'city\': u\'([A-Z a-z]*)\'', result, flags)
                
        #print re.findall('\'u\'city\': u\'([A-Z a-z]*)\'', results, 0)
                
except Exception, e:
       print 'Error: %s' % e
       #print 'Results found: %s' % results['total']
    
'''{
        'total': 8669969,
        'countries': [
                {
                        'code': 'US',
                        'count': 4165703,
                        'name': 'United States'
                },
                {'code': 'DE', 'count': 610270, 'name': 'Germany'},
                {'code': 'JP', 'count': 496556, 'name': 'Japan'},
                {'code': 'RO', 'count': 486107, 'name': 'Romania'},
                {'code': 'GB', 'count': 273948, 'name': 'United Kingdom'}
        ],
        'matches': [
                {
                        'country': 'DE',
                        'data': 'HTTP/1.0 200 OK\r\nDate: Mon, 08 Nov 2010 05:09:59 GMT\r\nSer...',
                        'hostnames': ['pl4t1n.de'],
                        'ip': '89.110.147.239',
                        'os': 'FreeBSD 4.4',
                        'port': 80,
                        'updated': '08.11.2010'
                },
                ...
        ]
        
} '''   
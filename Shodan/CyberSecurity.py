from shodan import WebAPI

SHODAN_API_KEY = "9LUSkTzrS8UgCyRaFSEPdMLU4FRDK9nS"

api = WebAPI(SHODAN_API_KEY)

# This example search a specific keyword in Shodan databae, and print the results.
try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip']
                print result['data']
                print ''
except Exception, e:
       print 'Error: %s' % e
    
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
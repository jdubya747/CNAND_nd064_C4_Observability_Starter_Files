
import requests

homepages = []
res = requests.get('https://api.openbrewerydb.org/breweries')
for result in res.json():
    print('Getting website for %s' % result['website_url'])
    #try:
        #homepages.append(requests.get(result['company_url']))
    #except:
    #    print('Unable to get site for %s' % result['company'])


    with tracer.start_span('get-beer-opportunities') as span:
        biers = []
        res = requests.get('https://api.openbrewerydb.org/breweries')
        span.set_tag('bier-tag', len(res.json()))
        for brewpub in res.json():
            try:
                biers.append(requests.get(brewpub['website_url']))
            except:
                return "Unable to get fact"
    return jsonify(biers)



        with tracer.start_span('get-python-jobs') as span:
        facts = []
        res = requests.get('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all')
        span.set_tag('facts-tag', len(res.json()))
        for fact in res.json():
            try:
                facts.append(requests.get(fact['fact']))
            except:
                return "Unable to get fact"
    return jsonify(facts)
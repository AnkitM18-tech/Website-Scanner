import os

def get_ip_address(url):
    command='nslookup '+url
    process=os.popen(command)
    results=str(process.read())
    marker=results.find('has address')+12
    return results[marker:].splitlines()[0]
# web mapper (in progress...)

Website mapper that should include a graph visualization function

## How to use it ?

```
python web_carto.py -h
```

```
usage: web_carto.py [-h] -u URL -o OUTPUT -e {txt,json} [--restricted-to-domain RESTRICTED_TO_DOMAIN]

Extract links and forms from a given URL

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Base URL to extract links and forms from
  -o OUTPUT, --output OUTPUT
                        output file
  -e {txt,json}, --extension {txt,json}
                        file format (txt or json)
  --restricted-to-domain RESTRICTED_TO_DOMAIN
                        Restricting the enumeration the a specified domain name
```

## Example of use

If you want to map a website limiting to a single domain name, you can execute a command like this :
```
python3 web_carto.py -u 'https://subdomain.domain/' -o 'output.json' -e 'json' --restricted-to-domain 'domain_name'
```

## requirements ?

see `requirements.txt`

```
beautifulsoup4==4.12.3
bs4==0.0.2
certifi==2024.12.14
charset-normalizer==3.4.0
idna==3.10
requests==2.32.3
soupsieve==2.6
urllib3==2.3.0
```

To install all of the requirements needed : 

```
pip install -r requirements.txt
```
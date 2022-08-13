# targeo
Target range calculator and ip geo lookup tool.


## Feautures
1. Continental IP ranges
2. National or Country IP ranges
3. Region and City IP ranges
4. IP to Geo Location
5. IP to internal provider information

## How to install
```
git clone https://github.com/cyberinspects/targeo
cd adminfinder
pip3 install -r requirements.txt
python3 targeo.py
```
## How to use
```
python3 targeo.py -t c -i AS                  {-t for range type c=continental, -i input {AS=Asia}}
python3 targeo.py -t c -i AS -o output.txt    {-t for range type c=continental, -i input {AS=Asia}, -o for outfile}
python3 targeo.py -t n -i IL                  {-t for range type n=nation/country, -i input {IL=isreal}}
python3 targeo.py -t r -i Jerusalem           {-t for range type r=region/city, -i input {Jerusalem}}
python3 targeo.py -l 127.0.0.1                {-l IP address to find geo and ISP information}}

```
#### options:
  -h, --help  show this help message and exit
  -t T        Range type (Allowed types are continent,nation and region)
  -l L        Ip address to find geo-location
  -i I        Input to specify the targeted range
  -o O        Output path and name

## Author
The script is developed by Kaleem Ibn Anwar (@kaleemibnanwar), He is a professional python programmer and Cyber Security expert. He is also the owner of cyberinspects vendor. You may follow or contact him on @kaleemibnanwar social media.
## Follow us!

##### Instagram: [@CyberInspects](https://instagram.com/cyberinspects)

##### Facebook: [@CyberInspects](https://facebook.com/cyberinspects)

##### Twitter: [@CyberInspects](https://twitter.com/cyberinspects)

##### LinkedIn: [@CyberInspects](https://linkedin.com/company/cyberinspects)

## YOUTUBE
[Subscribe Now](https://youtube.com/c/CyberInspects) 

## Contact
Email: [Send Mail](mailto:cyberinspects@Gmail.Com)

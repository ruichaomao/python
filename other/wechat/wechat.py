import itchat,time
from itchat.content import *
import requests

KEY = '46653ff2f959407da57e9ada472ce4f0'
ME = '@2df4bb846987e4e401e7da93e4fa09131e4ffc38cdedbb951ae18b74721f769e' #ziji
def get_response(msg):
	#shuju
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key'	: KEY,
		'info'	: msg,
		'userid'	: 'wechat-robot',
	}
	try:
		r = requests.post(apiUrl, data=data).json()
		return  r.get('text') + "\n"+"\t" + "---Note that I am just a robot."
	except:
		return
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
	print (msg['Text'])
	defaultReply = 'I received: ' + msg['Text']
	reply = get_response(msg['Text'])
	replymsg = reply or defaultReply
	print (replymsg)
	return replymsg
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
	msg.download(msg.fileName)
	typeSymbol = {
		PICTURE: 'img',
		VIDEO: 'vid' ,}.get(msg.type,'fil')
	return '@%s@%s' % (typeSymbol, msg.fileName)
@itchat.msg_register(FRIENDS)
def add_friend(msg):
	itchat.add_friend(**msg['Text'])
	itchat.send('Nice to meet you!',msg['RecommendInfo']['UserName'])
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
	print (msg['Text'])
	print ("to    ",msg['toUserName'])
	print ("from", msg['FromUserName'])
	defaultReply = 'I received: ' + msg['Text']
	reply = get_response(msg['Text'])
	replymsg = reply or defaultReply
	print(replymsg)
	return replymsg
itchat.auto_login(hotReload=True)
itchat.run(True)

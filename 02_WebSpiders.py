#!/usr/bin/env python
#coding:utf-8
# Python C:\Rei\Python\02_WebSpiders.py

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

########################### START ################################
from selenium import webdriver						#导入selenium
from selenium.webdriver.common.keys import Keys
import re
import json

def SearchInTwpro(name):
	driver.get('https://twpro.jp/search?word='+name)
	countContent=driver.find_elements_by_class_name("count")
	reCode=re.compile(r"\d{1,8}")
	tpValue=re.findall(reCode,countContent[0].text)
	return tpValue[0] 


driver = webdriver.Chrome()
namelist=("宮野真守","神谷浩史","鈴木達央","梶裕貴", "下野紘", "小野大輔", "蒼井翔太", "中村悠一", "櫻井孝宏", "福山潤", "鈴村健一", "柿原徹也", "岡本信彦", "木村良平",
	"寺島拓篤","杉田智和","細谷佳正", "前野智昭", "斉藤壮馬","谷山紀章","江口拓也","石田彰", "諏訪部順一", "森久保祥太郎","遊佐浩二","入野自由","増田俊樹", "鳥海浩輔", 
	"梅原裕一郎","花江夏樹", "島崎信長", "吉野裕行","小野賢章", "中井和哉","立花慎之介", "浪川大輔", "内山昂輝", "石川界人", "緑川光", "羽多野渉","代永翼","平川大輔", 
	"豊永利行","松岡禎丞","逢坂良太","安元洋貴", "津田健次郎", "近藤隆", "佐藤拓也","小野友樹","白井悠介","西山宏太朗","山下大輝","村瀬歩","内田雄馬","小林裕介"
)

fw=open("d:/"+"twpro"+".txt","w");
for name in namelist:
	fw.write("[\""+name+"\","+SearchInTwpro(name)+"]")
fw.close()

driver.quit()	

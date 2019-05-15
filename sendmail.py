#!usr/bin/python3
#-*-coding=UTF-8-*-
import smtplib #python 对SMTP的支持，smtplib这个库负责发送邮件
from email.mime.text import MIMEText #发送邮件要填充的成员
from email.header import Header #设置编码方式
import datetime #引入日期时间库
import string #引入字符串处理
import time
import sys
result=[]
with open('sendmailfile.txt','r') as f:
    for line in f:
        result.append(line.strip('\n'))
    sendmailset=set(result)
    #print(sendmailset)

dt = datetime.datetime.now()
str_time = dt.strftime('%Y-%m-%d %H:%M:%S')#用于在邮件发送标题栏 附上发送日期+时间
 
# #发送方邮件地址
sender = 'service@jishuapp.cn'
#发送方邮件设置的授权码
#pwd = 'xxxx'#填入发送方邮箱sender的授权码,注意不是密码，如何获取这个，请百度163邮箱获取SMTP/POP3获取授权码，即可知道
receivers = sendmailset #输入一个你要收取邮件的邮箱地址
 
#邮件的内容、收件人、发件人信息
#mail_message = '没有成功发送HTML'
maile_message = ""
#message = MIMEText('这是我使用python发送的邮件','plain', 'utf-8') #发送纯文本邮件
mail_message = '<html><body><h1>Hello</h1>' + \
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' + \
    '</body></html>'
mail_message = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>大事记_柏树镇同学发展促进会</title>
<meta name="keywords" content="大事记">
<meta name="description" content="柏树镇同学发展促进会本会是由在宣汉柏树华英中学毕业的学生自愿组成，不分所有制性质，自愿组成的地方性、非营利性的社会组织，是依法注册登记的社会团体法人。">
<link href="/css/style.css" rel="stylesheet" type="text/css" />
<script src="/css/jquery-1.4a2.min.js" type="text/javascript"></script>
<script src="/css/jquery.KinSlideshow-1.2.1.min.js" type="text/javascript"></script>
<script type="text/javascript">
$(function(){
	$("#KinSlideshow").KinSlideshow();
})
</script>
<style>
.m1b2{width:247px;  overflow:hidden;border:1px solid #e2e2e2;background-color:#f1f1f1;padding-left:0px; padding-top:0px;}
.m1b2 ul{padding:5px 10px 2px 5px;*padding:5px 10px 2px 5px;}
.m1b3{background-color:#da0e1a; padding-left:0px;}
.photo { max-width:125px;max-height:83px;width:expression(this.width > 125 ? "125px" : this.width);height:expression(this.height > 83 ? "83px" : this.height);overflow:hidden;}
</style>
</head>
<body>
<div class="content">
  <div class="header">
     <div class="h01"><a href="/"><img src="/img/banner.jpg" /></a></div>
     <div class="h02">
        <div id="beatles">
           <ul class="prodrop5">
              <li class="top p1"><a href="/" class="top_link pos">首页</a></li>
              <li class="aa2"></li>
              <li class="ab2"></li>
              <li class="top p2"><a href="/about/" class="top_link pos">本会概况<!--[if gte IE 7]><!--></a><!--<![endif]-->
               <!--[if lte IE 6]><table><tr><td><![endif]-->
               <ul>
			                    <li style=" width:85px; text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/about/jianjian/" title="本会简介">本会简介</a></li>                 <li style=" width:85px; text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/about/zhangcheng/" title="本会章程">本会章程</a></li>                 <li style=" width:85px; text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/about/jigou/" title="机构设置">机构设置</a></li>                 <li style=" width:85px; text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/about/ruhui/" title="入会指南">入会指南</a></li>               </ul>
               <!--[if lte IE 6]></td></tr></table></a><![endif]-->
              </li>
              <li class="aa2"></li>
              <li class="ab2"></li>
              <li class="top p3"><a href="/dongtai/" class="top_link pos">协会动态<!--[if gte IE 7]><!--></a><!--<![endif]-->
               <!--[if lte IE 6]><table><tr><td><![endif]-->
               <ul></ul>
               <!--[if lte IE 6]></td></tr></table></a><![endif]-->
              </li>
              <li class="aa2"></li>
              <li class="ab2"></li>
              <li class="top p7"><a href="/gonggao/" class="top_link pos">活动公告<!--[if gte IE 7]><!--></a><!--<![endif]-->
               <!--[if lte IE 6]><table><tr><td><![endif]-->
               <ul></ul>
               <!--[if lte IE 6]></td></tr></table></a><![endif]-->
              </li>
              <li class="aa2"></li>
              <li class="ab2"></li>
              <li class="top p4"><a href="/fengcai/" class="top_link pos">会员风采<!--[if gte IE 7]><!--></a><!--<![endif]-->
               <!--[if lte IE 6]><table><tr><td><![endif]-->
               <ul></ul>
               <!--[if lte IE 6]></td></tr></table></a><![endif]-->
              </li>
              <li class="aa2"></li>
              <li class="ab2"></li>
              <li class="top p5"><a href="/xinwen/" class="top_link pos">新闻中心<!--[if gte IE 7]><!--></a><!--<![endif]-->
               <!--[if lte IE 6]><table><tr><td><![endif]-->
               <ul></ul>
               <!--[if lte IE 6]></td></tr></table></a><![endif]-->
             </li>
             <li class="aa2"></li>
             <li class="ab2"></li>
             <li class="top current p6"><a href="/huzhu/" class="top_link pos">互帮互助<!--[if gte IE 7]><!--></a><!--<![endif]-->
               <!--[if lte IE 6]><table><tr><td><![endif]-->
               <ul>
			                    <li style=" width:85px;text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/huzhu/qiuzhi/" title="求职">求职</a></li>                 <li style=" width:85px;text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/huzhu/zhaopin/" title="招聘">招聘</a></li>                 <li style=" width:85px;text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/huzhu/zhaotongxue/" title="找同学">找同学</a></li>               </ul>
               <!--[if lte IE 6]></td></tr></table></a><![endif]-->
             </li>
             <li class="aa2"></li>
             <li class="ab2"></li>
             <li class="top current p6"><a href="/ziliao/" class="top_link pos">文件资料<!--[if gte IE 7]><!--></a><!--<![endif]-->
              <!--[if lte IE 6]><table><tr><td><![endif]-->
              <ul>
			                   <li style=" width:85px;text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/ziliao/cujinhui/" title="促进会">促进会</a></li>                 <li style=" width:85px;text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/ziliao/laozhaopian/" title="老照片">老照片</a></li>                 <li style=" width:85px;text-align:center; background-image:url(/img/dh2jbj.jpg);"><a href="/ziliao/juhui/" title="新聚会">新聚会</a></li>			  </ul>
              <!--[if lte IE 6]></td></tr></table></a><![endif]--></li>
             <li class="aa2"></li>
             <li class="ab2"></li>
             <li class="top current p6"><a href="/ruhui/" class="top_link pos">入会申请<!--[if gte IE 7]><!--></a><!--<![endif]-->
             　<!--[if lte IE 6]><table><tr><td><![endif]-->
             　<ul></ul>
             　<!--[if lte IE 6]></td></tr></table></a><![endif]-->
             </li>
             <li class="aa2"></li>
             <li class="ab2"></li>
             <li class="top current p6"><a href="/about/dashiji/" class="top_link pos">大事记<!--[if gte IE 7]><!--></a><!--<![endif]-->
             　<!--[if lte IE 6]><table><tr><td><![endif]-->
             　<ul></ul>
             　<!--[if lte IE 6]></td></tr></table></a><![endif]-->
              </li>
             <li class="aa2"></li>
             <li class="ab2"></li>
             <li class="top current p6"><a href="/liuyan/" class="top_link pos">留言板<!--[if gte IE 7]><!--></a><!--<![endif]-->
             　<!--[if lte IE 6]><table><tr><td><![endif]-->
             　<ul></ul>
             　<!--[if lte IE 6]></td></tr></table></a><![endif]-->
              </li>
           </ul>
       </div>
     </div>
  </div><div class="main">    
     <div class="left">
	    <div class="about">
		   <h3>关于我们</h3>
		   <div class="about1">
		      <ul>
			                    <li><a href="/about/jianjian/">本会简介</a></li>
			                    <li><a href="/about/zhangcheng/">本会章程</a></li>
			                    <li><a href="/about/jigou/">机构设置</a></li>
			                    <li><a href="/about/ruhui/">入会指南</a></li>
			                    <li><a href="/about/lianxi/">联系方式</a></li>
			                    <li><a href="/about/lingdao/">协会领导</a></li>
			                    <li><a href="/about/dashiji/" class="act">大事记</a></li>
			                    <li><a href="/about/changyishu/">同学倡议书</a></li>
			    			  </ul>
		   </div>
		</div>
	 </div>
	 <div class="right">
	    <div class="zhu_t"><h2>大事记</h2></div>
		<div class="zhu_b"><a href="http://www.baishuzhen.org/uploadfile/2014/1011/20141011110808189.docx">http://www.baishuzhen.org/uploadfile/2014/1011/20141011110808189.docx</a><br />
2014年9月10日，柏树镇同学发展促进会成立<br />
2014年10月2日，成功在柏树镇举办第一次会议<br />
2014.<strong>国庆茶话会内容部分重点：</strong><br />
  讨论过后决定聚会的时间是一年两次（国庆与春节前几天）、地点：国庆节轮值群主安排（可以是柏树、宣汉、达县）春节前聚只能在柏树。（特别说明同学间办酒席原则：不参加不送礼，送礼每人只送200元，以后就不要相互打电话问）<br />
 通过推荐、讨论过后鼓掌通过成为群主的有：袁小华、周素芳、熊华、向阳、袁娟五位群主，会后来通过群主讨论推选出杨旭、胡代云、周均三位加入群主的队伍中来。（根据我们选群主的标准，只要符合，后续还会选出新的群主），轮值坐庄群主可以是1人或者2人（安排下一次聚会的时间地点活动）。本次已选出下次春节前聚会轮值的群主是熊华、周素芳。<br />
</div>
	 </div>
  </div>
    <div class="footer">
      <div class="f1">柏树镇同学发展促进会版权所有，未经授权禁止复制或建立镜像</div>
      <div class="f2"><p>秘书处办公室电话：13594262384 袁小华　18696571773 周素芳</p>
<p>地址：四川省宣汉县柏树镇 邮编：636162</p>
<p>Copyright @ 2004-2020 All Rights Reserved　技术支持：<a href="http://www.pingmeibang.com/" target="_blank">整形点评</a> <a href="http://www.kaoruo.com/" target="_blank">学习网站</a></p></div>
    </div>
</div>
</body>
</html>
"""	
for receiver in receivers:
    print(receiver)
    message = MIMEText(mail_message,'html', 'utf-8') #发送含HTML内容的邮件
    message['To'] = receiver #填入收件人邮箱地址，用Header('聊天记录','utf-8')这个是绝对不行的，邮箱收和发的人的邮箱地址不用设置编码方式
    message['From'] =  sender #填入发件人邮箱地址，用Header('yj 和 DH','utf-8') 这个是绝对不行的，邮箱收和发的人的邮箱地址不用设置编码方式
    
    #邮件的标题
    #subject = 'Python SMTP 最新 邮件测试' + ' 发送时间： '+ str_time
    subject = 'Python SMTP 最新(含HTML内容)邮件测试' + ' 发送时间： '+ str_time
    #message['Subject'] = subject #可以不设置编码
    message['Subject'] = Header(subject,'utf-8')#也可以设置编码

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.jishuapp.cn', 465) #网易jishuapp.cn邮箱 使用非本地服务器，需要建立和网易邮件服务 的SSL链接，端口465
        smtpObj.login(sender, "west999@") #登录认证
        
        smtpObj.sendmail(sender,receiver,message.as_string()) #发送邮件主题
        print('邮件发送成功！')
    except smtplib.SMTPException as e:
        print('邮件发送失败，失败原因：',e)
    time.sleep(10)     

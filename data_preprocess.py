#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import re  # 导入正则表达式模块：re模块

# sys.setdefaultencoding('utf8')
import string
'''
sanjuban_1:
"三句半（古诗改编版）2015-1-2、歌谱控、人气:（载入中...）\n锄禾日当午， 汗滴禾下土。 谁知盘中餐， --有毒。 白日依山尽， 黄河入海流。 欲穷千里目， --有雾。 日照香炉生紫烟， 遥看瀑布挂前川。 飞流直下三千尺， --A股。 雕栏玉砌应犹在， 只是朱颜改。 问君能有几多愁， --要拆。 一去二三里， 烟村四五家。 亭台六七座， --豆腐渣。 远上寒山石径斜， 白云深处有人家。 停车坐爱枫林晚， --收费。 千山鸟飞绝， 万径人踪灭。 孤独蓑笠翁， --空巢。 葡萄美酒夜光杯， 欲饮琵琶马上催。 醉卧沙场君莫笑， --公费。 李白斗酒诗百篇， 长安市上酒家眠。 天子呼来不上船， --双规。\n"
"幼儿 表演 三句半2012-5-17、歌谱控、人气:（载入中...）\n六一到，\n喜洋洋，\n幼儿园里锣鼓响，\n咚咚咚咚哐!\n你笑得咧开嘴，\n我乐的把歌唱，\n今天咱们小朋友呀 \n心里真欢畅!\n天气真正好，\n我心里喜洋洋，\n看着咱们的幼儿园，\n漂亮!\n大树长的高，\n房子真漂亮，\n又有花来又有草，\n让我再瞧噍。\n这边坐着大哥哥\n那边坐着小弟弟\n挨个上台演节目\n瞧我的!\n我打鼓打得急\n我敲锣有力气\n我们几个一亮相\n神气!\n老师台下坐\n脸上笑咪咪\n我知道她心里想的啥?\n嗯，有出息。\n想想三年前，\n刚来幼儿园，\n都还穿着开裆裤，\n嗨，还提那干嘛!\n转眼上大班，\n样样都会干，\n唱歌、画画、扫地、擦桌，\n成了男子汉。\n原来是小调皮，\n天天恶作剧，\n这边闹来那边打，\n老师真着急。\n老师心里急，\n可脸上还笑咪咪，\n打人不是男子汉，\n嗯，服气!\n原来是小人精，\n现在是优等生，\n老师满脸都是笑，\n高兴!\n我们长大了，\n个子长高了，\n本事见来了，\n老师变老了。\n新千年新气象，\n老师又想新花样，\n上课就象做游戏，\n我爱上!\n我们都是小小鸟，\n幼儿园里飞得高，\n老师就象鸟妈妈，\n翅膀真大!\n今天我们来发言，\n老师的话儿记心间，\n从今往后好好干，\n决不捣乱!\n我们四个把鼓敲，\n节目不好图热闹，\n今天就先说到这儿，\n再见啦!\n"
"课间十分钟（三句半）2013-1-29、歌谱控、人气:（载入中...）\n课间休息十分钟，我们精神要轻松。下课铃声刚一响，往外冲！\n走廊楼道人攒动，个个活虎又生龙。要是撞倒就不妙，痛！\n行为举止要文明，追逐疯闹可不行。乱扔乱丢随意吐，恶心！\n入厕请你讲卫生，小便大便入池坑。不到地点随便撒，害人！\n小卖部里最热闹，柜台都被挤歪了。零食买了一大抱，撑死了！\n节制饮食才健康，肠胃不是集装箱。装得太多伤身体，遭殃！\n有的同学水平高，爱给别人取绰号。一喊别个心就烦，无聊！\n与人交往讲礼貌，见到师长要问好。语言文明又谦让，素质高！\n老师上课很辛劳，批改作业要动脑。要想打扰怎么说，报告！\n校园环境要美化，保洁工作靠大家。一见垃圾能捡起，顶呱呱！\n公共设施要爱惜，手不推来脚不踢。损坏公物要赔偿，该的！\n地面没有垃圾躺，桌椅整洁窗明亮。环境优美好学习，爽！\n课间虽只十分钟，知理明礼记心中。合理利用长知识，中！\n课间活动还蛮多，吃喝谈笑有娱乐。听到铃声进教室，上课！\n"
"公司三句半台词大全2015-5-1、歌谱控、人气:（载入中...）\n　　公司三句半台词大全\n　　1、工会活动特别好，爬山拔河做体操，强身健体展才艺，热闹。\n　　2、各位领导晚上好，欢迎大家都来到，不管说得好不好，别见笑。\n　　3、在座各位听我言，真情感激涌心间，美如祝福比蜜甜，能实现。\n　　4、信息服务很全面，大家围着网络转，各项工作不怠慢，都找俺！\n　　5、各位朋友谢谢你，百忙之中来到这里。今晚相聚在一起，为了庆祝隆中十周年厂庆。相会在这中秋月圆时，我们的心情高兴无比。啊， 我们的心情高兴无比。\n　　6、人事工作事不少，调动福利和功劳，一切为了员工好，有一票。\n　　7、俺们几个话挺多，大家不要嫌罗嗦，希望能够捧捧场，鼓掌！\n　　8、新年制定新目标，任务再翻也不高，只要大家齐努力，准超。\n　　9、超额完成又一年，看到成绩喜万千，代表大家表心愿 多发钱！\n　　10、中心成绩步步高，领导汗水不可少，领导班子一条心，协调！\n　　11、不管市场有多难， 人人都是英雄汉，个个都是敬业者，不一般！\n　　12、安全管理很重要，制度上墙警示牌，员工心里要记牢，真好（广东话）。\n　　13、公司今年能赚钱，长江药业来增添，精心生产和检验，不能偏（四川话）。\n　　14、建交成立十周年，咱们一起庆团圆，憧憬明天心儿醉，干杯！\n　　15、公司发展后劲足，还有3号4号地，产值要过几十亿，项目等着批。\n　　16、今年公司形势好，各大基地效益高，制药能源铝产业，赚钱。\n　　17、大家工作齐争先，学习中心领导班，正确树立人生观，比奉献\n　　18、企业识得东风面，集思广益内功练。挺柱开发取佳绩，1993年。\n　　19、综合物业搞创新，环境卫生抓的紧，建好食堂建车库，辛苦\n　　20、不管市场有多难，俊男靓女齐公关，业务水平不一般，签单（东北话）。\n　　21、规模发展在九五，浙江隆中显身手。锐意改革强企路，不停步！\n　　22、宾朋满座趁今宵，隆中发展业绩骄。借此舞台赊月色，表一表。\n　　23、大局下面齐行动，市场当中找定位，搞好创新求发展，全面。\n　　24、行政后勤很琐碎，里里外外都到位，每份付出都珍贵，不吃力（东阳话）。\n　　25、企业文化入人心，高科含量真不错，产品远销东南亚，值得夸。\n　　26、各大工程要建设，少了基建可不行，万丈高楼平地起，不马虎！\n　　27、上来说段三句半，大事小事胡乱侃，如有雷同你别喊，偶然。\n　　28、今年工作干得好，咱们千万别骄傲，领导开会搞总结，步步高！\n　　29、制动盘研发紧相连，科技创新记心间。紧握市场树诚信，94（就是）向前！\n　　30、为了今晚聚盛会，公司各部齐准备，精彩节目排着队，我们快退。\n　　31、档案事务很琐碎，您可别说无所谓，每份付出都珍贵，好累！\n　　32、公司老总水平高，科学决策勤思考，高科含量靠动脑，步步高。\n　　33、公司高楼一片片，基建部门有贡献，质量安全和进度，要督促（湖南话）。\n　　34、浙东玉环碧波涛，江山如画多姿娇。隆隆春雷遍大地，中兴潮。\n　　35、恰逢八月十五日，又值隆中厂庆时。双喜盈门好光景，真高兴！\n　　36、为了今天联欢会，我们辛苦来准备，下面还有好节目，俺们撤退。\n　　37、阿奇克拉好景观，锅炉水电操作班，齐心共把生产关，稳赚（宜都话）。\n　　38、今天说段三句半，说得不好多包涵，不管说得好不好，都别跑！\n　　39、签订单子真不少，海陆空运到处跑，产品销售不得了，创新高。\n　　40、支部工作细又妙，餐厅师傅手真巧，热菜热饭吃的好，别撑着。\n　　41、财务部门很关键，资金筹错不容易，员工收入钱不少，继续搞。\n　　42、领导同事大家好，新年马上要来到，我们先来拜个年 新年好！\n　　43、交易服务搞得好，创新意识不可少，团结拼搏又一年，猛收钱！\n　　44、宜都基地有巨变，二期投产快实现，生化明天更好看，使劲干。\n　　45、今晚大家来聚会，洗净一年苦和累，憧憬明天心儿醉，信心百倍。\n　　46、财务人员技能高，扛着算盘到处跑，精打细算搞节约，操劳！\n"

sanjuban_2:
锄禾日当午， 汗滴禾下土。 谁知盘中餐， --有毒。 白日依山尽， 黄河入海流。 欲穷千里目， --有雾。 日照香炉生紫烟， 遥看瀑布挂前川。 飞流直下三千尺， --A股。 雕栏玉砌应犹在， 只是朱颜改。 问君能有几多愁， --要拆。 一去二三里， 烟村四五家。 亭台六七座， --豆腐渣。 远上寒山石径斜， 白云深处有人家。 停车坐爱枫林晚， --收费。 千山鸟飞绝， 万径人踪灭。 孤独蓑笠翁， --空巢。 葡萄美酒夜光杯， 欲饮琵琶马上催。 醉卧沙场君莫笑， --公费。 李白斗酒诗百篇， 长安市上酒家眠。 天子呼来不上船， --双规。

六一到，
喜洋洋，
幼儿园里锣鼓响，
咚咚咚咚哐!
你笑得咧开嘴，
我乐的把歌唱，
今天咱们小朋友呀
心里真欢畅!
天气真正好，
我心里喜洋洋，
看着咱们的幼儿园，
漂亮!

课间休息十分钟，我们精神要轻松。下课铃声刚一响，往外冲！
走廊楼道人攒动，个个活虎又生龙。要是撞倒就不妙，痛！
行为举止要文明，追逐疯闹可不行。乱扔乱丢随意吐，恶心！

1、工会活动特别好，爬山拔河做体操，强身健体展才艺，热闹。
2、各位领导晚上好，欢迎大家都来到，不管说得好不好，别见笑。
3、在座各位听我言，真情感激涌心间，美如祝福比蜜甜，能实现。

'''
'''
·首先去除两端的双引号
·按\n分割每句话,去掉重复的\n\t\r
·去掉第一句话（+第二句话[台词、大全]）
·每句话可能是：1)多组三句半 2)三句半的每一句话 3)一组三句半
·"，。！"分割
'''
def normalizeToSanjuban(inputFile, outputFile):
    fin = open(inputFile, 'r',encoding='UTF-8')
    txt_originlist = fin.readlines()
    fin.close()
    rule = re.compile(u'[^a-zA-Z0-9.,;？！“”‘’@#￥%…&×——+-;；，。&～、|\s:：' + '\u4e00-\u9fa5]+')
    fout = open(outputFile, 'w',encoding='UTF-8')
    ii=1;
    txt_out="";
    for txt_origin in txt_originlist:
        txt_process=txt_origin.strip(string.ascii_uppercase) #去掉开头的大写字母
        txt_process = txt_process.strip(string.ascii_lowercase)#去掉开头的小写字母
        txt_process = txt_process.strip(string.digits)  # 去掉开头的数字
        #去掉括号及其内部文字
        txt_process = re.sub(u"\\(.*?\\)", "", txt_process) #去掉(xx)
        txt_process = re.sub(u"\\（.*?）", "", txt_process.encode('utf-8').decode()) # 去掉（xx）
        txt_process = re.sub(u"\\《.*?》", "", txt_process.encode('utf-8').decode())  # 去掉《xx》
        txt_process = re.sub(u"\\〈.*?〉", "", txt_process.encode('utf-8').decode())  # 去掉〈xx〉
        txt_process = re.sub('[甲乙丙丁齐――]', ' ', txt_process).strip()   # 去掉甲乙丙丁
        txt_process = re.sub("^([^\w]|_)+|�|([^\w]|_)+$", '', txt_process)#去掉字符串两端的标点符号
        txt_process = re.sub(rule, '', txt_process)
        txt_process = txt_process.strip()  # 去掉空格
#（鞠躬）
        length=len(txt_process)

        if length>0 and length<15 : #三句半中的一句
            if re.match('[ABCDabcd]*[0-9]*', txt_process) != None:  # 删除单独为字母的句子 和 单独为数字的句子
                txt_process = re.sub('[ABCD]*[0-9]*', "", txt_process, count=1)

            if ii % 2 == 1:
                txt_out=txt_out+txt_process+"，"
                ii += 1
            else:
                txt_out = txt_out + txt_process + "。"
                ii += 1
            if (ii-1) % 4 == 0:
                fout.write(txt_out + '\n')
                ii=1
                txt_out = "";

        else: #一组三句半 or 一堆堆三句半
            txt_split = re.split(r'[ !,-.:;?。！（），：；？~——]', txt_process.strip()) # 用标点符号分割短句
            for split in txt_split:
                if re.match('[ABCDabcd]*[0-9]*',split)!=None:# 删除单独为字母的句子 和 单独为数字的句子
                    idx=txt_split.index(split)
                    txt_split[idx] = re.sub('[ABCD]*[0-9]*', "", split,count=1)

            txt_split = [split.strip() for split in txt_split]
            txt_split = list(filter(None, txt_split))

            listlen=len(txt_split)
            if listlen % 4 == 0:            # 采用只有四个短句的三句半
                i=1
                for split in txt_split:
                    split=split.strip()
                    if i%2==1:
                        txt_out=txt_out+split.strip()+"，"
                        i+=1
                    else:
                        txt_out = txt_out + split.strip() + "。"
                        i += 1
                    if (i-1) % 4==0:
                        fout.write(txt_out + '\n')
                        txt_out="";

        # # 用标点符号分割短句，对每个短句，去除标点符号
        # txt_split = re.split(r'[，。！；？,!]', txt_process.strip())
        #
        # #对每个短句，去除它两端的标点符号,重新构建三句半
        # for split in txt_split:
        #     split= re.sub("^([^\w]|_)+|([^\w]|_)+$", '', split).strip()


        # line_split = [line.strip() for line in line_split if
        # line.strip() not in ['。', '！', '？', '；', '，'] and len(line.strip()) > 1]



        #
        # txt_split = txt_origin.split("\w")
        # linec = re.findall(r"[\w']+", txt_process)
        # print(linec)
        # result = " ".join(linec)
        # print(result)


    fout.close()



# 提取所有文字数据，得到格式布局较为杂乱的三句半
def organizeToSanjuban(inputFile, outputFile):
    fin = open(inputFile, 'r',encoding='UTF-8')
    txt_originlist = fin.readlines()
    fin.close()

    fout = open(outputFile, 'w',encoding='UTF-8')
    for txt_origin in txt_originlist:
        txt_origin=eval(txt_origin)
        txt_split=txt_origin.split("\n")
        for splits in txt_split:
            splits=splits.strip()
            if len(splits)>0:
                if splits.find("（载入中...）")==-1 and splits.find("台词")== -1 and splits.find("大全")== -1 :
                    if splits.find("★") == -1 and splits.find("【") == -1:
                        fout.write(splits+'\n')

    fout.close()


# 设置成训练数据格式 三句半名::三句半作者:: 三句半
def trainToSanjuban(inputFile, outputFile):
    fin = open(inputFile, 'r',encoding='UTF-8')
    txt_originlist = fin.readlines()
    fin.close()
    fout = open(outputFile, 'w',encoding='UTF-8')
    for txt_origin in txt_originlist:
        fout.write('三句半名:'+txt_origin )

    fout.close()

#删除重复项
def remove_duplication(inputFile, outputFile):
    fin = open(inputFile, 'r',encoding='UTF-8')
    txt_originlist = fin.readlines()
    fin.close()

    # txt_processlist=list(set(txt_originlist))
    txt_processlist = []
    for txt_origin in txt_originlist:
        if not txt_origin in txt_processlist:
            txt_processlist.append(txt_origin)

    fout = open(outputFile, 'w',encoding='UTF-8')
    for txt in txt_processlist:
        txt=txt[13:]
        fout.write('三句半名:'+txt )

    fout.close()


if __name__ == '__main__':
    txt_path_in = "sanjuban_1111.txt"
    txt_path_out = "sanjuban_2222.txt"
    organizeToSanjuban(txt_path_in, txt_path_out)

    txt_path_in = "sanjuban_2222.txt"
    txt_path_out = "sanjuban_3333.txt"
    normalizeToSanjuban(txt_path_in, txt_path_out)


    txt_path_in = "sanjuban_3333.txt"
    txt_path_out = "sanjuban_3333_train.txt"
    trainToSanjuban(txt_path_in, txt_path_out)

    txt_path_in = "sanjuban_tobeflitered.txt"
    txt_path_out = "sanjuban.txt"
    remove_duplication(txt_path_in, txt_path_out)


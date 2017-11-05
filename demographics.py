#coding:utf-8
import csv
import codecs

#with codecs.open("a020017.csv","r","cp932") as f:
#	dataReader = csv.reader(f)
#	for row in dataReader:
#		print row.decode("cp932")

prefecture = u"１７石　川"

with open("a020017.csv","r") as f:
	dataReader = csv.reader(f)
	for row in dataReader:
		print(row[0].decode("cp932"))
		print(row[0])
		print(prefecture)
		if row[0].decode("cp932") == prefecture:
			print("石川けん！！")
#		print(u"%sのデータです" % row[0].decode("cp932"))
#		print(u"出生数：%d" % row[1].decode("cp932"))
#			"出生数（2500g未満）："row[2].decode("cp932")
#			"死亡数："row[3].decode("cp932")
#			"死亡数（乳児死亡数）"：row[4].decode("cp932")
#			"新生児死亡数："row[5].decode("cp932")
#			"自然増減数："row[6].decode("cp932")
#			"死産数（総数）："row[7].decode("cp932")
#			"自然死産："row[8].decode("cp932")
#			"人工死産："row[9].decode("cp932")
#			"周産期死亡数（総数）："row[10].decode("cp932")
##			"早期新生児死亡数："row[12].decode("cp932")
import os
naukaStroka="взрыв физика химия биология организм ботаника живой термоядерная машина эксперимент прибор гаджет электричество взрыв ток технически пациент заболевания узи "
dobroyaStroka="привет пока спасибо хорошо умница нравится солнце жизнь замечательно дети потрясающе люблю понимаю будет пройдёт приятно подарок получится друзья пожалуйста заботу легко просто лучший хорощая хороший сок вода"
zlayaStroka="умерла умрет убьём уходи закрой уйди плохо плохой смерть убийство убил убьёт убийца бесит ненавижу прошло отвратительно черт враги сложно тяжело извини ужасно прекрати худший плохая плохой против покойник кровь водка алкогольлужи дождь против боль"
slengStroka="цыпочек  девка фигню бро чувак чувиха пацаны кореш кореша пацан детка братана братану окей грудь секс грудастые пошлые идиот идиотский голый голая нахер придурок спид сиськи "
stariVek =" знать князь барин старейшина король корлева короля замок замка царь динозаврь рыкарь королество заклятие чары магия заклинание "
vaka=stariVek.split(" ")
sleng = slengStroka.split(" ")
dobro = dobroyaStroka.split(" ")
zlo = zlayaStroka.split(" ")
nauka = naukaStroka.split(" ")
znaki = "!@\"№#$;%^:&?*()-+_={}[]'?.,:"
longestWord = "f"
dobri=0
zloy=0
slen=0
old=0
since=0
def onlyWords(fraza):
    i = 0
    fraza = fraza.lower()
    fraza += " "
    while i < len(fraza):
        if znaki.find(fraza[i]) != -1:
            fraza  = fraza[:i] + fraza[i+1:]
        i += 1

    words = fraza.split(" ")

    i=0
    global longestWord
    while i<len(words):

        if  words[i].isdigit() or words[i].find("<")!=-1 or not words[i].isalpha() or words[i].find("http")!=-1:
            words.remove(words[i])
        else:
            if len(longestWord) < len(words[i]):
                longestWord = words[i]
                print(longestWord)
            i+=1

    return words

os.chdir("Data")
globalInTxt = 0
globalData = {}
for serialName in os.listdir():

    os.chdir(serialName)
    print(serialName,)

    for seasonNumber in os.listdir():
        print(seasonNumber, )
        wordsInTxt = 0
        lexical = 0
        wordsCount = {}
        os.chdir(seasonNumber)
        for episodeSub in os.listdir():
            txt = ""
            try:
                file = open(episodeSub, "r",encoding='utf-8')
                txt = file.read()
            except Exception:
                file = open(episodeSub, "r")
                txt = file.read()

            lines = txt.split("\n")
            fraze = False

            for oneLine in lines:
                if len(oneLine) == 0:
                    fraze = False
                if fraze:
                    tmp =  onlyWords(oneLine)
                    wordsInTxt +=  len(tmp)
                    globalInTxt += len(tmp)
                    for word in tmp:
                        if wordsCount.get(word) == None:
                            wordsCount[word] = 1
                        else:
                            wordsCount[word] += 1

                        if globalData.get(word) == None:
                            globalData[word] = 1
                        else:
                            globalData[word] += 1

                if oneLine.find("-->") != -1:
                    fraze = True
        os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    listofTuples = sorted(wordsCount.items(), key=lambda x: (x[1]))
    listofTuples = reversed(listofTuples)
    f1 = open((serialName + '.txt'), "w")
    f1.write("\nКол-во слов:" + str(wordsInTxt) + "\nВсего различных слов:" + str(
        len(wordsCount)) + "\nСамое длинное слово:" + longestWord + "\n")

    longestWord=""
    for elem in listofTuples:
        if  elem[0] in dobro:
            dobri+=elem[1]
        if  (elem[0])in zlo :
            zloy+=elem[1]
        if  (elem[0])in sleng:
            slen+=elem[1]
        if  (elem[0])in vaka:
            old+=elem[1]

        if  (elem[0])in nauka:
            since+=elem[1]



        f1.write(str(elem[0]) + " :: " + str(elem[1]) + " - " + str((elem[1] / wordsInTxt) * 100)[:6] + "\n")
    f1.write(str(dobri/wordsInTxt*1000)[:5]+"/ db / "+ str(zloy/wordsInTxt*1000)[:5]+" sl/"+str(slen/wordsInTxt*10000)[:5]+" sl/"+str(old/wordsInTxt*10000)[:5]+"sl/"+str(since/wordsInTxt*10000)[:5])
    zloy=0
    dobri=0
    slen=0
    old=0
    since=0

    os.chdir("Data")

listofTuples = sorted(globalData.items(), key=lambda x: (x[1]))
listofTuples = reversed(listofTuples)
os.chdir('..')
f1 = open(('!Global.txt'),"w",encoding="utf8")
f1.write("Кол-во слов:" + str(globalInTxt ) + "  Всего различных слов:" + str(len(globalData))+"\n")
for elem in listofTuples:
    f1.write(str(elem[0])+ " :: "+ str(elem[1])+"\n" )


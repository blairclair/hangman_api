from flask import Flask
import random
app = Flask(__name__)

EasyWords = ["about","above","across","active","activity","afraid","after","again","agree","alone","along","already","always","amount","angry","another","answer","anyone","anything","anytime","appear","apple","area","army","around","arrive","attack","aunt","autumn","away baby","back","ball","bank","base","basket","bath","bean","bear","beautiful","bedroom","beer","behave","before","begin","behind","bell","below","besides","best","better","between","bird","birth","birthday","bite","black","bleed","block","blood","blow","blue","board","boat","body","boil","bone","book","border","born","borrow","both","bottle","bottom","bowl","branch","brave","bread","break","breakfast","breathe","bridge","bright","bring","brother","brown","brush","build","burn","business","busy","cake","call","candle","card","care","careful","careless","carry","case","catch","central","century","certain","chair","chance","change","chase","cheap","cheese","chicken","child","children","chocolate","choice","choose","circle","city","class","clever","clean","clear","climb","clock","cloth","clothes","cloud","cloudy","close","coffee","coat","coin","cold","collect","colour","comb","comfortable","common","compare","come","complete","computer","condition","continue","control","cook","cool","copper","corn","corner","correct","cost","contain","count","country","course","cover","crash","cross","cupboard","dance","dangerous","dark","daughter","dead","decide","decrease","deep","deer","depend","desk","destroy","develop","different","difficult","dinner","direction","dirty","discover","dish","door","double","down","draw","dream","dress","drink","drive","drop","duck","dust","duty","each","early","earn","earth","east","easy","education","effect","eight","either","electric","elephant","else","empty","enemy","enjoy","enough","enter","equal","entrance","escape","even","evening","event","ever","every","everyone","exact","everybody","examination","example","except","excited","exercise","expect","expensive","explain","extremely","face","fact","fail","fall","false","family","famous","farm","father","fast","fault","fear","feed","feel","female","fever","fight","fill","film","find","fine","finger","finish","fire","first","fish","five","flag","flat","float","floor","flour","flower","fold","food","fool","foot","football","force","foreign","forest","forget","forgive","fork","form","four","free","freedom","freeze","fresh","friend","friendly","from","front","fruit","full","funny","furniture","further","future","game","garden","gate","general","gentleman","gift","give","glad","glass","goat","gold","good","goodbye","grandfather","grandmother","grass","grave","great","green","gray","ground","group","grow","hair","half","hall","hammer","hand","happen","happy","hard","hate","have","head","healthy","hear","heavy","heart","heaven","height","hello","help","here","hers","hide","high","hill","hobby","hold","hole","holiday","home","hope","horse","hospital","hotel","house","hundred","hungry","hour","hurry","husband","hurt","idea","important","increase","inside","into","introduce","invent","iron","invite","island","jelly","join","juice","jump","just","keep","kill","kind","king","kitchen","knee","knife","knock","know","ladder","lady","lamp","land","large","last","late","lately","laugh","lazy","lead","leaf","learn","leave","left","lend","length","less","lesson","letter","library","life","light","like","lion","list","listen","little","live","lock","lonely","long","look","lose","love","lower","luck","machine","main","make","male","many","mark","market","marry","matter","meal","mean","measure","meat","medicine","meet","member","mention","method","middle","milk","million","mind","minute","miss","mistake","model","modern","moment","money","monkey","month","moon","more","morning","most","mother","mountain","mouth","move","much","music","must","name","narrow","nation","nature","near","nearly","neck","need","needle","neighbour","neither","never","news","newspaper","next","nice","night","nine","noble","noise","none","north","nose","nothing","notice","number","obey","object","ocean","offer","office","often","only","open","opposite","orange","order","other","outside","over","page","pain","paint","pair","paper","parent","park","part","partner","party","pass","past","path","peace","pencil","people","pepper","perfect","period","person","petrol","photograph","piano","pick","picture","piece","pink","place","plane","plant","plastic","plate","play","please","pleased","plenty","pocket","point","poison","police","polite","pool","poor","popular","position","possible","potato","pour","power","present","press","pretty","prevent","price","prince","prison","private","prize","probably","problem","produce","promise","proper","protect","provide","public","pull","punish","pupil","push","queen","question","quick","quiet","quite","radio","rain","rainy","raise","reach","read","ready","real","really","receive","record","remember","remind","remove","rent","repair","repeat","reply","report","rest","restaurant","result","return","rice","rich","ride","right","ring","rise","road","rock","room","round","rubber","rude","rule","ruler","rush","safe","sail","salt","same","sand","save","school","science","scissors","search","seat","second","seem","sell","send","sentence","serve","seven","several","shade","shadow","shake","shape","share","sharp","sheep","sheet","shelf","shine","ship","shirt","shoe","shoot","shop","short","should","shoulder","shout","show","sick","side","signal","silence","silly","silver","similar","simple","single","since","sing","sink","sister","size","skill","skin","skirt","sleep","slip","slow","small","smell","smile","smoke","snow","soap","sock","soft","some","someone","something","sometimes","soon","sorry","sound","soup","south","space","speak","special","speed","spell","spend","spoon","sport","spread","spring","square","stamp","stand","star","start","station","stay","steal","steam","step","still","stomach","stone","stop","store","storm","story","strange","street","strong","structure","student","study","stupid","subject","substance","successful","such","sudden","sugar","suitable","summer","sunny","support","sure","surprise","sweet","swim","sword","table","take","talk","tall","taste","taxi","teach","team","tear","telephone","television","tell","tennis","terrible","test","than","that","their","then","there","therefore","these","thick","thin","thing","think","third","this","though","threat","three","tidy","title","today","together","tomorrow","tonight","tool","tooth","total","touch","town","train","tram","travel","tree","trouble","true","trust","twice","turn","type","ugly","uncle","under","understand","unit","until","useful","usual","usually","vegetable","very","village","voice","visit","wait","wake","walk","want","warm","wash","waste","watch","water","weak","wear","weather","wedding","week","weight","welcome","were","well","west","what","wheel","when","where","which","while","white","wide","wife","wild","will","wind","window","wine","winter","wire","wise","wish","with","without","woman","wonder","word","work","world","worry","yard","yell","yesterday","young","your","zero"]
HardWords = ["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","ovary","oxidize","oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","voodoo","vortex","voyeurism","walkway","waltz","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern","xylophoneyachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]

@app.route('/firstdisplay/<word>')
def GetFirstDisplay(word):
	NewWord = ""
	i = 0
	WordLen = len(word)
	while i < WordLen:
		NewWord = NewWord + "_ "
		i = i + 1
	return NewWord

@app.route('/checkletter/<let>/<word>/<current>')
def CheckWord(let,word,current):
	let = let[0]
	if let in word:
		NewWord = ""
		j = 0
		LenWord = len(word)
		for i in range(0,LenWord):
			if word[i] == let:
				NewWord = NewWord + let
				print("nw", NewWord)
			else:
				NewWord = NewWord + current[j] + " "
			j = j + 2
		return NewWord
	return current

@app.route('/easy', methods=['GET'])
def GetEasyWord():
	return EasyWords[random.randrange(0,849)]

@app.route('/hard', methods=['GET'])
def GetHardWord():
	return HardWords[random.randrange(0,203)]

@app.route('/', methods=['GET'])
def GetRandomWord():
	num = random.randrange(0, 1052)
	if num <= 849:
		print("easy")
		return EasyWords[num]
	else:
		print("hard")
		return HardWords[num - 849]
if __name__ == '__main__':
	app.run(debug=True)
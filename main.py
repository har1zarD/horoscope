"""
Dobrodišli u PROGRAM ZA ODREĐIVANJE HOROSKOPSKOG ZNAKA
PREDMET: SOFTVERSKI STUDIO 3
STUDENT: HARIS VELIC
PROFESOR: PROF. DOC. VELIMIR DEDIC
DIFERENCIJALNI PREDMET !
"""

#POČETAN PROJEKTA

print("Saznajte svoj horoskopski znak i nešto više o vama!")
print('')
dan = int(input("Unesite svoj dan rođenja (1 - 31): "))
mjesec = input("Unesite svoj mjesec rođenja (januar,februar... - decembar): ")

#HOROSKOPSKI ZNAKOVI I MJESECI
if mjesec == 'april':
	horoskopski_znak = 'Ovan' if (dan < 21) else 'Bik'
elif mjesec == 'maj':
	horoskopski_znak = 'Bik' if (dan < 21) else 'Blizanac'
elif mjesec == 'juni':
	horoskopski_znak = 'Blizanac' if (dan < 21) else "Rak"
elif mjesec == 'juli':
	horoskopski_znak = 'Rak' if (dan < 21) else 'Lav'
elif mjesec == 'august':
	horoskopski_znak = 'Lav' if (dan < 23) else 'Djevica'
elif mjesec == 'septembar':
	horoskopski_znak = 'Djevica' if (dan < 23) else 'Vaga'
elif mjesec == 'oktobar':
	horoskopski_znak = 'Vaga' if (dan < 23) else 'Škorpion'
elif mjesec == 'novembar':
	horoskopski_znak = 'Škorpion' if (dan < 23) else 'Strijelac'
elif mjesec == 'decembar':
	horoskopski_znak = 'Strijelac' if (dan < 23) else 'Jarac'
elif mjesec == 'januar':
	horoskopski_znak = 'Jarac' if (dan < 22) else 'Vodenjak'
elif mjesec == 'februar':
	horoskopski_znak = 'Vodenjak' if (dan < 20) else 'Riba'
elif mjesec == 'mart':
	horoskopski_znak = 'Riba' if (dan < 20) else 'Ovan'
else:
    print("***NEPRAVILAN UNOS***")

#FUNKCIJE ZA NEPRAVILAN UNOS

if mjesec == 'januar' and dan > 31 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'februar' and dan > 29 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'mart' and dan > 31 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'april' and dan > 30 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'maj' and dan > 31 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'juni' and dan > 30 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'juli' and dan > 31 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'august' and dan > 31 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'septembar' and dan > 30 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'oktobar' and dan > 31 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'novembar' and dan > 30 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()
elif mjesec == 'decembar' and dan > 31 or dan < 1:
    print("*** NEPRAVILAN UNOS (Taj datum ne postoji) ***")
    exit()

#PART 2.

print("Vaš horoskopski znak je :", horoskopski_znak)
nesto_vise = "[1. Zdravlje, 2. Ljubav, 3. Posao]"
print("Ukoliko vas zanima nešto više o vašem horoskopskom znaku, upišite")
print(nesto_vise)
odgovor = int(input("Unesite broj 1, 2 ili 3: "))
if odgovor < 1 or odgovor > 3:
    print("*** NEPRAVILAN UNOS (Taj broj nije ponuđen) ***")
    odgovor = int(input("Unesite broj 1, 2 ili 3: "))

#ZDRAVLJE, LJUBAV, SRECA
 
if horoskopski_znak == 'Ovan' and odgovor == 1:
    print("Ovan vlada područjem glave, pa su pripadnici ovog znaka često skloni migrenama, glavoboljama, problemima sa sinusima, a nerijetko im teškoće zadaje i vid. Skloni su upalama, virozama i ozljedama, a nerijetko imaju problema i sa srcem, kolesterolom i visokom tlakom.")
elif horoskopski_znak == 'Ovan' and odgovor == 2:
    print ("Ovan je vatreni znak koji obožava da flertuje i svakako je osoba koja će preuzeti inicijativu kada dođe do romanse. Kada im neko zapadne za oko, brzo će reagovati. Ipak da bi zadržali pažnju ovna morate biti isto toliko energični i uzbudljivi kao i on. Osobe rođene u znaku ovna su izuzetno strastvene i obožavaju avanturu")
elif horoskopski_znak == 'Ovan' and odgovor == 3:
    print("Ovo je oblast u kojoj ovan sija najsjajnije. Radno okruženje je savršen prostor za, ambicioznog, kreativnog i često vođenog potrebom da bude što bolji, ovna. Rođeni lider, uvek će radije izdavati porudžbine, nego ih primati. Odlična sposobnost predviđanja omogućuje ovnu da uvek bude korak ispred i da postavi stvari na svoje mesto. Sve što ovan treba da uradi je da prati svoj odabrani put.")
elif horoskopski_znak == 'Bik' and odgovor == 1:
    print("Bikove osjetljive točke su grlo i glasnice, pa mnogi imaju čestih problema s upalama grla, laringitisom ili bronhitisa. Snažne su građe i obično imaju jak imunitet, no hedonistički način života često im ugrožava zdravlje, pa mnogi imaju problem sa šećerom, kolesterolom ili gušteračom.")
elif horoskopski_znak == 'Bik' and odgovor == 2:
    print("Kao pravi štićenici Venere, planeta ljubavi, pripadnici ovog znaka su iznimno senzualni i puteni. Bikovi nisu koketi poput Vaga, kojima također vlada Venera, no iznimno su privlačni suprotnom spolu pa oko sebe uvijek imaju pokojeg udvarača. U mladosti su skloni lutanju, pogotovo muškarci, koji su uvijek okruženi ženama, no što su stariji, sve više se žele skrasiti i zasnovati obitelj.")
elif horoskopski_znak == 'Bik' and odgovor == 3:
    print("a Bika je materijalna sigurnost iznimno bitna životna stavka, stoga će nastojati pronaći dobro radno mjesto sa solidnom plažom. Ovi ljudi obično imaju smisao za upravljanje financijama i poduzetnički duh, pa se dobro snalaze kao obrtnici, vlasnici firma i poduzeća.")
elif horoskopski_znak == 'Blizanac' and odgovor == 1:
    print("Ljudi rođeni u ovom znaku obično su vrlo nervozni i razdražljivi, a nemir pokušavaju odagnati cigaretama, koje pak imaju iznimno negativan utjecaj na njihovo zdravlje. Prestanak pušenja od ključne je važnosti za sve Blizance, budući da su im najosjetljivije točke pluća i dišni organi.")
elif horoskopski_znak == 'Blizanac' and odgovor == 2:
    print("Blizanci su zaljubljive i šarmantne osobe koje uživaju u flertu, kojeg se ne odriču čak i kad su u vezi. Partner im često zamjera upravo tu sklonost ka očijukanju, no trebao bi shvatiti da Blizanci samo traže zabavu i uzbuđenje, i vjerojatno nikad neće poduzeti ništa konkretno.")
elif horoskopski_znak == 'Blizanac' and odgovor == 3:
    print("Ovo su iznimno inteligentni i bistri ljudi koji s lakoćom uče i usvajaju nove informacije, stoga se odlično snalaze u raznim područjima. Nekad im je teško odabrati karijeru, budući da su podjednako uspješni i spretni u raznim područjima. Ipak, često se opredijele za zanimanje pisca, novinara, profesora, lektora ili se bave nekim drugim poslom u kojem će moći iskoristiti svoju elokvenciju i talent za pisanje.")
elif horoskopski_znak == 'Rak' and odgovor == 1:
    print("Rak spada u red osjetljivih znakova, i u emocionalnom i u zdravstvenom pogledu. Ovaj znak upravlja prsnim košem i želucem, su mu osjetljive točke svi organi koji se tu nalaze (gornji trbuh, donji otvor želuca, pankreas). Međutim, kako je vrlo emotivan, spada i u psihički osjetljive znakove.")
elif horoskopski_znak == 'Rak' and odgovor == 2:
    print("Kad Rak voli, on voli svim srcem i ništa mu nije teško napraviti za svog odabranika. Vrlo je nježan, pažljiv i strpljiv, a spreman je i mnogo toga pretrpjeti u ime ljubavi. Ipak, ono što mu se često prigovara jest prevelika osjetljivost.")
elif horoskopski_znak == 'Rak' and odgovor == 3:
    print("Premda odaju dojam skromnih i nenametljivih osoba, Rakovi su iznimno vrijedni i sposobni radnici koji ulažu mnogo truda u posao. Važno im je da se bave poslom koji će ih činiti sretnima, dok su im slava i priznanja od sporedne važnosti.")
elif horoskopski_znak == 'Lav' and odgovor == 1:
    print("Vatreni Lav upravlja vitalnim tjelesnim funkcijama - radom srca i krvotokom. Poslovično je dobrog zdravlja, prepun energije, plodan i izdržljiv. No, ne podnosi dobro bol, a posebno čekanje kod liječnika i odlazak stomatologu. Premda djeluje samopouzdano i snažno, zna biti vrlo plašljiv u opasnim situacijama.")
elif horoskopski_znak == 'Lav' and odgovor == 2:
    print("Ovaj je znak u svemu teatralan i dramatičan, stoga će se tako ponašati i u ljubavnim vezama. Kad se zaljubi, spreman je na mnoge romantične geste kako bi impresionirao voljenu osobu i uvjerio je da bi mu trebala dati priliku. Šarmantan, samouvjeren i neodoljivo privlačan, čega je i sam svjestan.")
elif horoskopski_znak == 'Lav' and odgovor == 3:
    print("Lavovi vole biti u središtu pozornosti, što ih čini rođenim vođama. Ponosni su, energični i odvažni, a u okolini izazivaju strahopoštovanje. Velikodušni su i pravedni, zbog čega ih većina suradnika poštuje, unatoč tome što često znaju biti egocentrični i tvrdoglavi.")
elif horoskopski_znak == 'Djevica' and odgovor == 1:
    print("Djevica je često pesimistična i zabrinuta, stoga često ima želučane smetnje, gastritis ili čir na želucu. Preporučuje im da se bave jogom ili nekom drugom opušatjućom aktivnošću,, jer je miran život lišen stresa ključan za njihovo dobro zdravlje.")
elif horoskopski_znak == 'Djevica' and odgovor == 2:
    print("Djevici treba mnogo vremena da se opusti i pokaže svoje prav eosjećaje. Na početku veze je oprezna i suzdržana, a gotovo nikad prva ne izjavljuje ljubav. Iako ne zna izraziti što osjeća, sitnim gestama i iskazivanjem pažnje dat će do znanja drugoj strani koliko im znači.")
elif horoskopski_znak == 'Djevica' and odgovor == 3:
    print("Marljiva, uporna i organizirana osoba poput Djevice odlično se snalazi u poslovima administracije, koje većina drugih ljudi smatra dosadnima. Stroljiva je, precizna i posjeduje dobar smisao za detalje, a perfekcionizam je tjera da svaki psoao nastoji obaviti najbolje što može.")
elif horoskopski_znak == 'Vaga' and odgovor == 1:
    print("U životu im je najvažnija ljubav i kvalitetan brak, pa ako su tu nezadovoljne, bit će podložnije stresu i bolestima. Dosta pažnje polažu na vanjski izgled, stalo im je da izgledaju lijepo i atraktivno, pa ako je u modi mršavost, izgladnjivat će se dok ne postigne željenu težinu.")
elif horoskopski_znak == 'Vaga' and odgovor == 2:
    print("Vagama je ljubav uvijek najvažnija stvar na svijetu, a bez partnera, svoje druge polovice, ne mogu funkcionirati. Upravo to je razlog zbog kojeg često ulaze u loše veze s ljudima koji im ne odgovaraju, samo zbog straha od samoće.")
elif horoskopski_znak == 'Vaga' and odgovor == 3:
    print("Vage su rođeni diplomati, čija je najveća prednost sposobnost da sagledaju sve aspekte nekog problema. Imaju izražen osjećaj za pravdu, vole timski rad i iznimno su miroljubive, što ih čini osobama s kojima je vrlo poželjno surađivati.")
elif horoskopski_znak == 'Škorpion' and odgovor == 1:
    print("Škorpione krasi izuzetna energija i snažna mišićna građa, čak i kad su vrlo mršavi. Žilavi su i otporni, a zahvaljujući vladarima Marsu i Plutonu, brzo se oporavljaju i nakon teških bolesti. Erotični su i strastveni, a da bi normalno funkcionirali, bitno je da imaju zadovoljavajući seksualni život.")
elif horoskopski_znak == 'Škorpion' and odgovor == 2:
    print("Škorpioni su u svemu strastveni, što ponajviše dolazi do izražaja u ljubavnom životu. Vrlo su nepovjerljivi pa su u početku veze nemogući, jer stalno provjeravaju partnera, a njihovom detektivskom oku ništa ne može promaknuti.")
elif horoskopski_znak == 'Škorpion' and odgovor == 3:
    print("U ovom je znaku rođen velik broj uspješnih poduzetnika i biznismena, što se može objasniti njihovom odvažnošću i spremnošću na povlačenje riskantnih poteza. Škorpioni su odlučni i sposobni radnici koji ne priznaju poraze i nikad ne bježe od problema.")
elif horoskopski_znak == 'Strijelac' and odgovor == 1:
    print("Strijelca krasi neuništiv optimizam i velikodušnost. Voli sport i rekreaciju, no njegov hedonizam može prevagnuti, pa je sklon davati prednost ovozemaljskim užicima nad aktivnom tjelovježbom.")
elif horoskopski_znak == 'Strijelac' and odgovor == 2:
    print("Strijelac je i po pitanju ljubavi veliki entuzijast. Uvijek je u potrazi za idealnim partnerom, pri čemu često griješi, ponajviše zbog svoje impulzivnosti i nepromišljenosti. Zaljubljiv je i pomalo naivan, pa je često laka meta ljudima sumnjivih namjera.")
elif horoskopski_znak == 'Strijelac' and odgovor == 3:
    print("Svestrani i nesputani Strijelci osobe su koje bi svatko poželio imati u svojem timu. Osim što su nedvojbeno sposobni i posjeduju zavidne komunikacijske vještine, u radnu atmosferu unose vedrinu i entuzijazam koji povoljno utječu na motivaciju.")
elif horoskopski_znak == 'Jarac' and odgovor == 1:
    print("Boležljiv u djetinjstvu, s godinama postaje čvršći, žilaviji i otporniji. Njegov je vladar hladni i opori Saturn koji tijelo izvrgava brojnim bolestima, ali ga istovremeno hrani iskustvima i antivirusima.")
elif horoskopski_znak == 'Jarac' and odgovor == 2:
    print("Suzdržan, oprezan i nesiguran jarac sigurno nije osoba koja se lako opušta pred drugima, no unatoč tome, mogu biti pravi zavodnici. Jarcima je lakše ući u površnu vezu s osobom koja im ne znači mnogo")
elif horoskopski_znak == 'Jarac' and odgovor == 3:
    print("Jarci su rođeni vođe koji često imaju prevelike zahtjeve od svojih suradnika, no i sami uvijek daju svoj maksimum. Vrlo su odgovorni i organizirani te su živi primjer radoholičara kojima je karijera najvažnija stvar u životu.")
elif horoskopski_znak == 'Vodenjak' and odgovor == 1:
    print("Vodenjak vlada cirkulacijom krvi i limfe, te ravna donjim dijelom tijela, potkoljenicama i gležnjevima, pa su mu to ujedno ranjive točka. Njegovi pripadnici skloni su problemima s cirkulacijom krvi i limfom, venama, bolnim i natečenim nogama, ravnim stopalima")
elif horoskopski_znak == 'Vodenjak' and odgovor == 2:
    print("Kad se zaljube, Vodenjaci to obično razglase na sva zvona. Osobu koja im je zaokupila pažnju vrlo lako mogu zavesti velikim romantičnim gestama i iznimnim šarmom. Postoji i drugi, suzdržaniji tip Vodenjaka, kojem je dominantan utjecaj suvladaoca Saturna, koji krije osjećaje u sebi i pokazuje ih tek u iznimnim prilikama.")
elif horoskopski_znak == 'Vodenjak' and odgovor == 3:
    print("Vodenjaci su idealisti i buntovnici koji u svemu čega se prihvate nastoje biti posebni i originalni. Većinom posjeduju kreativni talent koji im omogućuje da se bave umjetnošću ili nekim drugim zanimanjem koje nema fiksno radno vrijeme.")
elif horoskopski_znak == 'Riba' and odgovor == 1:
    print("Ribe su intuitivne, osjećajne, požrtvovne, ali i psihički nestabilne. Podložne su i tuđem uplivu, pa ako je on negativan, i same će krenuti u krivom smjeru. Sklone su psihosomatskim tegobama, raznim ovisnostima i poremećajima sna.")
elif horoskopski_znak == 'Riba' and odgovor == 2:
    print("Pripadnici Riba često se opisuju kao nepopravljivi romantičari, što je donekle istina. Ovi ljudi ne mogu živjeti bez ljubavi, stoga im je partner potreban kako bi mu pružio svu silnu ljubav i emocije koje se u njima kriju. Kad se zaljube, Ribe postaju ranjive, no ne boje Se pokazati svoje osjećaje.")
elif horoskopski_znak == 'Riba' and odgovor == 3:
    print("Ribe imaju potrebu baviti se poslom koji im predstavlja užitak te mu se mogu potpuno predati, zbog čega su uspješne u svemu čega se prihvate. S druge strane, ako se bave zanimanjem koje ne vole, njihovi će rezultati biti mizerni i slabi")
print ('')
print("Hvala vam što ste koristili ovaj program!")
exit()

#!/usr/bin/env python2

cipher =  [360575205516272353647725959973923332922859934062623515990157287L, 147121471099487603100103942210642238821212368870164629959708554L, 973776523698456974485285268207248463304785539161797442415515724L, 973776523698456974485285268207248463304785539161797442415515724L, 1989542264845745277130976293069288745712944297723265109141551240L, 2251682090999461666252822948628263912168715816760972058692440747L, 147121471099487603100103942210642238821212368870164629959708554L, 500999802327659646334011021043663318493321568487210306739944859L, 147121471099487603100103942210642238821212368870164629959708554L, 690110490875978577594520719909097376417907156757045161010173205L, 1516765543474947948979702045905703600901480327048677973465980375L, 1446553245069254302636559515370833608116249509836384578091086589L, 1989542264845745277130976293069288745712944297723265109141551240L, 1351997900795094837006304665938116579153956715701467150955972416L, 1516765543474947948979702045905703600901480327048677973465980375L, 1684350025354504872471293852031961738394959051951467495881755709L, 2251682090999461666252822948628263912168715816760972058692440747L, 595555146601819111964265870476380347455614362622127733875059032L, 1162887212246775905745794967072682521229371127431632296685744070L, 2273208297668223674021740841367439832599822680128017390546893759L, 1800431576297426345870466594203854687788358709453430254871322894L, 2251682090999461666252822948628263912168715816760972058692440747L, 2273208297668223674021740841367439832599822680128017390546893759L, 1800431576297426345870466594203854687788358709453430254871322894L, 2251682090999461666252822948628263912168715816760972058692440747L, 1516765543474947948979702045905703600901480327048677973465980375L, 1989542264845745277130976293069288745712944297723265109141551240L, 1705876232023266880240211744771137658826065915318512827736208721L, 690110490875978577594520719909097376417907156757045161010173205L, 2251682090999461666252822948628263912168715816760972058692440747L, 1257442556520935371376049816505399550191663921566549723820858243L, 973776523698456974485285268207248463304785539161797442415515724L, 336232159647806534360613641076076296745797957139999484229936900L, 52566126825328137469849092777925209858919574735247202824594381L, 1022462615435388613059509906002942535658909493007045505935956498L, 2251682090999461666252822948628263912168715816760972058692440747L, 1470896290937720121923671834268680644293311486759008609851306976L, 998119569566922793772397587105095499481847516084421474175736111L, 1470896290937720121923671834268680644293311486759008609851306976L, 2108440654988370562048343461399852810852299068780806568036885800L, 549685894064591284908235658839357390847445522332458370260385633L, 2108440654988370562048343461399852810852299068780806568036885800L, 903564225292763328142142737672378470519554721949504047040621938L, 1422210199200788483349447196472986571939187532913760546330866202L, 1446553245069254302636559515370833608116249509836384578091086589L, 690110490875978577594520719909097376417907156757045161010173205L, 147121471099487603100103942210642238821212368870164629959708554L, 336232159647806534360613641076076296745797957139999484229936900L, 2178652953394064208391485991934722803637529885993099963411779586L, 430787503921965999990868490508793325708090751274916911365051073L, 171464516967953422387216261108489274998274345792788661719928941L, 1754562323760198518814436382566831731180189869163760891256649495L, 1565451635211879587553926683701397673255604280893926036986421149L, 430787503921965999990868490508793325708090751274916911365051073L, 1705876232023266880240211744771137658826065915318512827736208721L, 879221179424297508855030418774531434342492745026880015280401551L, 2178652953394064208391485991934722803637529885993099963411779586L, 879221179424297508855030418774531434342492745026880015280401551L, 1989542264845745277130976293069288745712944297723265109141551240L, 1611320887749107414609956895338420629863773121183595400601094548L, 879221179424297508855030418774531434342492745026880015280401551L, 430787503921965999990868490508793325708090751274916911365051073L, 336232159647806534360613641076076296745797957139999484229936900L, 973776523698456974485285268207248463304785539161797442415515724L, 973776523698456974485285268207248463304785539161797442415515724L, 1327654854926629017719192347040269542976894738778843119195752029L]

plain = 'ISITDTU'
ind = 0
for i in range(0, len(cipher)-len(plain)):
    if cipher[i] == cipher[i+2] and cipher[i+3] == cipher[i+5]:
        ind = i
        break

ciphers = {}
for i in range(len(plain)):
    print plain[i], ord(plain[i]), cipher[ind+i]
    ciphers[ord(plain[i])] = cipher[ind+i]

m = 1110321085421447768275945874294757311370451552696385093861149689L
c = 1449370084268958114154753941529504723862204623391963277996853964L
n = 2315197515117055002182146598022231651703195899527687614857413551L

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

minv = modinv(m, n)
cinv = n-c

print(''.join([chr(((i+cinv)*minv)%n) for i in cipher]))

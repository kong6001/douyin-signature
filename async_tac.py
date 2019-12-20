# -*- coding: utf-8 -*-
import requests
import re
import random
import time
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9"
}
uids = '''100000212300
100000236218
100000483090
100000784836
100001267774
100001325665
100001349995
100001616353
100001634678
100002074315
100002150669
100002438027
100002809869
100002816183
100002983251
100003061278
100003461519
100003551928
100003894553
100003929258
100004231890
100004242682
100004367356
100004368351
100004433888
100004723484
100004829628
100005343111
100006624264
100006628464
100006860489
100007210076
100007361040
100007824735
100007858216
100008207412
100008374328
100008443171
100008452533
100008806250
100009502302
100010554232
100010804524
100011036154
100011148566
100011384852
100011615774
100011641222
100011671923
100012722766
100012747026
100012796868
100013050543
100013717955
100013722368
100013831411
100014179815
100014193912
100014298923
100014352130
100014467210
100014541602
100014677370
100014985476
100015175833
100015176647
100015201403
100015683704
100015908890
100015932068
100016075806
100016145369
100016364017
100016734245
100016740075
100016882002
100016899412
100017170931
10001718082
100017277893
100017341364
100017436657
100017558322
100017758072
100018035209
100018048932
100018598189
100018634573
100018810287
100018821494
100018865148
100018940218
100019018082
100019057352
100019208988
100019339001
100019372908
100019584523
100019680799
100019688253
100019758298
100020282651
100020349939
100020419662
100020592259
100020930602
100020965128
100021073661
100021111003
100021212449
100021233801
100021336457
100021402481
100021549801
100021621441
100021682121
100021743909
100021829987
100021849339
100021864850
100022094164
100022230020
100022422365
100022816874
100023018529
100023092597
100023147162
100023151093
100023176358
100023432292
100023576280
100023646072
100024267564
100024468141
100024551376
100024596129
100024702640
100024830150
100024858828
100025072984
100025167279
100025222581
100025331508
100025549191
100025598346
100025701930
100025729392
100026238065
100026339460
100026661988
100027089849
100027531937
100027690883
100027826527
100027975468
100028578419
100028661079
100028733106
100029662632
100029703820
100029727143
100029860499
100030761571
100031011042
100031131221
100031308693
100031319378
100031643189
100032077055
100032687990
100032844647
100032878655
100033065676
100033104818
100033274319
100033546642
100034246257
100034304687
100034410542
100034857595
100035025437
100035431598
100035480509
100035618041
100035796330
100035892348
100036237886
100036488175
100036571191
100037970260
10003948343
100039889405
100040114868
100040431513
100040899624
100040998330
100041135478
100041138509
100041188134
100041796947
100041859135
100041927289
100042124199
100042713221
100042735661
100042903247
100042922477
100043245988
100043427500
100043465314
100044118068
100044175480
100044186930
100044506224
100044924107
100045066577
100045503005
100046026050
100046204484
100046303335
100046327337
100046548509
100047406366
100047657811
100047718295
100047719339
100047731217
100048120340
100048688693
100048776437
100048986493
100049123952
100049149400
100049180620
100049294734
100049745189
100049784674
100049871080
100050298681
100050578650
100050603429
100050613145
100050618126
100050624047
100050640782
100050645670
100050648844
100050661772
100050674922
100050679487
100050685658
100050704274
100050731838
100050737335
100050765005
100050789606
100050789756
100050805011
100050805691
100050823415
100050830223
100050845473
100050855175
100050863236
100050873232
100050875824
100050876572
100050880756
100050894096
100050899426
100050910464
100050927353
100050934876
100050944214
100050945323
100050953150
100050962705
100050966811
100050966890
100050970245
100051007073
100051008686
100051009829
100051011167
100051014780
100051019744
100051021498
100051029125
100051037085
100051037504
100051054147
100051059497
100051059534
100051061343
100051070183
100051071909
100051082228
100051085138
100051092441
100051094152
100051096050
100051107053
100051138505
100051147055
100051157074
100051168881
100051176376
100051177260
100051182026
100051182873
100051190983
100051200631
100051205143
100051223151
100051227781
100051235818
100051239349
100051247002
100051262748
100051263487
100051281458
100051363834
100051370711
100051401058
100051408898
100051424260
100051434681
100051434791
100051449095
100051465911
100051473372
100051479409
100051480626
100051508898
100051523191
100051534373
100051552169
100051552725
100051566046
100051570354
100051573043
100051583017
100051585247
100051599304
100051602561
100051616401
100051640364
100051649920
100051651162
100051657450
100051690996
100051705990
100051718961
100051737636
100051741787
100051742347
100051744514
100051748993
100051768372
100051795147
100051795515
100051796770
100051813194
100051858654
100051872324
100051873673
100051889256
100051899322
100051909777
100051918064
100051925014
100051943326
100051962096
100051970053
100051973541
100051976885
100051980142
100051984980
100051985934
100051990171
100052004815
100052005352
100052006838
100052009948
100052015450
100052032949
100052046996
100052063622
100052073806
100052081955
100052105201
100052108029
100052111194
100052120530
100052150917
100052162223
100052181248
100052185964
100052201662
100052206744
100052210149
100052213914
100052214808
100052230307
100052241588
100052243024
100052245655
100052254383
100052264311
100052278535
100052280601
100052283021
100052288593
100052313711
100052326147
100052349680
100052390383
100052398355
100052439580
100052442170
100052445970
100052450853
100052464262
100052466480
100052471628
100052475978
100052476175
100052487141
100052499028
100052509616
100052513118
100052527481
100052531718
100052538085
100052539109
100052546517
100052572037
100052573595
100052594799
100052596684
100052608615
100052615946
100052626659
100052637408
100052637609
100052658628
100052660705
100052678137
100052691628
100052704512
100052706056
100052710586
100052711068
100052728380
100052733418
100052744975
100052747634
100052748095
100052750006
100052762942
100052764068
100052767364
100052777626
100052785546
100052798923
100052814778
100052814778
100052820791
100052822782
100052824267
100052847551
100052865128
100052866633
100052872130
100052886889
100052888937
100052898164
100052916918
100052942898
100052980064
100053004803
100053007667
100053008592
100053010924
100053026319
100053035408
100053049607
100053069696
100053082781
100053093492
100053105012
100053112090
100053115447
100053116744
100053132858
100053134897
100053136473
100053140260
100053148697
100053150225
100053150266
100053151444
100053166264
100053179520
100053211062
100053214011
100053215705
100053217814
100053239622
100053259081
100053260355
100053285204
100053287958
100053293704
100053331507
100053334442
100053347045
100053368968
100053385104
100053390177
100053407894
100053408093
100053428840
100053459826
100053476924
100053480912
100053494082
100053494685
100053495657
100053495828
100053501014
100053505512
100053505544
100053507619
100053556472
100053558188
100053575234
100053585143
100053585529
100053585980
100053587516
100053603655
100053606523
100053616074
100053617120
100053621302
100053634850
100053658693
100053662351
100053663544
100053666384
100053669354
100053674288
100053717790
100053723639
100053729455
100053732023
100053737596
100053768764
100053769253
100053789590
100053789947
100053795483
100053810669
100053810718
100053822736
100053826068
100053826150
100053832137
100053846346
100053853186
100053854637
100053862898
100053863623
100053865518
100053889580
100053898151
100053903994
100053912737
100053917992
100053919523
100053926279
100053932865
100053937207
100053940664
100053953501
100053955590
100053960546
100053965584
100053984501
100053994238
100054006363
100054010022
100054024212
100054024546
100054026274
100054027766
100054032760
100054056587
100054059555
100054059732
100054063473
100054078716
100054087653
100054091330
100054130636
100054142406
100054145834
100054157735
100054162335
100054165596
100054167354
100054170848
100054186268
100054194892
100054207471
100054211157
100054217921
100054225691
100054239479
100054246380
100054261039
100054262903
100054283974
100054292422
100054307915
100054333719
100054339290
100054342087
100054342865
100054349313
100054352838
100054352927
100054381334
100054390776
100054394439
100054402255
100054403322
100054477103
100054502340
100054504960
100054507626
100054520017
100054528438
100054546809
100054559146
100054560892
100054562624
100054573359
100054581603
100054589771
100054595296
100054597272
100054597708
100054630597
100054644490
100054648839
100054660047
100054664419
100054665511
100054674325
100054680590
100054695794
100054697155
100054701370
100054713425
100054755038
100054758288
100054780840
100054788266
100054795352
100054832882
100054845865
100054851102
100054885315
100054890657
100054909231
100054913456
100054914887
100054916793
100054922789
100054928656
100054942427
100054959998
100054961257
100054961260
100054965858
100054971010
100054997359
100055002489
100055045150
100055052535
100055065545
100055080589
100055083763
100055102313
100055125584
100055134398
100055137075
100055137362
100055141197
100055142551
100055148874
100055179076
100055182245
100055185103
100055185559
100055194869
100055199997
100055205852
100055222871
100055226560
100055230524
100055257101
100055258609
100055261582
100055280270
100055303849
100055307243
100055311134
100055326516
100055332713
100055332870
100055334105
100055334847
100055345182
100055361503
100055367776
100055376624
100055378870
100055399411
100055417369
100055418322
100055425016
100055428049
100055439199
100055445822
100055471769
100055487380
100055498073
100055519994
100055525339
100055527974
100055532935
100055543562
100055544030
100055548147
100055548602
100055569932
100055571081'''
uids = [i.strip() for i in uids.splitlines()]
def do_get_tac():
    while True:
        try:
            uid = random.choice(uids)
            response = requests.get('https://www.iesdouyin.com/share/user/{}'.format(uid),headers=headers,verify=False)
            tac = re.search(r"tac='([\s\S]*?)'</script>",response.text).group(1)
            data = {
                "tac":tac.split("|")[0],
            }
            requests.post('http://127.0.0.1:5000/tac/',data=data)
        except:
            pass
        finally:
            time.sleep(20)
if __name__ == '__main__':

        pass

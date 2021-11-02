#!/usr/bin/python
# -*- coding: utf-8 -*-
#  Copyright 2021 Hitomi Yanaka
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pandas as pd
import random

np_human_list = ["男性",
           "女性",
           "男の子",
           "女の子",
           "子供",
           "大人",
           "ホッケー選手",
           "テニス選手",
           "フットボール選手",
           "カップル",
           "ライダー",
           "スノーボーダー",
           "サーファー",
           "学生",
           "会社員",
           "若者",
           "老人"
           ]

np_nonhuman_list = ["犬",
                    "猫",
                    "猿",
                    "子犬",
                    "キツネ",
                    "リス",
                    "カエル",
                    "カンガルー"
                    ]

np_place_list = ["海辺",
                 "野原",
                 "公園",
                 "屋外",
                 "砂地",
                 "戸外",
                 "庭",
                 "森",
                 "動物園"
                 ]

iv_dic = {"立っている":"立たせている",
          "遊んでいる":"遊ばせている",
          "座っている":"座らせている",
          "走っている":"走らせている",
          "歩いている":"歩かせている",
          "歌を歌っている":"歌を歌わせている",
          "横たわっている":"横たわらせている",
          "泳いでいる":"泳がせている",
          "笑っている":"笑わせている",
          "歩き回っている":"歩き回らせている",
          # less than 30
          "眠っている":"眠らせた",
          "泣いている":"泣かせた"
          }

iv_human_list = ["しゃべっている",
                 "ピアノを弾いている",
                 "手品をしている",
                 "オートバイに乗っている",
                 "芝生を刈っている",
                 "ビールを飲んでいる",
                 "赤いジャケットを着ている",
                 "自転車を押して歩いている",
                 "写真を撮っている"
                 ]

tv_o_dic = {"見ている":"見られている", #見る
            "追いかけている":"追いかけられている", #追いかける
            "蹴った":"蹴られた", #蹴る
            "押した":"押された", #押す
            "見つめている":"見つめられている", #見つめる
            "たたいている":"たたかれている", #たたく, 叩く
            "指さしている":"指さされている", #指さす
            # less than 20
            "いじめている":"いじめられている", #いじめる
            # others
            "助けた":"助けられた", #助け出す
            "にらんでいる":"にらまれている", #にらむ
            "追い回した":"追い回された", #追い回す
            "追い払った":"追い払われた" #追い払う
            }

tv_ni_list = ["微笑んだ", #微笑む
              "話しかけている", #話しかける
              # less than 20
              "ぶつかった", #ぶつかる
              "跳びついた", #跳びつく
              "近づいた", #近づく
              "しがみついた", #しがみつく
              # JSNLI
              "寄りかかっている", #寄りかかる
              # others
              "合図を送った",
              "追いついた",
              "駆け寄った",
              "飛びかかった",
              "つかみかかった"
              ]
              
neg_list = ["のではない",
            "わけではない",
            "わけではありません"]

modal_list = ["かもしれない",
              "可能性がある",
              "らしい"]

reason_list = ["から、",
               "ので、",
               "ため、",
               "せいで、"]

concession_list = ["が、",
                   "けれども、",
                   "にもかかわらず、",
                   "のに、"]

factive_verb_list = ["ことがわかった",
                     "ことが知られている",
                     "のに気づいた",
                     "ことは確実だ"]

factive_adverb_list = ["間違いなく",
                       "確実に",
                       "明らかに"]

cond_adverb_list = ["もし"]

conditional_list = ["なら、",
                    "場合、",
                    "のでなければ、"]

cond_modal_list = ["にちがいない",
                   "だろう",
                   "はずだ"]

disjunction_list = ["か、",
                    "か、もしくは、",
                    "か、あるいは、"]

non_factive_verb_list = ["という噂がある",
                         "という疑いがある",
                         "と言われている",
                         "と信じられている"]

non_factive_adverb_list = ["ひょっとしたら",
                           "もしかしたら",
                           "おそらく"]


def develop(ws,ps,hs,label,htag,arg,stag,pairs,rate):
    allset = range(rate)
    testsplit = random.sample(allset, 5)
    for i in allset:
        pss, hss = ps, hs
        np1, np2, np3, np4 = random.sample(np_human_list, 4)
        tv_o_list = list(tv_o_dic.keys())
        iv_list = list(iv_dic.keys())
        tv1, tv2 = random.sample(tv_o_list, 2)
        iv_orig = random.choice(iv_list)
        iv_causative = iv_dic[iv_orig]
        tv_orig = random.choice(tv_o_list)
        tv_passive = tv_o_dic[tv_orig]
        if "np1" in ws:
            pss = pss.replace("np1", np1)
            hss = hss.replace("np1", np1)
        if "np2" in ws:
            pss = pss.replace("np2", np2)
            hss = hss.replace("np2", np2)
        if "np3" in ws:
            pss = pss.replace("np3", np3)
            hss = hss.replace("np3", np3)
        if "np4" in ws:
            pss = pss.replace("np4", np4)
            hss = hss.replace("np4", np4)
        if "np-nonhuman" in ws:
            np = random.choice(np_nonhuman_list)
            pss = pss.replace("np-nonhuman", np)
            hss = hss.replace("np-nonhuman", np)
        if "np-place" in ws:
            np = random.choice(np_place_list)
            pss = pss.replace("np-place", np)
            hss = hss.replace("np-place", np)
        if "iv-human" in ws:
            iv = random.choice(iv_human_list)
            pss = pss.replace("iv-human", iv)
            hss = hss.replace("iv-human", iv)
        if "tv-o1" in ws:
            pss = pss.replace("tv-o1", tv1)
            hss = hss.replace("tv-o1", tv1)
        if "tv-o2" in ws:
            pss = pss.replace("tv-o2", tv2)
            hss = hss.replace("tv-o2", tv2)
        if "tv-o" in ws:
            tv = random.choice(tv_o_list)
            pss = pss.replace("tv-o", tv)
            hss = hss.replace("tv-o", tv)
        if "tv-ni" in ws:
            tv = random.choice(tv_ni_list)
            pss = pss.replace("tv-ni", tv)
            hss = hss.replace("tv-ni", tv)
        if "iv-orig" in ws:
            pss = pss.replace("iv-orig", iv_orig)
            hss = hss.replace("iv-orig", iv_orig)
        if "iv-causative" in ws:
            pss = pss.replace("iv-causative", iv_causative)
            hss = hss.replace("iv-causative", iv_causative)
        if "tv-orig" in ws:
            pss = pss.replace("tv-orig", tv_orig)
            hss = hss.replace("tv-orig", tv_orig)
        if "tv-passive" in ws:
            pss = pss.replace("tv-passive", tv_passive)
            hss = hss.replace("tv-passive", tv_passive)
        if "neg" in ws:
            neg = random.choice(neg_list)
            pss = pss.replace("neg", neg)
            hss = hss.replace("neg", neg)
        if "cond-modal" in ws:
            cond_modal = random.choice(cond_modal_list)
            pss = pss.replace("cond-modal", cond_modal)
            hss = hss.replace("cond-modal", cond_modal)
        if "modal" in ws:
            modal = random.choice(modal_list)
            pss = pss.replace("modal", modal)
            hss = hss.replace("modal", modal)
        if "reason" in ws:
            reason = random.choice(reason_list)
            pss = pss.replace("reason", reason)
            hss = hss.replace("reason", reason)
        if "concession" in ws:
            concession = random.choice(concession_list)
            pss = pss.replace("concession", concession)
            hss = hss.replace("concession", concession)
        if "non-factive-verb" in ws:
            non_factive_verb = random.choice(non_factive_verb_list)
            pss = pss.replace("non-factive-verb", non_factive_verb)
            hss = hss.replace("non-factive-verb", non_factive_verb)
        if "non-factive-adverb" in ws:
            non_factive_adverb = random.choice(non_factive_adverb_list)
            pss = pss.replace("non-factive-adverb", non_factive_adverb)
            hss = hss.replace("non-factive-adverb", non_factive_adverb)
        if "cond-adverb" in ws:
            cond_adverb = random.choice(cond_adverb_list)
            pss = pss.replace("cond-adverb", cond_adverb)
            hss = hss.replace("cond-adverb", cond_adverb)
        if "factive-adverb" in ws:
            factive_adverb = random.choice(factive_adverb_list)
            pss = pss.replace("factive-adverb", factive_adverb)
            hss = hss.replace("factive-adverb", factive_adverb)
        if "factive-verb" in ws:
            factive_verb = random.choice(factive_verb_list)
            pss = pss.replace("factive-verb", factive_verb)
            hss = hss.replace("factive-verb", factive_verb)
        if "conditional" in ws:
            conditional = random.choice(conditional_list)
            pss = pss.replace("conditional", conditional)
            hss = hss.replace("conditional", conditional)
        if "disjunction" in ws:
            disjunction = random.choice(disjunction_list)
            pss = pss.replace("disjunction", disjunction)
            hss = hss.replace("disjunction", disjunction)
        if "iv" in ws:
            iv = random.choice(iv_list)
            pss = pss.replace("iv", iv)
            hss = hss.replace("iv", iv)
        if i in testsplit:
            split = "test"
        else:
            split = "train"
        pairs.append([pss.replace(" ",""), hss.replace(" ",""), label, htag, arg, stag, split])
    return pairs

def main():
    pairs = []
    with open("./data/JaNLI_template.csv") as f:
        finput = f.readlines()
    for line in finput:
        ws = []
        ps, hs, label, htag, arg, stags= line.strip().split(",")[0:6]
        if ps == "sentence1":
            continue
        ws = ps.split(" ")
        ws.extend(hs.split(" "))
        stag = stags.split(';')[0] # use the first semtag only
        # print(ps,hs,l,ws)
        pairs = develop(ws,ps,hs,label,htag,arg,stag,pairs,100)
    df = pd.DataFrame(pairs, columns=["sentence_A_Ja", "sentence_B_Ja", "entailment_label_Ja", "heuristics", "number_of_NPs", "semtag", "split"])
    df.to_csv("janli.tsv", sep="\t", index=True)

if __name__ == '__main__':
    main()

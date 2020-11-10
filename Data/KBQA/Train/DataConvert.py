#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 3:15 下午
# @Author  : SPC
# @FileName: DataConvert.py
# @Software: PyCharm
# @Des     ：generate json file for KBQA train data

import json

fe = open("train_entities.txt","r",encoding="UTF-8")
elines = fe.readlines()
fm = open("train_mentions.txt","r",encoding="UTF-8")
mlines = fm.readlines()
fp = open("train_predicates.txt","r",encoding="UTF-8")
plines = fp.readlines()
fq = open("train_questions.txt","r",encoding="UTF-8")
qlines = fq.readlines()

# tain_candidate_predicates.txt这一文件存放的是gold_ent对应的全部predicate
fc = open("train_candidate_predicates.txt","r",encoding="UTF-8")
clines = fc.readlines()


train_data = []

for idx,qline in enumerate(qlines):
    print(idx)
    data = {}
    question = qline.strip()
    data["qu"] = question
    mls = mlines[idx].strip().split("|||")
    data["sub_men"] = mls
    els = elines[idx].strip().split("|||")
    data["gold_ent"] = els
    pls = plines[idx].strip().split("|||")
    data["gold_pre"] = list(set(pls))
    cls = clines[idx].strip().split("|||")
    if cls:
        data["pres"] = list(set(cls))
    else:
        data["pres"] = list(set(pls))
    train_data.append(data)

with open("train_data.json","w",encoding="UTF-8") as f:
    json.dump(train_data,f,ensure_ascii=False,indent=4)







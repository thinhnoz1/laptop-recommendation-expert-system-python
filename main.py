__author__ = 'thinhnoz1'
import json
from sys import int_info

def import_rules():
    rule_file = './rules.json'
    with open(rule_file, 'r') as f:
        rules = json.load(f)
        return rules

def import_facts():
    fact_file = './facts.json'
    with open(fact_file, 'r') as f:
        facts = json.load(f)
        return facts

def search(list, keyword):
    for item in list:
        if (item["IF"] == keyword):
            return item["THEN"], True
    return [], False

def isElementInList(element, list):
    if (element in list or "any" in list):
        return True
    else:
        return False

def recommend(rules, facts, purpose, budget):
    current_rule, success = search(rules, purpose)
    result = []

    for i in range(len(facts)):
        if (facts[i]["ram"] >= current_rule["ram"] and 
            facts[i]["hd_size"] >= current_rule["hd_size"] and 
            facts[i]["screen_size"] >= current_rule["screen_size"] and 
            facts[i]["clock_speed"] >= current_rule["clock_speed"] and
            facts[i]["graphic_card_size"] >= current_rule["graphic_card_size"] and 
            (facts[i]["processor_brand"] == current_rule["processor_brand"] or current_rule["processor_brand"] == "any") and 
            facts[i]["weight"] <= current_rule["weight"] and
            facts[i]["price"] <= budget):

            if (purpose == "gaming"):
                if (isElementInList(facts[i]["graphic_card_brand"], current_rule["graphic_card_brand"])):
                    result.append(i)
            else:
                result.append(i)
        
    return result

def choose_one_best_option (index_array, facts):
    highest_price = 0
    highest_idx =0
    for idx in index_array:
        if (facts[idx]["price"] > highest_price):
            highest_price = facts[idx]["price"]
            highest_idx = idx

    return highest_idx
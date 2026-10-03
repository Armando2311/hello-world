import json,re,collections
d=json.load(open("reviews.json"))
themes={
 "price/subscription":r"subscri|pric|expensive|paywall|\$|pay |paid|money|cost|free trial|charg|refund",
 "data loss/sync/backup":r"lost|lose|deleted|sync|backup|back up|transfer|export|gone|wiped",
 "bugs/crash":r"crash|bug|freez|glitch|won't load|doesn.t work|not working|broken|slow",
 "missing tracking/insight":r"track|log|diary|pattern|correlat|trigger|insight|report|graph|chart",
 "food database gaps":r"database|not listed|can.t find|missing food|search|brand|barcode|scan",
 "reintro/plan guidance":r"reintro|challenge|elimination|phase|plan|meal plan|guide|stack",
 "serving size/data accuracy":r"serving|portion|accura|wrong|incorrect|inconsistent|traffic light|green|red",
 "UI/usability":r"confus|clunky|hard to|difficult|interface|ui|navigate|tedious|too many (taps|steps)",
 "doctor/export":r"doctor|gastro|dietitian|pdf|print|share",
 "ads":r"\bads?\b|advert",
}
neg={a:[r for r in v["reviews"] if r["r"]<=3] for a,v in d.items()}
tot=collections.Counter()
for a,rs in neg.items():
    c=collections.Counter()
    for r in rs:
        txt=(r["t"]+" "+r["b"]).lower()
        for k,p in themes.items():
            if re.search(p,txt): c[k]+=1; tot[k]+=1
    print(f"\n## {a} (n={len(rs)} 1-3★)"); 
    for k,v in c.most_common(): print(f"  {k}: {v} ({100*v//max(1,len(rs))}%)")
n=sum(len(v) for v in neg.values())
print(f"\n## ALL (n={n})")
for k,v in tot.most_common(): print(f"  {k}: {v} ({100*v//n}%)")

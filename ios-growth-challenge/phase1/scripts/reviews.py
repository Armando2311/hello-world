import json, sys, urllib.request, urllib.parse, collections
def find(term):
    u="https://itunes.apple.com/search?"+urllib.parse.urlencode({"term":term,"entity":"software","country":"us","limit":1})
    return json.load(urllib.request.urlopen(u,timeout=30))["results"][0]
out={}
for term in sys.argv[1:]:
    a=find(term); aid=a["trackId"]; revs=[]
    for p in range(1,11):
        u=f"https://itunes.apple.com/us/rss/customerreviews/page={p}/id={aid}/sortby=mostrecent/json"
        try: d=json.load(urllib.request.urlopen(u,timeout=30))
        except Exception: break
        es=d.get("feed",{}).get("entry",[])
        if isinstance(es,dict): es=[es]
        es=[e for e in es if "im:rating" in e]
        if not es: break
        for e in es: revs.append({"r":int(e["im:rating"]["label"]),"t":e["title"]["label"],"b":e["content"]["label"],"v":e.get("im:version",{}).get("label","")})
    out[a["trackName"]]={"id":aid,"reviews":revs}
    c=collections.Counter(r["r"] for r in revs)
    print(a["trackName"], aid, len(revs), dict(sorted(c.items())))
json.dump(out,open("reviews.json","w"))

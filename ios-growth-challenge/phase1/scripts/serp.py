import json, sys, urllib.parse, urllib.request
terms = sys.argv[1:]
for t in terms:
    url = "https://itunes.apple.com/search?" + urllib.parse.urlencode({"term": t, "entity": "software", "country": "us", "limit": 10})
    try:
        d = json.load(urllib.request.urlopen(url, timeout=30))
    except Exception as e:
        print(t, "ERR", e); continue
    rs = d["results"]
    print(f"\n=== {t} === ({len(rs)} results)")
    for r in rs:
        print(f"  {r.get('userRatingCount',0):>8} ratings  {r.get('averageUserRating',0):.1f}*  ${r.get('price',0):<5} upd {r.get('currentVersionReleaseDate','')[:10]}  {r['trackName'][:60]}  [{r.get('primaryGenreName')}]")

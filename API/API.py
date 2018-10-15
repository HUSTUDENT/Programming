import requests
import xmltodict

ReisInformatieLijst = []
station = "UTRECHT"
auth_details = ("loenaherst@hotmail.com", "Sunsq1YjltTbYDS3VKx-0dyHGBdjIMDhf-qxUuDwcj_No6VMZMWhPw")
api_url = "http://webservices.ns.nl/ns-api-avt?station=" + station
response = requests.get(api_url, auth = auth_details)
tijden_xml = xmltodict.parse(response.text)

for tijden in tijden_xml["ActueleVertrekTijden"]["VertrekkendeTrein"]:
    RitNummer = tijden["RitNummer"]
    VertrekTijd = tijden["VertrekTijd"]
    EindBestemming = tijden["EindBestemming"]
    TreinSoort = tijden["TreinSoort"]
    Vervoerder = tijden["Vervoerder"]
    VertrekSpoor = tijden["VertrekSpoor"]["#text"]
    VertrekSpoorWijziging = tijden["VertrekSpoor"]["@wijziging"]
    try:
        RouteTekst = tijden["RouteTekst"]
    except:
        RouteTekst = ""
    try:
        ReisTip = tijden["ReisTip"]
    except:
        ReisTip = ""
    try:
        VertrekVertragingTekst = tijden["VertrekVertragingTekst"]
    except:
        VertrekVertragingTekst = ""
    ReisInformatie = [RitNummer, VertrekTijd, VertrekVertragingTekst, EindBestemming, TreinSoort, RouteTekst, Vervoerder, VertrekSpoor, VertrekSpoorWijziging, ReisTip]
    ReisInformatieLijst.append(ReisInformatie)
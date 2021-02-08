#!/usr/bin/env python3

""" Generates random name """

from secrets import choice as secrets_choice

FOODS = [
    'anaar-e', 'azgil-e', 'albaloo-ye', 'aloo-ye', 'ananas-e',
    'anjir-e', 'angoor-e', 'avokaado-ye', 'badoom-e', 'baalang-e',
    'baloot-e', 'beh-e', 'porteghal-e', 'peste-ye', 'toranj-e',
    'tamr_hendi-ye', 'anbe-ye', 'tameshk-e', 'toot_farangi-ye',
    'toot-e', 'kharboze-ye', 'khormaloo-ye', 'khorma-ye', 'khiyar-e',
    'zoghal_akhte-ye', 'zalzalak-e', 'zard_aloo-ye', 'zereshk-e', 'zeytoon-e',
    'senjed-e', 'sib-e', 'shaatoot-e', 'shaftaaloo-ye', 'shalil-e', 'taalebi-e',
    'fandogh-e', 'gheisi-e', 'komboze-ye', 'kivi-ye', 'gerdoo-ye',
    'grip_froot-e', 'golabi-ye', 'alooche-ye', 'gilas-e', 'limoo_torsh-e',
    'limoo_shirin-e', 'nargil-e', 'movz-e', 'narengi-e', 'holoo-ye', 'hendoone-ye',
    'karafs-e', 'shivid-e', 'torob-e', 'piyaz-e', 'sir-e', 'havij-e',
    'nokhod-e', 'lobooya_sefid-e', 'loobiya_chiti-ye', 'ghoore-ye',
    'kalam-e', 'kadoo_halavee-ye', 'delester-e', 'nooshabe-ye',
    'panir-e', 'tah_chin-e', 'ton_maahi-ye', 'faloode-ye', 'shir_berenj-e'
]

ADJS = [
    'araasteh', 'ashofteh', 'asoodeh', 'aloodeh', 'afrookhteh', 'afsordeh',
    'baaz_maandeh', 'bargozideh', 'paloodeh', 'pokhteh', 'parvardeh',
    'parishan', 'parideh', 'pasandideh', 'pichideh', 'pishrafteh', 'bad_badan',
    'tafteh', 'taftideh', 'chasbideh', 'khamideh', 'kharamideh', 'chegher',
    'khalideh', 'khoshkideh', 'khaste', 'dars_khaandeh', 'darideh',
    'dast_amooz', 'deldadeh', 'delpazir', 'domborideh', 'rahideh', 'ablah',
    'rang_parideh', 'resideh', 'zereh_push', 'zabanzad', 'zir_afkan',
    'zhoolideh', 'salkhodeh', 'sar_afkandeh', 'sar_sepordeh', 'sar_shekasteh',
    'sar_gashteh', 'sookhteh', 'sharab_zadeh', 'shoorideh', 'shifteh',
    'farrokhzad', 'farsoodeh', 'farifteh', 'foroo_heshteh', 'kar_azmoodeh',
    'kar_amad', 'gosasteh', 'ghoshadeh', 'gozideh', 'gomashteh',
    'legam_gosikhteh', 'miyaneh_ro', 'modabber', 'naadaan', 'sharlatan',
    'naz_parvardeh', 'vabasteh', 'varafteh', 'varasteh', 'varparideh',
    'varshekasteh', 'haraasaan', 'bi_namoos', 'khak_barsar', 'oghde_ee',
    'kheng', 'dana', 'khoshhal', 'kheng', 'ghozmit', 'afsoreh_sima',
    'boland_parvaz', 'delsard', 'kaftar_baaz', 'chabok', 'khafan',
    'daneshmand', 'data_scientist'
]

def run():
    """ The main function """
    adjs = ADJS * 10
    foods = ADJS * 10
    name, adjective = secrets_choice(foods), secrets_choice(adjs)

    print(f"{name}-{adjective}")

if __name__ == '__main__':
    run()

#!/usr/bin/env python
import random


fruits = [
    'anaar-e', 'azgil-e', 'albaloo-ye', 'aloo-ye', 'ananas-e',
    'anjir-e', 'angoor-e', 'avokaado-ye', 'badoom-e', 'baalang-e',
    'baloot-e', 'beh-e', 'porteghal-e', 'peste-ye', 'toranj-e',
    'tamr_hendi-ye', 'anbe-ye', 'tameshk-e', 'toot_farangi-ye',
    'toot-e', 'kharboze-ye', 'khormaloo-ye', 'khorma-ye', 'khiyar-e',
    'zoghal_akhte-ye', 'zalzalak-e', 'zard_aloo-ye', 'zereshk-e', 'zeytoon-e',
    'senjed-e', 'sib-e', 'shaatoot-e', 'shaftaaloo-ye', 'shalil-e', 'taalebi-e',
    'fandogh-e', 'gheisi-e', 'komboze-ye', 'kivi-ye', 'gerdoo-ye',
    'grip_froot-e', 'golabi-ye', 'alooche-ye', 'gilas-e', 'limoo_torsh-e',
    'limoo_shirin-e', 'nargil-e', 'movz-e', 'narengi-e', 'holoo-ye', 'hendoone-ye'
]



adjs = [
    'araasteh', 'ashofteh', 'asoodeh', 'aloodeh', 'afrookhteh', 'afsordeh',
    'baaz_maandeh', 'bargozideh', 'paloodeh', 'pokhteh', 'parvardeh',
    'parishan', 'parideh', 'pasandideh', 'pichideh', 'pishrafteh',
    'tafteh', 'taftideh', 'chasbideh', 'khamideh', 'kharamideh',
    'khalideh', 'khoshkideh', 'khaste', 'dars_khaandeh', 'darideh',
    'dast_amooz', 'deldadeh', 'delpazir', 'domborideh', 'rahideh',
    'rang_parideh', 'resideh', 'zereh_push', 'zabanzad', 'zir_afkan',
    'zhoolideh', 'salkhodeh', 'sar_afkandeh', 'sar_sepordeh', 'sar_shekasteh',
    'sar_gashteh', 'sookhteh', 'sharab_zadeh', 'shoorideh', 'shifteh',
    'farrokhzad', 'farsoodeh', 'farifteh', 'foroo_heshteh', 'kar_azmoodeh',
    'kar_amad', 'gosasteh', 'ghoshadeh', 'gozideh', 'gomashteh',
    'legam_gosikhteh', 'miyaneh_ro', 'modabber', 'naadaan',
    'naz_parvardeh', 'vabasteh', 'varafteh', 'varasteh', 'varparideh',
    'varshekasteh', 'haraasaan', 'bi_namoos', 'khak_barsar', 'oghde_ee',
    'kheng', 'dana', 'khoshhal', 'kheng', 'ghozmit'
]


print(f"{random.choice(fruits)}-{random.choice(adjs)}")


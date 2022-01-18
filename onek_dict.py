import time

from funcs import *

func_dict = {
    0: func0,
    1: func1,
    2: func2,
    3: func3,
    4: func4,
    5: func5,
    6: func6,
    7: func7,
    8: func8,
    9: func9,
    10: func10,
    11: func11,
    12: func12,
    13: func13,
    14: func14,
    15: func15,
    16: func16,
    17: func17,
    18: func18,
    19: func19,
    20: func20,
    21: func21,
    22: func22,
    23: func23,
    24: func24,
    25: func25,
    26: func26,
    27: func27,
    28: func28,
    29: func29,
    30: func30,
    31: func31,
    32: func32,
    33: func33,
    34: func34,
    35: func35,
    36: func36,
    37: func37,
    38: func38,
    39: func39,
    40: func40,
    41: func41,
    42: func42,
    43: func43,
    44: func44,
    45: func45,
    46: func46,
    47: func47,
    48: func48,
    49: func49,
    50: func50,
    51: func51,
    52: func52,
    53: func53,
    54: func54,
    55: func55,
    56: func56,
    57: func57,
    58: func58,
    59: func59,
    60: func60,
    61: func61,
    62: func62,
    63: func63,
    64: func64,
    65: func65,
    66: func66,
    67: func67,
    68: func68,
    69: func69,
    70: func70,
    71: func71,
    72: func72,
    73: func73,
    74: func74,
    75: func75,
    76: func76,
    77: func77,
    78: func78,
    79: func79,
    80: func80,
    81: func81,
    82: func82,
    83: func83,
    84: func84,
    85: func85,
    86: func86,
    87: func87,
    88: func88,
    89: func89,
    90: func90,
    91: func91,
    92: func92,
    93: func93,
    94: func94,
    95: func95,
    96: func96,
    97: func97,
    98: func98,
    99: func99,
    100: func100,
    101: func101,
    102: func102,
    103: func103,
    104: func104,
    105: func105,
    106: func106,
    107: func107,
    108: func108,
    109: func109,
    110: func110,
    111: func111,
    112: func112,
    113: func113,
    114: func114,
    115: func115,
    116: func116,
    117: func117,
    118: func118,
    119: func119,
    120: func120,
    121: func121,
    122: func122,
    123: func123,
    124: func124,
    125: func125,
    126: func126,
    127: func127,
    128: func128,
    129: func129,
    130: func130,
    131: func131,
    132: func132,
    133: func133,
    134: func134,
    135: func135,
    136: func136,
    137: func137,
    138: func138,
    139: func139,
    140: func140,
    141: func141,
    142: func142,
    143: func143,
    144: func144,
    145: func145,
    146: func146,
    147: func147,
    148: func148,
    149: func149,
    150: func150,
    151: func151,
    152: func152,
    153: func153,
    154: func154,
    155: func155,
    156: func156,
    157: func157,
    158: func158,
    159: func159,
    160: func160,
    161: func161,
    162: func162,
    163: func163,
    164: func164,
    165: func165,
    166: func166,
    167: func167,
    168: func168,
    169: func169,
    170: func170,
    171: func171,
    172: func172,
    173: func173,
    174: func174,
    175: func175,
    176: func176,
    177: func177,
    178: func178,
    179: func179,
    180: func180,
    181: func181,
    182: func182,
    183: func183,
    184: func184,
    185: func185,
    186: func186,
    187: func187,
    188: func188,
    189: func189,
    190: func190,
    191: func191,
    192: func192,
    193: func193,
    194: func194,
    195: func195,
    196: func196,
    197: func197,
    198: func198,
    199: func199,
    200: func200,
    201: func201,
    202: func202,
    203: func203,
    204: func204,
    205: func205,
    206: func206,
    207: func207,
    208: func208,
    209: func209,
    210: func210,
    211: func211,
    212: func212,
    213: func213,
    214: func214,
    215: func215,
    216: func216,
    217: func217,
    218: func218,
    219: func219,
    220: func220,
    221: func221,
    222: func222,
    223: func223,
    224: func224,
    225: func225,
    226: func226,
    227: func227,
    228: func228,
    229: func229,
    230: func230,
    231: func231,
    232: func232,
    233: func233,
    234: func234,
    235: func235,
    236: func236,
    237: func237,
    238: func238,
    239: func239,
    240: func240,
    241: func241,
    242: func242,
    243: func243,
    244: func244,
    245: func245,
    246: func246,
    247: func247,
    248: func248,
    249: func249,
    250: func250,
    251: func251,
    252: func252,
    253: func253,
    254: func254,
    255: func255,
    256: func256,
    257: func257,
    258: func258,
    259: func259,
    260: func260,
    261: func261,
    262: func262,
    263: func263,
    264: func264,
    265: func265,
    266: func266,
    267: func267,
    268: func268,
    269: func269,
    270: func270,
    271: func271,
    272: func272,
    273: func273,
    274: func274,
    275: func275,
    276: func276,
    277: func277,
    278: func278,
    279: func279,
    280: func280,
    281: func281,
    282: func282,
    283: func283,
    284: func284,
    285: func285,
    286: func286,
    287: func287,
    288: func288,
    289: func289,
    290: func290,
    291: func291,
    292: func292,
    293: func293,
    294: func294,
    295: func295,
    296: func296,
    297: func297,
    298: func298,
    299: func299,
    300: func300,
    301: func301,
    302: func302,
    303: func303,
    304: func304,
    305: func305,
    306: func306,
    307: func307,
    308: func308,
    309: func309,
    310: func310,
    311: func311,
    312: func312,
    313: func313,
    314: func314,
    315: func315,
    316: func316,
    317: func317,
    318: func318,
    319: func319,
    320: func320,
    321: func321,
    322: func322,
    323: func323,
    324: func324,
    325: func325,
    326: func326,
    327: func327,
    328: func328,
    329: func329,
    330: func330,
    331: func331,
    332: func332,
    333: func333,
    334: func334,
    335: func335,
    336: func336,
    337: func337,
    338: func338,
    339: func339,
    340: func340,
    341: func341,
    342: func342,
    343: func343,
    344: func344,
    345: func345,
    346: func346,
    347: func347,
    348: func348,
    349: func349,
    350: func350,
    351: func351,
    352: func352,
    353: func353,
    354: func354,
    355: func355,
    356: func356,
    357: func357,
    358: func358,
    359: func359,
    360: func360,
    361: func361,
    362: func362,
    363: func363,
    364: func364,
    365: func365,
    366: func366,
    367: func367,
    368: func368,
    369: func369,
    370: func370,
    371: func371,
    372: func372,
    373: func373,
    374: func374,
    375: func375,
    376: func376,
    377: func377,
    378: func378,
    379: func379,
    380: func380,
    381: func381,
    382: func382,
    383: func383,
    384: func384,
    385: func385,
    386: func386,
    387: func387,
    388: func388,
    389: func389,
    390: func390,
    391: func391,
    392: func392,
    393: func393,
    394: func394,
    395: func395,
    396: func396,
    397: func397,
    398: func398,
    399: func399,
    400: func400,
    401: func401,
    402: func402,
    403: func403,
    404: func404,
    405: func405,
    406: func406,
    407: func407,
    408: func408,
    409: func409,
    410: func410,
    411: func411,
    412: func412,
    413: func413,
    414: func414,
    415: func415,
    416: func416,
    417: func417,
    418: func418,
    419: func419,
    420: func420,
    421: func421,
    422: func422,
    423: func423,
    424: func424,
    425: func425,
    426: func426,
    427: func427,
    428: func428,
    429: func429,
    430: func430,
    431: func431,
    432: func432,
    433: func433,
    434: func434,
    435: func435,
    436: func436,
    437: func437,
    438: func438,
    439: func439,
    440: func440,
    441: func441,
    442: func442,
    443: func443,
    444: func444,
    445: func445,
    446: func446,
    447: func447,
    448: func448,
    449: func449,
    450: func450,
    451: func451,
    452: func452,
    453: func453,
    454: func454,
    455: func455,
    456: func456,
    457: func457,
    458: func458,
    459: func459,
    460: func460,
    461: func461,
    462: func462,
    463: func463,
    464: func464,
    465: func465,
    466: func466,
    467: func467,
    468: func468,
    469: func469,
    470: func470,
    471: func471,
    472: func472,
    473: func473,
    474: func474,
    475: func475,
    476: func476,
    477: func477,
    478: func478,
    479: func479,
    480: func480,
    481: func481,
    482: func482,
    483: func483,
    484: func484,
    485: func485,
    486: func486,
    487: func487,
    488: func488,
    489: func489,
    490: func490,
    491: func491,
    492: func492,
    493: func493,
    494: func494,
    495: func495,
    496: func496,
    497: func497,
    498: func498,
    499: func499,
    500: func500,
    501: func501,
    502: func502,
    503: func503,
    504: func504,
    505: func505,
    506: func506,
    507: func507,
    508: func508,
    509: func509,
    510: func510,
    511: func511,
    512: func512,
    513: func513,
    514: func514,
    515: func515,
    516: func516,
    517: func517,
    518: func518,
    519: func519,
    520: func520,
    521: func521,
    522: func522,
    523: func523,
    524: func524,
    525: func525,
    526: func526,
    527: func527,
    528: func528,
    529: func529,
    530: func530,
    531: func531,
    532: func532,
    533: func533,
    534: func534,
    535: func535,
    536: func536,
    537: func537,
    538: func538,
    539: func539,
    540: func540,
    541: func541,
    542: func542,
    543: func543,
    544: func544,
    545: func545,
    546: func546,
    547: func547,
    548: func548,
    549: func549,
    550: func550,
    551: func551,
    552: func552,
    553: func553,
    554: func554,
    555: func555,
    556: func556,
    557: func557,
    558: func558,
    559: func559,
    560: func560,
    561: func561,
    562: func562,
    563: func563,
    564: func564,
    565: func565,
    566: func566,
    567: func567,
    568: func568,
    569: func569,
    570: func570,
    571: func571,
    572: func572,
    573: func573,
    574: func574,
    575: func575,
    576: func576,
    577: func577,
    578: func578,
    579: func579,
    580: func580,
    581: func581,
    582: func582,
    583: func583,
    584: func584,
    585: func585,
    586: func586,
    587: func587,
    588: func588,
    589: func589,
    590: func590,
    591: func591,
    592: func592,
    593: func593,
    594: func594,
    595: func595,
    596: func596,
    597: func597,
    598: func598,
    599: func599,
    600: func600,
    601: func601,
    602: func602,
    603: func603,
    604: func604,
    605: func605,
    606: func606,
    607: func607,
    608: func608,
    609: func609,
    610: func610,
    611: func611,
    612: func612,
    613: func613,
    614: func614,
    615: func615,
    616: func616,
    617: func617,
    618: func618,
    619: func619,
    620: func620,
    621: func621,
    622: func622,
    623: func623,
    624: func624,
    625: func625,
    626: func626,
    627: func627,
    628: func628,
    629: func629,
    630: func630,
    631: func631,
    632: func632,
    633: func633,
    634: func634,
    635: func635,
    636: func636,
    637: func637,
    638: func638,
    639: func639,
    640: func640,
    641: func641,
    642: func642,
    643: func643,
    644: func644,
    645: func645,
    646: func646,
    647: func647,
    648: func648,
    649: func649,
    650: func650,
    651: func651,
    652: func652,
    653: func653,
    654: func654,
    655: func655,
    656: func656,
    657: func657,
    658: func658,
    659: func659,
    660: func660,
    661: func661,
    662: func662,
    663: func663,
    664: func664,
    665: func665,
    666: func666,
    667: func667,
    668: func668,
    669: func669,
    670: func670,
    671: func671,
    672: func672,
    673: func673,
    674: func674,
    675: func675,
    676: func676,
    677: func677,
    678: func678,
    679: func679,
    680: func680,
    681: func681,
    682: func682,
    683: func683,
    684: func684,
    685: func685,
    686: func686,
    687: func687,
    688: func688,
    689: func689,
    690: func690,
    691: func691,
    692: func692,
    693: func693,
    694: func694,
    695: func695,
    696: func696,
    697: func697,
    698: func698,
    699: func699,
    700: func700,
    701: func701,
    702: func702,
    703: func703,
    704: func704,
    705: func705,
    706: func706,
    707: func707,
    708: func708,
    709: func709,
    710: func710,
    711: func711,
    712: func712,
    713: func713,
    714: func714,
    715: func715,
    716: func716,
    717: func717,
    718: func718,
    719: func719,
    720: func720,
    721: func721,
    722: func722,
    723: func723,
    724: func724,
    725: func725,
    726: func726,
    727: func727,
    728: func728,
    729: func729,
    730: func730,
    731: func731,
    732: func732,
    733: func733,
    734: func734,
    735: func735,
    736: func736,
    737: func737,
    738: func738,
    739: func739,
    740: func740,
    741: func741,
    742: func742,
    743: func743,
    744: func744,
    745: func745,
    746: func746,
    747: func747,
    748: func748,
    749: func749,
    750: func750,
    751: func751,
    752: func752,
    753: func753,
    754: func754,
    755: func755,
    756: func756,
    757: func757,
    758: func758,
    759: func759,
    760: func760,
    761: func761,
    762: func762,
    763: func763,
    764: func764,
    765: func765,
    766: func766,
    767: func767,
    768: func768,
    769: func769,
    770: func770,
    771: func771,
    772: func772,
    773: func773,
    774: func774,
    775: func775,
    776: func776,
    777: func777,
    778: func778,
    779: func779,
    780: func780,
    781: func781,
    782: func782,
    783: func783,
    784: func784,
    785: func785,
    786: func786,
    787: func787,
    788: func788,
    789: func789,
    790: func790,
    791: func791,
    792: func792,
    793: func793,
    794: func794,
    795: func795,
    796: func796,
    797: func797,
    798: func798,
    799: func799,
    800: func800,
    801: func801,
    802: func802,
    803: func803,
    804: func804,
    805: func805,
    806: func806,
    807: func807,
    808: func808,
    809: func809,
    810: func810,
    811: func811,
    812: func812,
    813: func813,
    814: func814,
    815: func815,
    816: func816,
    817: func817,
    818: func818,
    819: func819,
    820: func820,
    821: func821,
    822: func822,
    823: func823,
    824: func824,
    825: func825,
    826: func826,
    827: func827,
    828: func828,
    829: func829,
    830: func830,
    831: func831,
    832: func832,
    833: func833,
    834: func834,
    835: func835,
    836: func836,
    837: func837,
    838: func838,
    839: func839,
    840: func840,
    841: func841,
    842: func842,
    843: func843,
    844: func844,
    845: func845,
    846: func846,
    847: func847,
    848: func848,
    849: func849,
    850: func850,
    851: func851,
    852: func852,
    853: func853,
    854: func854,
    855: func855,
    856: func856,
    857: func857,
    858: func858,
    859: func859,
    860: func860,
    861: func861,
    862: func862,
    863: func863,
    864: func864,
    865: func865,
    866: func866,
    867: func867,
    868: func868,
    869: func869,
    870: func870,
    871: func871,
    872: func872,
    873: func873,
    874: func874,
    875: func875,
    876: func876,
    877: func877,
    878: func878,
    879: func879,
    880: func880,
    881: func881,
    882: func882,
    883: func883,
    884: func884,
    885: func885,
    886: func886,
    887: func887,
    888: func888,
    889: func889,
    890: func890,
    891: func891,
    892: func892,
    893: func893,
    894: func894,
    895: func895,
    896: func896,
    897: func897,
    898: func898,
    899: func899,
    900: func900,
    901: func901,
    902: func902,
    903: func903,
    904: func904,
    905: func905,
    906: func906,
    907: func907,
    908: func908,
    909: func909,
    910: func910,
    911: func911,
    912: func912,
    913: func913,
    914: func914,
    915: func915,
    916: func916,
    917: func917,
    918: func918,
    919: func919,
    920: func920,
    921: func921,
    922: func922,
    923: func923,
    924: func924,
    925: func925,
    926: func926,
    927: func927,
    928: func928,
    929: func929,
    930: func930,
    931: func931,
    932: func932,
    933: func933,
    934: func934,
    935: func935,
    936: func936,
    937: func937,
    938: func938,
    939: func939,
    940: func940,
    941: func941,
    942: func942,
    943: func943,
    944: func944,
    945: func945,
    946: func946,
    947: func947,
    948: func948,
    949: func949,
    950: func950,
    951: func951,
    952: func952,
    953: func953,
    954: func954,
    955: func955,
    956: func956,
    957: func957,
    958: func958,
    959: func959,
    960: func960,
    961: func961,
    962: func962,
    963: func963,
    964: func964,
    965: func965,
    966: func966,
    967: func967,
    968: func968,
    969: func969,
    970: func970,
    971: func971,
    972: func972,
    973: func973,
    974: func974,
    975: func975,
    976: func976,
    977: func977,
    978: func978,
    979: func979,
    980: func980,
    981: func981,
    982: func982,
    983: func983,
    984: func984,
    985: func985,
    986: func986,
    987: func987,
    988: func988,
    989: func989,
    990: func990,
    991: func991,
    992: func992,
    993: func993,
    994: func994,
    995: func995,
    996: func996,
    997: func997,
    998: func998,
    999: func999,
}


def l(x):
    func_dict[x]()


s = time.time()
for x in range(0, 1000):
    l(x)

e = time.time() - s
print(f"Time: {e}")

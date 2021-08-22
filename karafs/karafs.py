#!/usr/bin/env python3

""" Karafs - Generate random persian names """

import sys
import time


def choice(objs):
    """ Selects a random item from a list """
    index = int(time.time() * 1_000_000) % len(objs)
    return objs[index]


FOODS = [
    {'en': 'ab havij-e', 'fa': 'آب هویج'},
    {'en': 'albaloo-ye', 'fa': 'آلبالوی'},
    {'en': 'aloo-ye', 'fa': 'آلوی'},
    {'en': 'alooche-ye', 'fa': 'آلوچهٔ'},
    {'en': 'anaar-e', 'fa': 'انار'},
    {'en': 'ananas-e', 'fa': 'آناناس'},
    {'en': 'anbe-ye', 'fa': 'انبهٔ'},
    {'en': 'angoor-e', 'fa': 'انگور'},
    {'en': 'anjir-e', 'fa': 'انجیر'},
    {'en': 'avokaado-ye', 'fa': 'آوکادوی'},
    {'en': 'azgil-e', 'fa': 'ازگیل'},
    {'en': 'baalang-e', 'fa': 'بالنگ'},
    {'en': 'badoom-e', 'fa': 'بادوم'},
    {'en': 'baloot-e', 'fa': 'بلوط'},
    {'en': 'beh-e', 'fa': 'به'},
    {'en': 'delester-e', 'fa': 'دلستر'},
    {'en': 'faloode-ye', 'fa': 'فالودهٔ'},
    {'en': 'fandogh-e', 'fa': 'فندق'},
    {'en': 'gerdoo-ye', 'fa': 'گردوی'},
    {'en': 'gheisi-e', 'fa': 'قیسی'},
    {'en': 'ghoore-ye', 'fa': 'غورهٔ'},
    {'en': 'gilas-e', 'fa': 'گیلاس'},
    {'en': 'golabi-ye', 'fa': 'گلابی'},
    {'en': 'grip froot-e', 'fa': 'گریپ فروت'},
    {'en': 'havij-e', 'fa': 'هویج'},
    {'en': 'hendoone-ye', 'fa': 'هندوانهٔ'},
    {'en': 'holoo-ye', 'fa': 'هلوی'},
    {'en': 'kadoo halvaee-ye', 'fa': 'کدو حلوایی'},
    {'en': 'kalam-e', 'fa': 'کلم'},
    {'en': 'karafs-e', 'fa': 'کرفس'},
    {'en': 'kharboze-ye', 'fa': 'خربزهٔ'},
    {'en': 'khiyar-e', 'fa': 'خیار'},
    {'en': 'khorma-ye', 'fa': 'خرمای'},
    {'en': 'khormaloo-ye', 'fa': 'خرمالوی'},
    {'en': 'kivi-ye', 'fa': 'کیوی'},
    {'en': 'komboze-ye', 'fa': 'کمبوزهٔ'},
    {'en': 'limoo shirin-e', 'fa': 'لیمو شیرین'},
    {'en': 'limoo torsh-e', 'fa': 'لیمو ترش'},
    {'en': 'loobiya chiti-ye', 'fa': 'لوبیا چیتی'},
    {'en': 'loobiya sefid-e', 'fa': 'لوبی سفید'},
    {'en': 'movz-e', 'fa': 'موز'},
    {'en': 'narengi-e', 'fa': 'نارنگی'},
    {'en': 'nargil-e', 'fa': 'نارگیل'},
    {'en': 'nokhod-e', 'fa': 'نخود'},
    {'en': 'nooshabe-ye', 'fa': 'نوشابهٔ'},
    {'en': 'panir-e', 'fa': 'پنیر'},
    {'en': 'peste-ye', 'fa': 'پستهٔ'},
    {'en': 'piyaz-e', 'fa': 'پیاز'},
    {'en': 'porteghal-e', 'fa': 'پرتغال'},
    {'en': 'sandis-e', 'fa': 'ساندیس'},
    {'en': 'senjed-e', 'fa': 'سنجد'},
    {'en': 'shaatoot-e', 'fa': 'شاتوت'},
    {'en': 'shaftaaloo-ye', 'fa': 'شفتالوی'},
    {'en': 'shalil-e', 'fa': 'شلیل'},
    {'en': 'shir berenj-e', 'fa': 'شیر برنج'},
    {'en': 'shir cacao-e', 'fa': 'شیر کاکائو'},
    {'en': 'shir moz-e', 'fa': 'شیر موز'},
    {'en': 'shir nargil-e', 'fa': 'شیر نارگیل'},
    {'en': 'shir toot-farangi-ye', 'fa': 'شیر توت فرنگی'},
    {'en': 'shivid-e', 'fa': 'شوید'},
    {'en': 'sib-e', 'fa': 'سیب'},
    {'en': 'sir-e', 'fa': 'سیر'},
    {'en': 'taalebi-e', 'fa': 'طالبی'},
    {'en': 'tah chin-e', 'fa': 'ته چین'},
    {'en': 'tameshk-e', 'fa': 'تمشک'},
    {'en': 'tamr hendi-ye', 'fa': 'تمر هندی'},
    {'en': 'ton maahi-ye', 'fa': 'تن ماهی'},
    {'en': 'toot farangi-ye', 'fa': 'توت فرنگی'},
    {'en': 'toot-e', 'fa': 'توت'},
    {'en': 'toranj-e', 'fa': 'ترنج'},
    {'en': 'torob-e', 'fa': 'ترب'},
    {'en': 'zalzalak-e', 'fa': 'زلزلک'},
    {'en': 'zard aloo-ye', 'fa': 'زردآلوی'},
    {'en': 'zereshk-e', 'fa': 'زرشک'},
    {'en': 'zeytoon-e', 'fa': 'زیتون'},
    {'en': 'zoghal akhte-ye', 'fa': 'ذغال اختهٔ'}
]

ADJS = [
    {'en': 'ablah', 'fa': 'ابله'},
    {'en': 'afsordeh', 'fa': 'افسرده'},
    {'en': 'afsordeh_sima', 'fa': 'افسرده سیما'},
    {'en': 'aloodeh', 'fa': 'آلوده'},
    {'en': 'ashofteh', 'fa': 'آشفته'},
    {'en': 'bad-bakht', 'fa': 'بدبخت'},
    {'en': 'bad-kholgh', 'fa': 'بد خلق'},
    {'en': 'bargozideh', 'fa': 'برگزیده'},
    {'en': 'bi-farhang', 'fa': 'بی فرهنگ'},
    {'en': 'bi-hejaab', 'fa': 'بی حجاب'},
    {'en': 'bi-taab', 'fa': 'بی تاب'},
    {'en': 'bi_namoos', 'fa': 'بی ناموس'},
    {'en': 'boland parvaz', 'fa': 'بلند پرواز'},
    {'en': 'chaaploos', 'fa': 'چاپلوس'},
    {'en': 'chabok', 'fa': 'چابک'},
    {'en': 'chasbideh', 'fa': 'چسبیده'},
    {'en': 'chegher', 'fa': 'چغر'},
    {'en': 'dana', 'fa': 'دانا'},
    {'en': 'daneshmand', 'fa': 'دانشمند'},
    {'en': 'dars khaandeh', 'fa': 'درس خوانده'},
    {'en': 'data scientist', 'fa': 'دیتا ساینتیست'},
    {'en': 'deldadeh', 'fa': 'دلداده'},
    {'en': 'delpazir', 'fa': 'دلپذیر'},
    {'en': 'delsard', 'fa': 'دلسرد'},
    {'en': 'divaneh', 'fa': 'دیوانه'},
    {'en': 'dom borideh', 'fa': 'دم بریده'},
    {'en': 'dordi_kash', 'fa': 'دردی کش'},
    {'en': 'farifteh', 'fa': 'فریفته'},
    {'en': 'farrokhzad', 'fa': 'فرخزاد'},
    {'en': 'farsoodeh', 'fa': 'فرسوده'},
    {'en': 'feminist', 'fa': 'فمینیست'},
    {'en': 'foroo_heshteh', 'fa': 'فروهشته'},
    {'en': 'forootan', 'fa': 'فروتن'},
    {'en': 'gharb zadeh', 'fa': 'غرب زده'},
    {'en': 'ghozmit', 'fa': 'قزمیت'},
    {'en': 'gij', 'fa': 'گیج'},
    {'en': 'gomashteh', 'fa': 'گماشته'},
    {'en': 'gorosne', 'fa': 'گرسنه'},
    {'en': 'gosasteh', 'fa': 'گسسته'},
    {'en': 'gozideh', 'fa': 'گزیده'},
    {'en': 'haraasaan', 'fa': 'هراسان'},
    {'en': 'javan-mard', 'fa': 'جوانمرد'},
    {'en': 'kaftar baaz', 'fa': 'کفترباز'},
    {'en': 'kalleh-pook', 'fa': 'کله پوک'},
    {'en': 'kar amad', 'fa': 'کارآمد'},
    {'en': 'kar azmoodeh', 'fa': 'کار آزموده'},
    {'en': 'khafan', 'fa': 'خفن'},
    {'en': 'khak_barsar', 'fa': 'خاک برسر'},
    {'en': 'khalideh', 'fa': 'خلیده'},
    {'en': 'khamideh', 'fa': 'خمیده'},
    {'en': 'khar-khoon', 'fa': 'خر خون'},
    {'en': 'kharaab', 'fa': 'خراب'},
    {'en': 'kharaaman', 'fa': 'خرامان'},
    {'en': 'khaste', 'fa': 'خسته'},
    {'en': 'kheng', 'fa': 'خنگ'},
    {'en': 'kheng', 'fa': 'خنگ'},
    {'en': 'khoshhal', 'fa': 'خوشحال'},
    {'en': 'legam gosikhteh', 'fa': 'لگام گسیخته'},
    {'en': 'mehrabaan', 'fa': 'مهربان'},
    {'en': 'miyaneh ro', 'fa': 'میانه رو'},
    {'en': 'modabber', 'fa': 'مدبر'},
    {'en': 'mofles', 'fa': 'مفلس'},
    {'en': 'momen', 'fa': 'مومن'},
    {'en': 'motor savar', 'fa': 'موتور سوار'},
    {'en': 'na-javan-mard', 'fa': 'نا جوانمرد'},
    {'en': 'na-shenas', 'fa': 'ناشناس'},
    {'en': 'naadaan', 'fa': 'نادان'},
    {'en': 'naz parvardeh', 'fa': 'ناز پرورده'},
    {'en': 'oghde_ee', 'fa': 'عقده\u200cای'},
    {'en': 'oskol', 'fa': 'اسکل'},
    {'en': 'parishan', 'fa': 'پریشان'},
    {'en': 'parvardeh', 'fa': 'پرورده'},
    {'en': 'pichideh', 'fa': 'پیچیده'},
    {'en': 'pishrafteh', 'fa': 'پیشرفته'},
    {'en': 'pokhteh', 'fa': 'پخته'},
    {'en': 'rahideh', 'fa': 'رهیده'},
    {'en': 'rang parideh', 'fa': 'رنگ پریده'},
    {'en': 'ravaanparish', 'fa': 'روانپریش'},
    {'en': 'resideh', 'fa': 'رسیده'},
    {'en': 'sakht-koosh', 'fa': 'سخت کوش'},
    {'en': 'salkhordeh', 'fa': 'سالخورده'},
    {'en': 'sar afkandeh', 'fa': 'سرافکنده'},
    {'en': 'sar gashteh', 'fa': 'سر گشته'},
    {'en': 'sar sepordeh', 'fa': 'سر سپرده'},
    {'en': 'sar shekasteh', 'fa': 'سر شکسته'},
    {'en': 'sarkhosh', 'fa': 'سرخوش'},
    {'en': 'setam-gar', 'fa': 'ستمگر'},
    {'en': 'setam-kesh', 'fa': 'ستمکش'},
    {'en': 'shab-zendeh-daar', 'fa': 'شب زنده دار'},
    {'en': 'shad', 'fa': 'شاد'},
    {'en': 'sharaab_zadeh', 'fa': 'شراب زده'},
    {'en': 'sharab zadeh', 'fa': 'شراب زده'},
    {'en': 'shargاi', 'fa': 'شرقی'},
    {'en': 'sharlatan', 'fa': 'شارلاتان'},
    {'en': 'shifteh', 'fa': 'شیفته'},
    {'en': 'shoorideh', 'fa': 'شوریده'},
    {'en': 'sirish', 'fa': 'سیریش'},
    {'en': 'sookhteh', 'fa': 'سوخته'},
    {'en': 'tafteh', 'fa': 'تافته'},
    {'en': 'taftideh', 'fa': 'تفتیده'},
    {'en': 'tahamtan', 'fa': 'تهمتن'},
    {'en': 'vabasteh', 'fa': 'وابسته'},
    {'en': 'varafteh', 'fa': 'وارفته'},
    {'en': 'varasteh', 'fa': 'وارسته'},
    {'en': 'varparideh', 'fa': 'ورپریده'},
    {'en': 'varshekasteh', 'fa': 'ورشکسته'},
    {'en': 'zabanzad', 'fa': 'زبانزد'},
    {'en': 'zereh push', 'fa': 'زره پوش'},
    {'en': 'zhoolideh', 'fa': 'ژولیده'},
    {'en': 'zir afkan', 'fa': 'زیر افکن'}
]


LANGS = ['en', 'fa']


def gen():
    """ Generates a name and adjective and returns them as tuple """
    return choice(FOODS), choice(ADJS)


def gen_str(lang='en') -> str:
    """ Generates a random name and returns that as a string

    Args:
        lang(str): you can specify the language (default is `en`)
    """
    food, adjective = gen()
    return f"{food[lang]} {adjective[lang]}"


def gen_str_without_space(lang='en'):
    """ Generates a random name without white space (gets language) """
    return gen_str(lang).replace(' ', '-')


def main(flags):
    """ The main cli entry point """
    if '-n' in flags:
        ind = flags.index('-n')
        try:
            count = flags.pop(ind+1)
        except IndexError:
            # no parameter passed to -n
            print('warning: option -n requires a parameter', file=sys.stderr)
            count = 1
        try:
            count = int(count)
        except ValueError:
            print('warning: option -n requires a number parameter', file=sys.stderr)
            count = 1
        flags.remove('-n')
    else:
        count = 1

    no_space = False
    if '--no-space' in flags:
        flags.remove('--no-space')
        no_space = True

    # handle language flags
    for lang in LANGS:
        if lang in flags:
            ind = flags.index(lang)
            flags[ind] = '-' + lang

    for i in range(count):
        name, adjective = gen()
        flags = ['-' + lang for lang in LANGS] if not flags else flags

        for lang in LANGS:
            if '-' + lang in flags:
                output = f"{name[lang]} {adjective[lang]}"
                # if `--no-space` flag in inserted, remove whitespaces
                if no_space:
                    output = output.replace(' ', '-')
                print(output)


if __name__ == '__main__':
    main(sys.argv[1:])

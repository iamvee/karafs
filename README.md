# karafs کرفس
تولید اسم های رندوم فینگیلیش

## installation 

```shell
pip install karafs
```

## usage

## دو زبانه

```shell
➜ karafs -n 10
توت فرنگی بی ناموس
toot farangi-ye bi_namoos
غورهٔ خسته
ghoore-ye khaste
انار زره پوش
anaar-e zereh push
انگور سر سپرده
angoor-e sar sepordeh
زلزلک نادان
zalzalak-e naadaan
سیب ورپریده
sib-e varparideh
فندق عقدهای
fandogh-e oghde_ee
گریپ فروت قزمیت
grip froot-e ghozmit
نارگیل پرورده
nargil-e parvardeh
تن ماهی تافته
ton maahi-ye tafteh
```

## فقط انگلیسی

```shell
➜ karafs -n 10 en
shaftaaloo-ye boland parvaz
baalang-e khoshhal
porteghal-e foroo_heshteh
piyaz-e oghde_ee
fandogh-e afsordeh
gheisi-e kar azmoodeh
piyaz-e gomashteh
limoo shirin-e zhoolideh
senjed-e tafteh
ananas-e khafan
```

## فقط فارسی

```shell
➜ karafs -n 10 fa

کیوی شارلاتان
لوبیا چیتی چابک
نوشابهٔ مفلس
تن ماهی اسکل
انار آلوده
انجیر پرورده
توت خسته
خیار رهیده
کمبوزهٔ شراب زده
گلابی فرسوده
```

## option `-n`
با این آپشن میتونید تعداد دفعات تولید اسم رندوم رو مشخص کنید.
اگر تنظیمش نکنید به طور پیشفرض تعداد 1 در نظر گرفته میشه.

```shell
➜ karafs -n 5
```

## option `--no-space`
با این آپشن میتونید خروجی رو بدون فاصله بین کلمات بگیرین:

```shell
➜ karafs --no-space -n 10
```


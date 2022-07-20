from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
from dataclasses import dataclass

# Create your views here.
dict_zoo = {'leo':'Leo [li:əu] - Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
            'scorpio': 'Scorpio [skɔ:piəu] - Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
            'aries':'Aries [ɛəri:z] - Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
            'taurus':'Taurus [tɔ:rəs] - Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
            'gemini':'Gemini [dʒeminai] - Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
            'cancer':'Cancer [kænsə(r)] - Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
            'virgo':'Virgo [vз:gəu] - Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
            'libra':'Libra [li:brə] - Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
            'sagittarius':'Sagittarius [sædʒitɛəriəs] - Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
            'capricorn':'Capricorn [kæprikɔ:n] - Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
            'aquarius':'Aquarius [əkwɛəriəs] - Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
            'pisces':'Pisces [paisi:z] - Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'}

def index(request):
    zodiacs = list(dict_zoo)
    #f"<li> <a href='{redirect_path}'>{sign.title()}</a> </li>"
    contex = {
        "zodiacs":zodiacs,
    }
    return render(request, "horoscope/index.html", context= contex)


def get_info_about_zodiak(request, dinamic_zoo:str):
    description = dict_zoo.get(dinamic_zoo, None)
    zodiacs = list(dict_zoo)
    data = {
        'description_zoo' : description,
        'sign': dinamic_zoo,
        'sign_name': description.split()[0],
        'zodiacs': zodiacs,
    }
    return render(request,'horoscope/info_zodiac.html', context=data)


def get_info_about_zodiak_integer(request, dinamic_zoo:int):
    zodiacs = list(dict_zoo)
    if dinamic_zoo > len(zodiacs):
        return HttpResponseNotFound(f'Nepravilnyi nomer Zodiaka - {dinamic_zoo}')
    name_zodiac = zodiacs[dinamic_zoo-1]
    redirect_url = reverse('horoscope-name',args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)
# def Leo(request):
#     return HttpResponse('Leo [li:əu] - Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).')
#
# def Scorpio(request):
#     return HttpResponse('Scorpio [skɔ:piəu] - Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).')
#
# def Aries (request):
#     return HttpResponse('Aries [ɛəri:z] - Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).')
#
# def Taurus (request):
#     return HttpResponse('Taurus [tɔ:rəs] - Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).')
#
# def Gemini (request):
#     return HttpResponse('Gemini [dʒeminai] - Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).')
#
# def Cancer (request):
#     return HttpResponse('Cancer [kænsə(r)] - Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).')
#
# def Virgo (request):
#     return HttpResponse('Virgo [vз:gəu] - Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).')
#
# def Libra (request):
#     return HttpResponse('Libra [li:brə] - Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).')
#
# def Sagittarius (request):
#     return HttpResponse('Sagittarius [sædʒitɛəriəs] - Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).')
#
# def Capricorn (request):
#     return HttpResponse('Capricorn [kæprikɔ:n] - Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).')
#
# def Aquarius (request):
#     return HttpResponse('Aquarius [əkwɛəriəs] - Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).')
#
# def Pisces (request):
#     return HttpResponse('Pisces [paisi:z] - Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).')

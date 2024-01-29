import flet as ft
from random import choice
import os



def main(page: ft.Page):
    WORDS = ('аэропОрты бАнты бОроду бухгАлтеров вероисповЕдание водопровОд газопровОд граждАнство дефИс дешевИзна '
             'диспансЕр договорённость докумЕнт досУг еретИк жалюзИ знАчимость Иксы икс каталОг квартАл киломЕтр кОнусов '
             'кОнус корЫсть крАны кран кремЕнь кремнЯ  лЕкторов лОктя локтЕй мЕстностей намЕрение нарОст нЕдруг недУг '
             'некролОг нЕнависть нефтепровОд новостЕй нОгтя ногтЕй отзЫвОтрочество партЕр портфЕль пОручни придАное '
             'призЫв свёкла сирОты созЫв сосредотОчение срЕдства стАтуя столЯр тамОжня тОрты тУфля цемЕнт цЕнтнер цепОчка '
             'шАрфы  шофёр экспЕрт вернА знАчимый красИвее красИвейший  кУхонный ловкА  лОвкий мозаИчный оптОвый '
             'прозорлИвый прозорлИва слИвовый глагОлы бралА бралАсь взялА взялАсб влилАсь ворвалАсь воспринЯть воспринялА '
             ' воссоздалА вручИт гналА гналАсь добралА добралАсь дождалАсь дозвонИтся дозИровать ждалА жилОсь закУпорить '
             'занЯть зАнял  занялА зАняли заперлА заперлА запломбировАть защемИт звалА звонИт кАшлянуть клАла клЕить '
             'крАлась кровоточИть лгалА лилА лилАсь навралА наделИт надорвалАсь назвалАсь накренИтся  налилА  нарвалА '
             'начАть нАчал началА  нАчали  обзвонИт облегчИть облегчИт облилАсь обнялАсь обогналА ободралА ободрИть '
             'ободрИт ободрИтся одолжИт озлОбить оклЕить окружИт опОшлить освЕдомиться освЕдомится  отбылА  отдалА '
             'откУпорить отозвалА отозвалАсь перезвонИт перелилА плодоносИть пломбировАть повторИт позвалА позвонИт '
             'полилА положИть положИл понялА  послАла прибЫть прИбыл прибылА прИбыли принЯть прИнял принялА прИняли рвалА '
             'сверлИт снялА совралА создалА сорвалА сорИт убралА углубИть укрепИт чЕрпать щемИт щЁлкать').split()
    page.theme_mode = ft.ThemeMode.DARK
    def check_word(e):
        nonlocal picked_word
        if guess.value == picked_word:
            page.snack_bar = ft.SnackBar(ft.Text('вЕрно!'))
            page.snack_bar.open = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text('невЕрно, правильно: ' + picked_word))
            page.snack_bar.open = True
            page.update()
        picked_word = choice(WORDS)
        word.value = picked_word.lower()
        guess.value = ''
        page.update()
    picked_word = choice(WORDS)
    word = ft.Text(picked_word.lower())
    check = ft.IconButton(icon=ft.icons.CHECK_CIRCLE_ROUNDED, icon_color=ft.colors.GREEN, on_click=check_word)
    guess = ft.TextField(label='отвЕт', multiline=False, on_submit=check_word, autofocus=True)
    field = ft.Row([guess, check])

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(word)
    page.add(field)



ft.app(target=main)
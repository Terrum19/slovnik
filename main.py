import flet as ft
from random import choice
import os



def main(page: ft.Page):
    total_right = 0
    total_wrong = 0
    normal_radius = 50
    hover_radius = 60
    normal_title_style = ft.TextStyle(
        size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
    )
    hover_title_style = ft.TextStyle(
        size=22,
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
        shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
    )

    def on_chart_event(e: ft.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                section.radius = hover_radius
                section.title_style = hover_title_style
            else:
                section.radius = normal_radius
                section.title_style = normal_title_style
        chart.update()

    right_section = ft.PieChartSection(
                100, color=ft.colors.GREEN, title="Правильно 100%", title_style=normal_title_style
            )

    wrong_section = ft.PieChartSection(
                0, color=ft.colors.RED, title="Неправильно 0%", title_style=normal_title_style
    )

    chart = ft.PieChart(
        sections=[
            right_section,
            wrong_section
        ],
        sections_space=0,
        center_space_radius=30,
        on_chart_event=on_chart_event,)
    WORDS = {'VERB': ' бралА бралАсь взялА взялАсб влилАсь ворвалАсь воспринЯть воспринялА '
             ' воссоздалА вручИт гналА гналАсь добралА добралАсь дождалАсь дозвонИтся дозИровать ждалА жилОсь закУпорить '
             'занЯть зАнял  занялА зАняли заперлА заперлА запломбировАть защемИт звалА звонИт кАшлянуть клАла клЕить '
             'крАлась кровоточИть лгалА лилА лилАсь навралА наделИт надорвалАсь назвалАсь накренИтся  налилА  нарвалА '
             'начАть нАчал началА  нАчали  обзвонИт облегчИть облегчИт облилАсь обнялАсь обогналА ободралА ободрИть '
             'ободрИт ободрИтся одолжИт озлОбить оклЕить окружИт опОшлить освЕдомиться освЕдомится  отбылА  отдалА '
             'откУпорить отозвалА отозвалАсь перезвонИт перелилА плодоносИть пломбировАть повторИт позвалА позвонИт '
             'полилА положИть положИл понялА  послАла прибЫть прИбыл прибылА прИбыли принЯть прИнял принялА прИняли рвалА '
             'сверлИт снялА совралА создалА сорвалА сорИт убралА углубИть укрепИт чЕрпать щемИт щЁлкать'.split(),

             'ADJ': 'вернА знАчимый красИвее красИвейший кУхонный ловкА лОвкий мозаИчный оптОвый '
             'прозорлИвый прозорлИва слИвовый'.split(),

             'NOUN': 'аэропОрты бАнты бОроду бухгАлтеров вероисповЕдание водопровОд газопровОд граждАнство дефИс дешевИзна '
             'диспансЕр договорЁнность докумЕнт досУг еретИк жалюзИ знАчимость Иксы икс каталОг квартАл киломЕтр кОнусов '
             'кОнус корЫсть крАны кран кремЕнь кремнЯ  лЕкторов лОктя локтЕй мЕстностей намЕрение нарОст нЕдруг недУг '
             'некролОг нЕнависть нефтепровОд новостЕй нОгтя ногтЕй отзЫв Отрочество партЕр портфЕль пОручни придАное '
             'призЫв свЁкла сирОты созЫв сосредотОчение срЕдства стАтуя столЯр тамОжня тОрты тУфля цемЕнт цЕнтнер цепОчка '
             'шАрфы  шофёр экспЕрт'.split()
             }

    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.NONE
    def check_word(e):
        nonlocal picked_word
        nonlocal total_right
        nonlocal total_wrong
        if guess.value == picked_word:
            page.snack_bar = ft.SnackBar(ft.Text('вЕрно!'))
            page.snack_bar.bgcolor = ft.colors.GREEN
            total_right += 1
        else:
            page.snack_bar = ft.SnackBar(ft.Text('невЕрно, правильно: ' + picked_word, color=ft.colors.WHITE))
            page.snack_bar.bgcolor = ft.colors.RED
            total_wrong += 1
        page.snack_bar.open = True
        VAR = []
        for option in [noun_checkbox, adj_checkbox, verb_checkbox]:
            if option.value:
                VAR += WORDS[option.data]
        if not VAR:
            page.snack_bar = ft.SnackBar(ft.Text('Выберите группу слов, остолоп!!!!!!!!!', color=ft.colors.WHITE))
            page.snack_bar.bgcolor = ft.colors.RED
        else:
            picked_word = choice(VAR)
            right_section.value = total_right / (total_right + total_wrong) * 100
            wrong_section.value = 100 - right_section.value
            right_section.title = f'Правильно {round(right_section.value)}%'
            wrong_section.title = f'Неправильно {100 - round(right_section.value)}%'
            page.snack_bar.open = True
            word.value = picked_word.lower()
            guess.focus()
            guess.value = ''
            page.update()

    picked_word = choice(choice([value for value in list(WORDS.values())]))
    word = ft.Text(picked_word.lower())
    word.style = ft.TextThemeStyle.HEADLINE_MEDIUM
    check = ft.IconButton(icon=ft.icons.CHECK_CIRCLE_ROUNDED, icon_color=ft.colors.GREEN, on_click=check_word)
    guess = ft.TextField(label='отвЕт', multiline=False, on_submit=check_word, autofocus=True)
    noun_checkbox = ft.Checkbox(label='Существительные', value=True, data='NOUN')
    adj_checkbox = ft.Checkbox(label='Прилагательные', value=True, data='ADJ')
    verb_checkbox = ft.Checkbox(label='Глаголы', value=True, data='VERB')
    options = ft.Row([noun_checkbox, adj_checkbox, verb_checkbox])
    field = ft.Column([word, ft.Row([guess, check]), options, chart])

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(field)



ft.app(target=main)
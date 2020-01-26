# -*- coding: utf-8 -*-
import random

times = ['утром', 'днем', 'вечером', 'ночью', 'после обеда', 'перед сном']
advices = ['ожидайте', 'предостерегайтесь', 'будьте открыты для']
promises = ['гостей из забытого прошлого', 'встреч со старыми знакомыми',
            'неожиданного праздника', 'приятных встреч']


def generate_prophecies(total_num=5, num_sentence=3):
    prophecies = []

    i = 0
    while i < total_num:
        j = 0
        forecast = ''
        while j < num_sentence:
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = "{} {} {}.".format(t, a, p).capitalize()
            if j != num_sentence - 1:
                full_sentence += '<br>\n'

            forecast += full_sentence
            j += 1

        prophecies.append(forecast)
        i += 1

    return prophecies

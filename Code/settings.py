main_lst = {
    'благоустройство': {'банкомат': ['банкомат'],
                        'зрдавоохранение': ['аптечный',
                                            'пункт',
                                            'стоматология',
                                            'здоровье',
                                            'лекарство',
                                            'медицинский',
                                            'заболевание',
                                            'ковид',
                                            'педиатор'],
                        'каток': ['каток'],
                        'озеленение': ['кустарник', 'газон', 'сад', 'зелёный'],
                        'парк': ['парк'],
                        'развлечения': ['клуб'],
                        'садик': ['садик'],
                        'свет': ['свет', 'фонарь', 'освещение', 'лампочка'],
                        'школа': ['школа']},
    'дороги и транспорт': {'дорога': ['дорога',
                                      'тротуар',
                                      'бордюр',
                                      'лежачий',
                                      'полицейский',
                                      'остановка',
                                      'пешеходный']},
    'неприятный запах': {'мусор': ['мусор'],
                         'неприятный запах': ['неприятный', 'запах', 'вонь']},
    'содержание двора': {'вода': ['разводка', 'вода'],
                         'детская площадка': ['детский', 'площадка'],
                         'парковочное место': ['парковочный',
                                               'место',
                                               'автостоянка'],
                         'скамейка': ['скамейка'],
                         'спортивная площадка': ['спорт',
                                                 'площадка',
                                                 'тренажёр',
                                                 'баскетбольный',
                                                 'волейбольный',
                                                 'хоккейный'],
                         'электроника дома': ['провод', 'щиток']}
}
main_dct = {'благоустройство': ['банкомат',
                                'зрдавоохранение',
                                'каток',
                                'озеленение',
                                'парк',
                                'развлечения',
                                'садик',
                                'свет',
                                'школа'],
            'дороги и транспорт': ['дорога'],
            'неприятный запах': ['мусор', 'неприятный запах'],
            'содержание двора': ['вода',
                                 'детская площадка',
                                 'парковочное место',
                                 'скамейка',
                                 'спортивная площадка',
                                 'электроника дома']}

way_db = './output/db/hakaton.sqlite'
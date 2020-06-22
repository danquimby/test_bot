# coding=utf-8

states = ['gretings','SelectPizzaSize','SelectPayment', 'CompleteOrder', 'Confirm', 'Cancel', 'Complete']
answer = {
    'gretings': {
            'exit' : u'Добро пожаловать дорогой друг.'
        },
    'SelectPizzaSize' :
        {
            'enter': u'Какую вы хотите пиццу?  Большую или маленькую?',
            'exit' : u'Вы заказали {} пиццу',
            'error_answer': u'Я не разобрал ваш ответ, так какую пиццу?',
            'conditions' :
                [
                    [u'большую', u'первая', u'1'],
                    [u'маленькую', u'вторая', u'2']
                ]

            ,
        }
    ,
    'SelectPayment':
        {
            'enter': u'Как вы будете платить??',
            'exit' : u'Вы будете оплачивать заказ {}',
            'error_answer': u'Я не разобрал ваш ответ, так какую платить будем?',
            'conditions':
                [
                    [u'наличкой', u'налом', u'деньгами', '1'],
                    [u'картой', u'безналом', '2']
                ]
            ,
        }
    ,
    'CompleteOrder' :
        {
            'enter' : u'Вы хотите {} пиццу, оплата {} ?',
            'error_answer': u'ммм ??',
            'conditions': [[u'да', '1'], [u'нет', '2']] ,
        }
    ,
    'Confirm':{
            'enter': u'',
    },
    'Cancel':
        {
            'enter': u'Отмена заказа, возможно вы к нам еще вернетесь',
        }
    ,
    'Complete' :
        {
            'enter': u'Для оформления вам необходимо перейти на наш сайт',
        }

}

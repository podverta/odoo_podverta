import random, pytz, datetime, locale
from odoo import  models, fields, api
from datetime import datetime

READONLY_FIELD_STATES = {
    state: [('readonly', True)]
    for state in {'sale', 'done', 'cancel'}
}

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def random_value(self):
        return str(random.randint(1, 999))

    test = fields.Char(string='test', states=READONLY_FIELD_STATES,
                       default= random_value, copy=False)


    @api.onchange('order_line', 'date_order')
    def _onchange_date_order(self):
        format_datetime = datetime.now(pytz.timezone(
            "Europe/Moscow")).strftime("%d/%m/%Y %H:%M:%S")
        total = locale.currency(self.amount_total, symbol=False,
                                grouping=True)
        diff_dt = (datetime.now().replace(microsecond=0) \
                              - self.date_order).total_seconds()
        if len(self.order_line) > 0 or diff_dt != 0:
            self.test = str(f'{total} - {format_datetime}')

    @api.onchange('test')
    def _inverse_check_state(self):
        if len(self.test) > 50:
            return {'warning': {
                'title': ("Внимание!"),
                'message': (
                    'Длина текста должна быть меньше 50 символов!')}}






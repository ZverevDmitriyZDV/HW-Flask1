from settings import app
from views import AdvView

adv_view = AdvView.as_view('adv_api')

app.add_url_rule('/advs/', defaults={'id_needed': None},
                 view_func=adv_view, methods=['GET', ])
app.add_url_rule('/advs/', view_func=adv_view, methods=['POST', ])
app.add_url_rule('/advs/<int:id_needed>', view_func=adv_view,
                 methods=['GET', 'DELETE'])
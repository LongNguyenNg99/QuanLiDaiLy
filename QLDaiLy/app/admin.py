from app import admin, db
from flask_admin.contrib.sqla import ModelView
from app.models import *



admin.add_view(LoaidailyModelView(Loaidaily, db.session))
admin.add_view(HosoModelView(Hoso, db.session))
admin.add_view(PhieuthutienModelView(Phieuthutien, db.session))
admin.add_view(DoanhsoModelView(Doanhso, db.session))
admin.add_view(ModelView(Congno, db.session))
admin.add_view(ModelView(Phieuxuathang, db.session))
admin.add_view(MathangModelView(Mathang, db.session))
admin.add_view(ModelView(Chitietxuathang, db.session))
admin.add_view(ModelView(Quydinhmathang, db.session))
admin.add_view(ModelView(Quychetochuc, db.session))
admin.add_view(ModelView(Quydinhtienno, db.session))

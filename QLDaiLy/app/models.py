from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Enum
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from app import db
from datetime import datetime

class HosoModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = False
    can_export = True
    form_columns = ('tendaily','sdt','diachi','idquan','ngaytiepnhan','email','tienno', )

class LoaidailyModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = False
    form_columns = ('tenloaidaily', )

class PhieuthutienModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = False
    can_export = True
    form_columns = ('hoso','ngaythutien','sotienthu', )

class DoanhsoModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = False
    can_export = True
    form_columns = ('hoso','thang','sophieuxuat','tonggiatri', )

class MathangModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = False
    can_export = True
    form_columns = ('tenmathang', )

class Loaidaily(db.Model):
    __tablename__ = "loaidaily"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenloaidaily = Column(String(255),nullable=False)
    hoso = relationship('Hoso', backref="loaidaily", lazy=True)


    def __str__(self):
        return self.name

class Hoso(db.Model):
    __tablename__="hoso"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tendaily = Column(String(50), nullable=False)
    sdt = Column(String(255), nullable=True)
    diachi = Column(String(255), nullable=True)
    idquan = Column(String(255), nullable=True)
    ngaytiepnhan = Column(DateTime, default=datetime.now())
    email = Column(String(255), nullable=True)
    tienno = Column(Float, default=8)
    loaidaily_id = Column(Integer, ForeignKey(Loaidaily.id), nullable=False)
    phieuthutien = relationship('Phieuthutien', backref = "hoso", lazy = True)
    doanhso = relationship('Doanhso', backref="hoso", lazy=True)
    congno = relationship('Congno', backref="hoso", lazy=True)
    phieuxuathang = relationship('Phieuxuathang', backref="hoso", lazy=True)



    def __str__(self):
        return self.name


class Phieuthutien(db.Model):
    __tablename__ = "phieuthutien"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngaythutien = Column(DateTime, default=datetime.now())
    sotienthu = Column(Float, default=8)
    hoso_id = Column(Integer, ForeignKey(Hoso.id), nullable=False)


    def __str__(self):
        return self.name

class Doanhso(db.Model):
    __tablename__ = "doanhso"
    thang = Column(Integer, primary_key=True, autoincrement=True)
    sophieuxuat = Column(String(255),nullable=False)
    tonggiatri = Column(Float, default=8)
    hoso_id = Column(Integer, ForeignKey(Hoso.id), nullable=False)


    def __str__(self):
        return self.name

class Congno(db.Model):
    __tablename__ = "congno"
    thang = Column(Integer, primary_key=True, autoincrement=True)
    nodau = Column(Float, default=8)
    phatsinh = Column(Float, default=8)
    nocuoi = Column(Float, default=8)
    hoso_id = Column(Integer, ForeignKey(Hoso.id), nullable=False)


    def __str__(self):
        return self.name

class Phieuxuathang(db.Model):
    __tablename__ = "phieuxuathang"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngaylapphieuxuat = Column(DateTime, default=datetime.now())
    hoso_id = Column(Integer, ForeignKey(Hoso.id), nullable=False)
    chitietxuathang = relationship('Chitietxuathang', backref="phieuxuathang", lazy=True)


    def __str__(self):
        return self.name




class Mathang(db.Model):
    __tablename__ = "mathang"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenmathang = Column(String(255),nullable=False)
    chitietxuathang = relationship('Chitietxuathang', backref="mathang", lazy=True)


    def __str__(self):
        return self.name


class Chitietxuathang(db.Model):
    __tablename__ = "chitietxuathang"
    phieuxuathang_id = Column(Integer, ForeignKey(Phieuxuathang.id), primary_key=True)
    mathang_id = Column(Integer, ForeignKey(Mathang.id), primary_key=True)

    soluong = Column(Integer, nullable=False)
    dongia = Column(Float, default=8)
    donvitinh = Column(String(255), nullable=False)
    thanhtien = Column(Float, default=8)


    def __str__(self):
        return self.name


class Quydinhmathang(db.Model):
    __tablename__ = "quydinhmathang"
    id = Column(Integer, primary_key=True, autoincrement=True)
    donvitinh = Column(String(255), nullable=False)
    dongia = Column(Float, default=0)

class Quychetochuc(db.Model):
    __tablename__ = "quychetochuc"
    id = Column(Integer, primary_key=True, autoincrement=True)
    soloaidaily = Column(String(255), nullable=False)
    sodailytoida = Column(String(255), nullable=False)
    somathang = Column(String(255), nullable=False)
    soquan = Column(String(255), nullable=False)

class Quydinhtienno(db.Model):
    __tablename__ = "quydinhtienno"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tiennotoida = Column(Float, default=0)

if __name__== "__main__":
    db.create_all()

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Equipment(Model):
    __table__ = 'equipment'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    model = StringField(ddl='varchar(50)')
    asset_number = StringField(ddl='varchar(50)')
    acessories = StringField(ddl='varchar(50)')
    warehouse = StringField(default='入库', ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(default='无', ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    borrow_time = FloatField(default=time.time)
    scrapped = StringField(default='正常', ddl='varchar(50)')
    created_at = FloatField(default=time.time)

class Loan_records(Model):
    __table__ = 'loan_records'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    equipment_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    acessories =  StringField(ddl='varchar(50)')
    borrow_time = FloatField(default=time.time)
    return_time = FloatField(default=time.time)
    created_at = FloatField(default=time.time)
	
class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

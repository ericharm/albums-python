from peewee import CharField, DateTimeField, IntegerField

from albums_python.domain.utils import current_utc_datetime
from albums_python.query.models.model import Model


class User(Model):
    class Meta:
        table_name = "users"

    id = IntegerField(primary_key=True)
    email = CharField(null=False)
    encrypted_password = CharField(null=False)
    created_at = DateTimeField(default=current_utc_datetime)
    updated_at = DateTimeField(default=current_utc_datetime)

    def __repr__(self) -> str:
        return f"User<id={self.id}, email={self.email}>"

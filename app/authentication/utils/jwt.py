from app import JWT
from app.authentication.models import Blacklist


@JWT.token_in_blacklist_loader
def in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    jti_object = Blacklist.query.filter_by(jti=jti).first()

    return not (jti_object is None)

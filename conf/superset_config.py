SECRET_KEY = "__SECRET_KEY__"
SQLALCHEMY_DATABASE_URI="postgresql://__DB_USER__:__DB_PWD__@127.0.0.1/__DB_NAME__"

AUTH_TYPE = 2
AUTH_LDAP_SERVER = "ldap://127.0.0.1:389/"
AUTH_LDAP_USE_TLS = False

AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"
AUTH_LDAP_EMAIL_FIELD = "mail"

AUTH_LDAP_USERNAME_FORMAT = "uid=%s,ou=users,dc=yunohost,dc=org"
AUTH_LDAP_SEARCH = "ou=users,dc=yunohost,dc=org"
AUTH_LDAP_UID_FIELD = "uid"

AUTH_LDAP_GROUP_FIELD = "permission"
AUTH_ROLES_MAPPING = {
    "cn=__APP__.main,ou=permission,dc=yunohost,dc=org": ["Public"],
    "cn=__APP__.alpha,ou=permission,dc=yunohost,dc=org": ["Alpha"],
    "cn=__APP__.gamma,ou=permission,dc=yunohost,dc=org": ["Gamma"],
    "cn=__APP__.admin,ou=permission,dc=yunohost,dc=org": ["Admin"],
}
AUTH_ROLES_SYNC_AT_LOGIN = True

ENABLE_PROXY_FIX = True

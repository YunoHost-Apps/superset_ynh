from flask_appbuilder.security.manager import (
    AUTH_LDAP,
)

# Superset specific config
ROW_LIMIT = 5000

# Somehow these do not work
SUPERSET_WEBSERVER_PROTOCOL = "http"
SUPERSET_WEBSERVER_ADDRESS = "localhost"
SUPERSET_WEBSERVER_PORT = __PORT__

# Flask App Builder configuration
# Your App secret key will be used for securely signing the session cookie
# and encrypting sensitive information on the database
# Make sure you are changing this key for your deployment with a strong key.
# You can generate a strong key using `openssl rand -base64 42`

SECRET_KEY = '__SECRET_KEY__'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'postgresql://__DB_USER__:__DB_PWD__@localhost'

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = '__MAPBOX_API_KEY__'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# Replace users database roles each login with those received from OAUTH/LDAP
AUTH_ROLES_SYNC_AT_LOGIN = True

# A mapping from LDAP/OAUTH group names to FAB roles
AUTH_ROLES_MAPPING = {
    # For LDAP
    "(permission=cn=__APP__.user,ou=permission,dc=yunohost,dc=org)": ["User"],
    "(permission=cn=__APP__.admin,ou=permission,dc=yunohost,dc=org)": ["Admin"],
}

AUTH_LDAP_SERVER = "ldap://localhost"
AUTH_LDAP_USE_TLS = False

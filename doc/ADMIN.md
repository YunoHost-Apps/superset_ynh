# Permissions

The package ships with the following permissions for YunoHost users, corresponding to the user roles as defined in Superset's documentation:
Public (default YunoHost permission), Alpha, Gamma, Admin.

# Included database for user data

You can add your first connected database to Superset with the following settings.
This database is stored within your YunoHost server.

- Host: `127.0.0.1`
- Port: `5432`
- Database name: __USERDATA_DB_NAME__
- Username: __USERDATA_DB_USER__
- Password: __USERDATA_DB_PWD__

# External databases

This package ships with the dependencies required to connect to MySQL, SQL Server, and PostgreSQL databases.
Many more database types are compatible, but you will need to perform some manual actions on your sever.
More information on Superset's documentation about [Connecting to Databases](https://superset.apache.org/docs/configuration/databases).

⚠️ Do not run  Python (`pip`) commands as `root`!
If you need to install Python dependencies, first open the app's environment in CLI with `yunohost app shell __APP__`.
<!--
Nota bene : ce README est automatiquement généré par <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Il NE doit PAS être modifié à la main.
-->

# Apache Superset pour YunoHost

[![Niveau d’intégration](https://dash.yunohost.org/integration/superset.svg)](https://ci-apps.yunohost.org/ci/apps/superset/) ![Statut du fonctionnement](https://ci-apps.yunohost.org/ci/badges/superset.status.svg) ![Statut de maintenance](https://ci-apps.yunohost.org/ci/badges/superset.maintain.svg)

[![Installer Apache Superset avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Lire le README dans d'autres langues.](./ALL_README.md)*

> *Ce package vous permet d’installer Apache Superset rapidement et simplement sur un serveur YunoHost.*  
> *Si vous n’avez pas YunoHost, consultez [ce guide](https://yunohost.org/install) pour savoir comment l’installer et en profiter.*

## Vue d’ensemble

Superset is a modern data exploration and data visualization platform. Superset can replace or augment proprietary business intelligence tools for many teams. Superset integrates well with a variety of data sources.

Superset provides:

- A no-code interface for building charts quickly
- A powerful, web-based SQL Editor for advanced querying
- A lightweight semantic layer for quickly defining custom dimensions and metrics
- Out of the box support for nearly any SQL database or data engine
- A wide array of beautiful visualizations to showcase your data, ranging from simple bar charts to geospatial visualizations
- Lightweight, configurable caching layer to help ease database load
- Highly extensible security roles and authentication options
- An API for programmatic customization
- A cloud-native architecture designed from the ground up for scale

*-- Superset's Github repository*


**Version incluse :** 4.1.1~ynh1

## Captures d’écran

![Capture d’écran de Apache Superset](./doc/screenshots/explore.jpg)

## Documentations et ressources

- Site officiel de l’app : <https://superset.apache.org/>
- Documentation officielle de l’admin : <https://superset.apache.org/docs/intro>
- Dépôt de code officiel de l’app : <https://github.com/apache/superset>
- YunoHost Store : <https://apps.yunohost.org/app/superset>
- Signaler un bug : <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche `testing`](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

Pour essayer la branche `testing`, procédez comme suit :

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
ou
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**Plus d’infos sur le packaging d’applications :** <https://yunohost.org/packaging_apps>

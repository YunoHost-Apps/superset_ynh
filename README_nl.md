<!--
NB: Deze README is automatisch gegenereerd door <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Hij mag NIET handmatig aangepast worden.
-->

# Apache Superset voor Yunohost

[![Integratieniveau](https://apps.yunohost.org/badge/integration/superset)](https://ci-apps.yunohost.org/ci/apps/superset/)
![Mate van functioneren](https://apps.yunohost.org/badge/state/superset)
![Onderhoudsstatus](https://apps.yunohost.org/badge/maintained/superset)

[![Apache Superset met Yunohost installeren](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Deze README in een andere taal lezen.](./ALL_README.md)*

> *Met dit pakket kun je Apache Superset snel en eenvoudig op een YunoHost-server installeren.*  
> *Als je nog geen YunoHost hebt, lees dan [de installatiehandleiding](https://yunohost.org/install), om te zien hoe je 'm installeert.*

## Overzicht

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


**Geleverde versie:** 4.1.2~ynh1

## Schermafdrukken

![Schermafdrukken van Apache Superset](./doc/screenshots/explore.jpg)

## Documentatie en bronnen

- Officiele website van de app: <https://superset.apache.org/>
- Officiele beheerdersdocumentatie: <https://superset.apache.org/docs/intro>
- Upstream app codedepot: <https://github.com/apache/superset>
- YunoHost-store: <https://apps.yunohost.org/app/superset>
- Meld een bug: <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Ontwikkelaarsinformatie

Stuur je pull request alsjeblieft naar de [`testing`-branch](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

Om de `testing`-branch uit te proberen, ga als volgt te werk:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
of
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**Verdere informatie over app-packaging:** <https://yunohost.org/packaging_apps>

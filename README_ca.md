<!--
N.B.: Aquest README ha estat generat automàticament per <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NO s'ha de modificar manualment.
-->

# Apache Superset per YunoHost

[![Nivell d'integració](https://apps.yunohost.org/badge/integration/superset)](https://ci-apps.yunohost.org/ci/apps/superset/)
![Estat de funcionament](https://apps.yunohost.org/badge/state/superset)
![Estat de manteniment](https://apps.yunohost.org/badge/maintained/superset)

[![Instal·la Apache Superset amb YunoHosth](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Llegeix aquest README en altres idiomes.](./ALL_README.md)*

> *Aquest paquet et permet instal·lar Apache Superset de forma ràpida i senzilla en un servidor YunoHost.*  
> *Si no tens YunoHost, consulta [la guia](https://yunohost.org/install) per saber com instal·lar-lo.*

## Visió general

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


**Versió inclosa:** 4.1.2~ynh1

## Captures de pantalla

![Captures de pantalla de Apache Superset](./doc/screenshots/explore.jpg)

## Documentació i recursos

- Lloc web oficial de l'aplicació: <https://superset.apache.org/>
- Documentació oficial per l'administrador: <https://superset.apache.org/docs/intro>
- Repositori oficial del codi de l'aplicació: <https://github.com/apache/superset>
- Botiga YunoHost: <https://apps.yunohost.org/app/superset>
- Reportar un error: <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Informació per a desenvolupadors

Envieu les pull request a la [branca `testing`](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

Per provar la branca `testing`, procedir com descrit a continuació:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
o
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**Més informació sobre l'empaquetatge d'aplicacions:** <https://yunohost.org/packaging_apps>

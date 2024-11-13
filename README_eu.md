<!--
Ohart ongi: README hau automatikoki sortu da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>ri esker
EZ editatu eskuz.
-->

# Apache Superset YunoHost-erako

[![Integrazio maila](https://dash.yunohost.org/integration/superset.svg)](https://ci-apps.yunohost.org/ci/apps/superset/) ![Funtzionamendu egoera](https://ci-apps.yunohost.org/ci/badges/superset.status.svg) ![Mantentze egoera](https://ci-apps.yunohost.org/ci/badges/superset.maintain.svg)

[![Instalatu Apache Superset YunoHost-ekin](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Irakurri README hau beste hizkuntzatan.](./ALL_README.md)*

> *Pakete honek Apache Superset YunoHost zerbitzari batean azkar eta zailtasunik gabe instalatzea ahalbidetzen dizu.*  
> *YunoHost ez baduzu, kontsultatu [gida](https://yunohost.org/install) nola instalatu ikasteko.*

## Aurreikuspena

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


**Paketatutako bertsioa:** 4.1.0~ynh1

## Pantaila-argazkiak

![Apache Superset(r)en pantaila-argazkia](./doc/screenshots/explore.jpg)

## Dokumentazioa eta baliabideak

- Aplikazioaren webgune ofiziala: <https://superset.apache.org/>
- Administratzaileen dokumentazio ofiziala: <https://superset.apache.org/docs/intro>
- Jatorrizko aplikazioaren kode-gordailua: <https://github.com/apache/superset>
- YunoHost Denda: <https://apps.yunohost.org/app/superset>
- Eman errore baten berri: <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Garatzaileentzako informazioa

Bidali `pull request`a [`testing` abarrera](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

`testing` abarra probatzeko, ondorengoa egin:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
edo
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**Informazio gehiago aplikazioaren paketatzeari buruz:** <https://yunohost.org/packaging_apps>

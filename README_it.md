<!--
N.B.: Questo README è stato automaticamente generato da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON DEVE essere modificato manualmente.
-->

# Apache Superset per YunoHost

[![Livello di integrazione](https://dash.yunohost.org/integration/superset.svg)](https://dash.yunohost.org/appci/app/superset) ![Stato di funzionamento](https://ci-apps.yunohost.org/ci/badges/superset.status.svg) ![Stato di manutenzione](https://ci-apps.yunohost.org/ci/badges/superset.maintain.svg)

[![Installa Apache Superset con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Leggi questo README in altre lingue.](./ALL_README.md)*

> *Questo pacchetto ti permette di installare Apache Superset su un server YunoHost in modo semplice e veloce.*  
> *Se non hai YunoHost, consulta [la guida](https://yunohost.org/install) per imparare a installarlo.*

## Panoramica

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


**Versione pubblicata:** 3.1.0~ynh1

## Screenshot

![Screenshot di Apache Superset](./doc/screenshots/explore.jpg)

## Documentazione e risorse

- Sito web ufficiale dell’app: <https://superset.apache.org/>
- Documentazione ufficiale per gli amministratori: <https://superset.apache.org/docs/intro>
- Repository upstream del codice dell’app: <https://github.com/apache/superset>
- Store di YunoHost: <https://apps.yunohost.org/app/superset>
- Segnala un problema: <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Informazioni per sviluppatori

Si prega di inviare la tua pull request alla [branch di `testing`](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

Per provare la branch di `testing`, si prega di procedere in questo modo:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
o
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**Maggiori informazioni riguardo il pacchetto di quest’app:** <https://yunohost.org/packaging_apps>

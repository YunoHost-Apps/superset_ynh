<!--
N.B.: Diese README wurde automatisch von <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> generiert.
Sie darf NICHT von Hand bearbeitet werden.
-->

# Apache Superset für YunoHost

[![Integrations-Level](https://apps.yunohost.org/badge/integration/superset)](https://ci-apps.yunohost.org/ci/apps/superset/)
![Funktionsstatus](https://apps.yunohost.org/badge/state/superset)
![Wartungsstatus](https://apps.yunohost.org/badge/maintained/superset)

[![Apache Superset mit YunoHost installieren](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Dieses README in anderen Sprachen lesen.](./ALL_README.md)*

> *Mit diesem Paket können Sie Apache Superset schnell und einfach auf einem YunoHost-Server installieren.*  
> *Wenn Sie YunoHost nicht haben, lesen Sie bitte [die Anleitung](https://yunohost.org/install), um zu erfahren, wie Sie es installieren.*

## Übersicht

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


**Ausgelieferte Version:** 4.1.2~ynh1

## Bildschirmfotos

![Bildschirmfotos von Apache Superset](./doc/screenshots/explore.jpg)

## Dokumentation und Ressourcen

- Offizielle Website der App: <https://superset.apache.org/>
- Offizielle Verwaltungsdokumentation: <https://superset.apache.org/docs/intro>
- Upstream App Repository: <https://github.com/apache/superset>
- YunoHost-Shop: <https://apps.yunohost.org/app/superset>
- Einen Fehler melden: <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Entwicklerinformationen

Bitte senden Sie Ihren Pull-Request an den [`testing` branch](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

Um den `testing` Branch auszuprobieren, gehen Sie bitte wie folgt vor:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
oder
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**Weitere Informationen zur App-Paketierung:** <https://yunohost.org/packaging_apps>

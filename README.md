<!--
N.B.: This README was automatically generated by <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
It shall NOT be edited by hand.
-->

# Apache Superset for YunoHost

[![Integration level](https://dash.yunohost.org/integration/superset.svg)](https://ci-apps.yunohost.org/ci/apps/superset/) ![Working status](https://ci-apps.yunohost.org/ci/badges/superset.status.svg) ![Maintenance status](https://ci-apps.yunohost.org/ci/badges/superset.maintain.svg)

[![Install Apache Superset with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Read this README in other languages.](./ALL_README.md)*

> *This package allows you to install Apache Superset quickly and simply on a YunoHost server.*  
> *If you don't have YunoHost, please consult [the guide](https://yunohost.org/install) to learn how to install it.*

## Overview

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


**Shipped version:** 4.1.0~ynh1

## Screenshots

![Screenshot of Apache Superset](./doc/screenshots/explore.jpg)

## Documentation and resources

- Official app website: <https://superset.apache.org/>
- Official admin documentation: <https://superset.apache.org/docs/intro>
- Upstream app code repository: <https://github.com/apache/superset>
- YunoHost Store: <https://apps.yunohost.org/app/superset>
- Report a bug: <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Developer info

Please send your pull request to the [`testing` branch](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

To try the `testing` branch, please proceed like that:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
or
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**More info regarding app packaging:** <https://yunohost.org/packaging_apps>

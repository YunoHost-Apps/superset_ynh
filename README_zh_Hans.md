<!--
注意：此 README 由 <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> 自动生成
请勿手动编辑。
-->

# YunoHost 上的 Apache Superset

[![集成程度](https://dash.yunohost.org/integration/superset.svg)](https://ci-apps.yunohost.org/ci/apps/superset/) ![工作状态](https://ci-apps.yunohost.org/ci/badges/superset.status.svg) ![维护状态](https://ci-apps.yunohost.org/ci/badges/superset.maintain.svg)

[![使用 YunoHost 安装 Apache Superset](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[阅读此 README 的其它语言版本。](./ALL_README.md)*

> *通过此软件包，您可以在 YunoHost 服务器上快速、简单地安装 Apache Superset。*  
> *如果您还没有 YunoHost，请参阅[指南](https://yunohost.org/install)了解如何安装它。*

## 概况

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


**分发版本：** 4.0.2~ynh1

## 截图

![Apache Superset 的截图](./doc/screenshots/explore.jpg)

## 文档与资源

- 官方应用网站： <https://superset.apache.org/>
- 官方管理文档： <https://superset.apache.org/docs/intro>
- 上游应用代码库： <https://github.com/apache/superset>
- YunoHost 商店： <https://apps.yunohost.org/app/superset>
- 报告 bug： <https://github.com/YunoHost-Apps/superset_ynh/issues>

## 开发者信息

请向 [`testing` 分支](https://github.com/YunoHost-Apps/superset_ynh/tree/testing) 发送拉取请求。

如要尝试 `testing` 分支，请这样操作：

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
或
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**有关应用打包的更多信息：** <https://yunohost.org/packaging_apps>

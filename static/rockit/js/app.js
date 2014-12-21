define([
  'angular',
  'configs/constants',
  'configs/routes',
  'configs/translate',
  'services/rockit',
  'services/translate',
  'services/notification',
  'services/anchorSmoothScroll',
  'directives/module',
  'associations/module',
  'mixes/module',
  'nodes/module',
  'settings/module'], function (ng, constants, routes, translate, rockitService, translateService, notificationService, anchorScroll) {
  'use strict';

  return ng.module("rockit", [
    "ngRoute",
    "pascalprecht.translate",
    "rockit.directives",
    "rockit.associations",
    "rockit.mixes",
    "rockit.nodes",
    "rockit.settings"
  ]).constant("RockitConfigs", constants)
    .service("RockitService", rockitService)
    .service("RockitTranslateService", translateService)
    .service("RockitNotifyService", notificationService)
    .service("RockitAnchorScroll", anchorScroll)
    .config(translate)
    .config(routes);
});
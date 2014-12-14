define([
  'angular',
  'configs/constants',
  'configs/routes',
  'configs/translate',
  'services/rockit',
  'services/translate',
  'services/notification',
  'directives/module',
  'associations/module',
  'nodes/module',
  'settings/module'], function (ng, constants, routes, translate, rockitService, translateService, notificationService) {
  'use strict';

  return ng.module("rockit", [
    "ngRoute",
    "pascalprecht.translate",
    "rockit.directives",
    "rockit.associations",
    "rockit.nodes",
    "rockit.settings"
  ]).constant("RockitConfigs", constants)
    .service("RockitService", rockitService)
    .service("RockitTranslateService", translateService)
    .service("RockitNotifyService", notificationService)
    .config(translate)
    .config(routes);
});
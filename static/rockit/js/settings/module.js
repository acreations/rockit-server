/**
 * Module for handle settings
 */
define(['angular',
  './controller',
  './service',
  './routes'], function (ng, controller, service, routes) {
  'use strict';

  var module = ng.module("rockit.settings", ['rockit']);

  return module
    .service('SettingsService', service)
    .controller('SettingsController', controller)
    .config(routes);
});
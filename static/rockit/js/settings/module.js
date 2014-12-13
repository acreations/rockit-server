/**
 * Module for handle settings
 */
define(['angular', './controller', './service'], function (ng, controller, service) {
  'use strict';

  var module = ng.module("rockit.settings", ['rockit.services']);

  return module
    .service('SettingsService', service)
    .controller('SettingsCtrl', controller);
});
/**
 * Module for handle settings
 */
define(['angular', './controller', './service', './routes'], function (ng, controller, service, routes) {
  'use strict';

  var module = ng.module("rockit.mixes", ['rockit']);

  return module
    .service('MixesService', service)
    .controller('MixesController', controller)
    .config(routes);
});
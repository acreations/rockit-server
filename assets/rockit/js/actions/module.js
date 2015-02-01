/**
 * Module for handle settings
 */
define(['angular', './controller', './service', './routes'], function (ng, controller, service, routes) {
  'use strict';

  var module = ng.module("rockit.actions", ['rockit']);

  return module
    .service('ActionResource', service)
    .controller('ActionsController', controller)
    .config(routes);
});
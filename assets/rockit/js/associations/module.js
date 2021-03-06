/**
 * Module for handle settings
 */
define(['angular', './controller', './service'], function (ng, controller, service) {
  'use strict';

  var module = ng.module("rockit.associations", ['rockit']);

  return module
    .service('AssociationsService', service)
    .controller('AssociationsCtrl', controller);
});
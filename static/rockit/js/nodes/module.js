/**
 * Module for handle nodes
 */
define(['angular', './controller', './service'], function (ng, controller, service) {

  var module = ng.module("rockit.nodes", ['rockit.services']);

  return module
    .service('NodesService', service)
    .controller('NodesController', controller);

});
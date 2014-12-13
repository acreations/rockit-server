/**
 * Module for handle nodes
 */
define(['angular',
  './controller/nodes',
  './controller/details',
  './service',
  './routes'], function (ng, nodesCtrl, detailsCtrl,service, routes) {

  var module = ng.module("rockit.nodes", ['rockit.services']);

  return module
    .service('NodesService', service)
    .controller('NodesController', nodesCtrl)
    .controller('NodesDetailsController', detailsCtrl)
    .config(routes);
});
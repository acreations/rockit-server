/**
 * Module for handle nodes
 */
define(['angular',
  './controller/list',
  './controller/detail',
  './service',
  './routes'], function (ng, nodeListCtrl, nodeDetailCtrl, service, routes) {
  'use strict';

  var module = ng.module("rockit.nodes", ['rockit']);

  return module
    .service('NodeService', service)
    .controller('NodeListController', nodeListCtrl)
    .controller('NodeDetailController', nodeDetailCtrl)
    .config(routes);
});
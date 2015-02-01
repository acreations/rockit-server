/**
 * Module for handle nodes
 */
define(['angular',
  './controller/list',
  './controller/detail',
  './controller/detail-razberry',
  './service',
  './routes',
  './commands/module'], function (ng, nodeListCtrl, nodeDetailCtrl, razberryCtrl, service, routes) {
  'use strict';

  var module = ng.module("rockit.nodes", ['rockit', 'rockit.nodes.commands']);

  return module
    .service('NodeService', service)
    .controller('NodeListController', nodeListCtrl)
    .controller('NodeDetailController', nodeDetailCtrl)
    .controller('NodeDetailRazberryController', razberryCtrl)
    .config(routes);
});
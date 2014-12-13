define([], function () {
  'use strict';

  return ['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/nodes', {
      templateUrl: 'partials/nodes',
      controller: 'NodesController'
    });
    $routeProvider.when('/nodes/:resource', {
      templateUrl: 'partials/nodes/details',
      controller: 'NodesDetailsController'
    });
  }];
});
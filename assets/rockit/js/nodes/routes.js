define([], function () {
  'use strict';

  return ['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/nodes', {
      templateUrl: 'partials/nodes',
      controller: 'NodeListController'
    });
    $routeProvider.when('/nodes/:uuid', {
      templateUrl: 'partials/nodes/details',
      controller: 'NodeDetailController'
    });
  }];
});
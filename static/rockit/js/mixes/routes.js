define([], function () {
  'use strict';

  return ['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/mixes', {
      templateUrl: 'partials/mixes',
      controller: 'MixesController'
    });
  }];
});
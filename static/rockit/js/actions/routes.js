define([], function () {
  'use strict';

  return ['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/actions', {
      templateUrl: 'partials/actions',
      controller: 'ActionsController'
    });
    $routeProvider.when('/actions/:url', {
      templateUrl: 'partials/actions/details',
      controller: 'ActionsController'
    });
  }];
});
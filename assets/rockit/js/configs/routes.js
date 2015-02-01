define(['angular-route'], function () {
  'use strict';

  return ['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/home', {
      templateUrl: 'partials/home'
    });
    $routeProvider.otherwise({
      redirectTo: '/home'
    });
  }];
});
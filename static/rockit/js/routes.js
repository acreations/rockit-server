define(['angular', 'angular-route'], function (ng) {
  'use strict';

  return ng.module("rockit.routes", ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
      $routeProvider.when('/home', {
        templateUrl: 'partials/home'
      });
      $routeProvider.otherwise({
        redirectTo: '/home'
      });
    }]);
});
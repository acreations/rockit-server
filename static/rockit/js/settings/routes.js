define([], function () {
  'use strict';

  return ['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/settings', {
      templateUrl: 'partials/settings',
      controller: 'SettingsController'
    });
  }];
});
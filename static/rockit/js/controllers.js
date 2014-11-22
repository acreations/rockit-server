define(['angular'], function (angular) {
  'use strict';

  return angular.module('rockit.controllers', [])

    .controller('MyCtrl1', ['$scope', 'settings', function ($scope, settings) {
      $scope.test = 'hello world';

      console.log("WORKS", settings.serverUrl);
    }]);
});
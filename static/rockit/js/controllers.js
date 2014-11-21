define(['angular'], function (angular) {
  'use strict';

  return angular.module('rockit.controllers', [])

    .controller('MyCtrl1', ['$scope', function ($scope) {
      $scope.test = 'hello world';

      console.log("WORKS");
    }]);
});
define([], function () {
  'use strict';

  return ['$scope',
    function (scope) {

      scope.details = scope.selected.details;

    }];
});
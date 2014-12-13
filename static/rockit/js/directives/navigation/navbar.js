define([], function () {
  'use strict';

  return ['$rootScope', '$location', function ($rootScope, $location) {
    return {
      restrict: 'C',
      translude: true,
      controller: function ($scope) {
        $rootScope.$on('$locationChangeSuccess', function () {
          $scope.path = $location.path().split('/')[1];
        });
      }
    };
  }];
});
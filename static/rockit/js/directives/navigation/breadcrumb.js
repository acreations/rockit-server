define([], function () {
  'use strict';

  return ['$rootScope', '$location', function ($rootScope, $location) {
    return {
      restrict: 'C',
      translude: true,
      controller: function ($scope) {

        var ucfirst = function (string) {
          return string.charAt(0).toUpperCase() + string.slice(1);
        };

        $rootScope.$on('$locationChangeSuccess', function () {
          var items = $location.path().split('/');
          items.shift();

          var locations = [];

          angular.forEach(items, function (item) {
            locations.push({
              title: ucfirst(item)
            })
          });

          $scope.items = locations;
        });

      }
    };
  }];
});
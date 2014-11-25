define(['angular', 'configs'], function (angular, configs) {
  'use strict';

  return angular.module('rockit.services', [])
    .factory('RockitService', ['$q', '$http', function (q, http) {

      return {
        get: function (resource) {
          var deferred = q.defer();

          http.get(resource).success(function (response) {
            deferred.resolve(response);
          });

          return deferred.promise;
        }
      };
    }])
    .config(['$provide', function (provide) {
      if (configs.rockit.mockEnabled) {
        provide.decorator('RockitService', ['$delegate', '$timeout', function (delegate, timeout) {
          var getFn = delegate.get;
          delegate.get = function () {
            timeout.setTimeout(function () {
              getFn();
            }, 5000);
          };
        }]);
      }
    }]);
});
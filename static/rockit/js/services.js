define(['angular', 'configs'], function (angular, configs) {
  'use strict';

  return angular.module('rockit.services', [])
    .factory('RockitService', ['$q', '$http', function (q, http) {

      return {
        get: function (resource) {
          var deferred = q.defer();

          http.get(resource).success(function (response) {
            if (configs.rockit.mockEnabled) {
              // Set a timer
            }
            deferred.resolve(response);
          });

          return deferred.promise;
        }
      };
    }]);
});
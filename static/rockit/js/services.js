define(['angular'], function (angular) {
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
    }]);
});
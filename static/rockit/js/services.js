define(['angular', 'configs'], function (angular, configs) {
  'use strict';

  return angular.module('rockit.services', [])
    .factory('RockitService', ['$q', '$http', function (q, http) {

      return {
        /**
         * Original list function that should not be public use
         */
        _list: function (resource) {
          var deferred = q.defer();

          http.get(resource).success(function (response) {
            deferred.resolve(response);
          });

          return deferred.promise;
        },
        /*
         * Get a resource
         */
        get: function (resource) {
          var deferred = q.defer();

          http.get(resource).success(function (response) {
            deferred.resolve(response);
          });

          return deferred.promise;
        },
        /*
         * Update a resource
         */
        update: function (resource, update) {
          var deferred = q.defer();

          http.put(resource, update).success(function (response) {
            deferred.resolve(response);
          });

          return deferred.promise;
        }
      };
    }]);
});
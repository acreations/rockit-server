define([], function () {
  'use strict';

  return ['$q', '$http', function (q, http) {
    return {
      /**
       * Original list function that should not be public use
       */
      list: function (resource) {
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
      },
      save: function (resource, data) {
        var deferred = q.defer();

        http.post(resource, data).success(function (response) {
          deferred.resolve(response);
        });

        return deferred.promise;
      }
    };
  }];
});
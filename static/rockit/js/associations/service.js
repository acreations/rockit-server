define(['angular', 'configs'], function (angular, configs) {
  'use strict';

  return angular.module('rockit.associations.service', [])
    .factory('AssociationsService', ['$q', '$http', function (q, http) {

      var serviceUrl = configs.rockit.serverUrl + '/associations';

      return {
        list: function () {
          var deferred = q.defer();

          http.get(serviceUrl).success(function (response) {
            deferred.resolve(response);
          });

          return deferred.promise;
        }
      };
    }]);
});
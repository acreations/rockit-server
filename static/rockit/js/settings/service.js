define(['angular'], function (angular) {
  'use strict';

  return angular.module('rockit.services.settings', ['rockit.configs'])
    .factory('SettingsService', ['$q', '$http', 'settings', function (q, http, settings) {

      var serviceUrl = settings.serverUrl + '/settings';

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
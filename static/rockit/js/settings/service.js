define(['angular', 'configs'], function (angular, configs) {
  'use strict';

  var serviceUrl = configs.rockit.serverUrl + '/settings';

  return angular.module('rockit.settings.service', ['rockit.services'])
    .factory('SettingsService', ['$q', '$http', 'RockitService', function (q, http, baseService) {

      var extended = angular.extend(baseService, {});

      extended.list =  function () {
        var deferred = q.defer();

        http.get(serviceUrl).success(function (response) {
          deferred.resolve(response);
        });

        return deferred.promise;
      };

      return extended;
    }])
    .config(function () {

      if (configs.rockit.mockEnabled) {
        serviceUrl = configs.rockit.mockUrl + '/settings/responses/list.response';
      }

    });
});
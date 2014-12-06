define(['angular', 'configs'], function (angular, configs) {
  'use strict';

  var serviceUrl = configs.rockit.serverUrl + '/nodes';

  return angular.module('rockit.nodes.service', ['rockit.services'])
    .factory('NodesService', ['$q', '$http', 'RockitService', function (q, http, baseService) {

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

      if (configs.rockit.mockEnabled && false) {
        serviceUrl = configs.rockit.mockUrl + '/settings/responses/list.response';
      }

    });
});
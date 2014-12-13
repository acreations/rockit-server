define(['angular', 'configs'], function (ng, configs) {
  'use strict';

  var serviceUrl = configs.rockit.serverUrl + '/nodes';

  if (configs.rockit.mockEnabled && false) {
    serviceUrl = configs.rockit.mockUrl + '/settings/responses/list.response';
  }

  return ['$q', '$http', 'RockitService', function (q, http, baseService) {

    var extended = ng.extend(baseService, {});

    extended.list =  function () {
      var deferred = q.defer();

      http.get(serviceUrl).success(function (response) {
        deferred.resolve(response);
      });

      return deferred.promise;
    };

    return extended;
  }];
});
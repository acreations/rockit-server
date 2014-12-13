define(['angular', 'configs'], function (ng, configs) {
  'use strict';

  var serviceUrl = configs.rockit.serverUrl + '/settings';

  if (configs.rockit.mockEnabled) {
    serviceUrl = configs.rockit.mockUrl + '/settings/responses/list.response';
  }

  return ['$q', '$http', 'RockitService', function (q, http, baseService) {

    var extended = ng.extend(baseService, {});

    extended.list =  function () {
      return extended._list(serviceUrl);
    };

    return extended;
  }];
});
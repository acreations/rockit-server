define(['angular', 'configs'], function (ng, configs) {
  'use strict';

  var serviceUrl = configs.rockit.serverUrl + '/associations';

  return ['RockitService', function (baseService) {

    var extended = ng.extend(baseService, {});

    extended.list =  function () {
      return extended._list(serviceUrl);
    };

    return extended;
  }];
});
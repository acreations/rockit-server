define([], function () {
  'use strict';

  return ['RockitConfigs', 'RockitService', function (configs, service) {

    var serviceUrl = configs.serverUrl + '/associations';

    return {
      list: function () {
        return service.list(serviceUrl);
      }
    };
  }];
});
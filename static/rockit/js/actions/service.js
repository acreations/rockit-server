define([], function () {
  'use strict';

  return ['RockitConfigs', 'RockitService', function (configs, service) {

    var serviceUrl = configs.serverUrl + '/actions';

    return {
      list: function () {
        return service.list(serviceUrl);
      },
      get: function (resource) {
        return service.get(resource);
      },
    };
  }];
});
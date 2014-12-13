define([], function () {
  'use strict';

  return ['RockitConfigs', 'RockitService', function (configs, service) {

    var serviceUrl = configs.serverUrl + '/nodes';

    if (configs.mockEnabled && false) {
      serviceUrl = configs.mockUrl + '/settings/responses/list.response';
    }

    return {
      list: function () {
        return service.list(serviceUrl);
      },
      get: function (resource) {
        return service.get(resource);
      },
      update: function (resource, update) {
        return service.update(resource, update);
      }
    };
  }];
});
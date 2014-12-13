define(['configs'], function (configs) {
  'use strict';

  var serviceUrl = configs.rockit.serverUrl + '/nodes';

  if (configs.rockit.mockEnabled && false) {
    serviceUrl = configs.rockit.mockUrl + '/settings/responses/list.response';
  }

  return ['RockitService', function (service) {

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
define(['configs'], function (configs) {
  'use strict';

  var serviceUrl = configs.rockit.serverUrl + '/associations';

  return ['RockitService', function (service) {

    return {
      list: function () {
        return service.list(serviceUrl);
      }
    };
  }];
});
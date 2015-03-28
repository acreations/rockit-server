(function() {
define([], function () {
  'use strict';

  return ['RockitConfigs', '$resource', function (configs, resource) {

    var resourceUrl = configs.serverUrl + '/actions/';

    return {
      query: function () {
        return resource(resourceUrl).query().$promise;
      },
      get: function (url) {
        return resource(url).get().$promise;
      },
      delete: function (url) {
        return resource(url).delete().$promise;
      },
      run: function (url) {
        var Action = resource(url, {}, { run: { method: 'PUT' } })
        return new Action().$run();
      }
    };
  }];
});
})();
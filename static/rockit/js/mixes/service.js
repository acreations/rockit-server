define(['angular', 'jquery'], function (angular, $) {
  'use strict';

  return ['$q', '$resource', 'RockitConfigs', 'RockitTranslateService', function (q, resource, configs, translate) {

    var resourceUrl = configs.serverUrl + '/mixes/';

    var _normalizeSelect = function (criteria) {
      var values = [];

      if (criteria.value) {
        angular.forEach(criteria.value, function (key) {
          var label = criteria.type + '-' + String(key);
          translate.t(label).then(function (translated) {
            values.push({
              id: key,
              label: translated
            });

            if (values.length === 1) {
              criteria.model = key;
            }
          });
        });
      }

      criteria.values = values;
    };

    var normalize = {
      'select': _normalizeSelect,
    };

    translate.addPart("mixes");

    return {
      criteria: function (url) {
        var deferred = q.defer();

        resource(url).get().$promise.then(
          function (data) {

            if (data.actions.POST) {
              angular.forEach(data.actions.POST, function (criteria) {
                if (normalize.hasOwnProperty(criteria.type)) {
                  normalize[criteria.type](criteria);
                }
              });
            }

            deferred.resolve(data);
          },
          function (error) {
            deferred.reject(error);
          }
        );

        return deferred.promise;
      },
      get: function () {
        return resource(resourceUrl).get().$promise;
      },
      save: function (data) {
        var Mix = resource(resourceUrl, {}, {}, { stripTrailingSlashes: false });

        return new Mix(data).$save();
      }
    };
  }];
});
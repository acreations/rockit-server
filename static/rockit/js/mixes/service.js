define(['angular'], function (angular) {
  'use strict';

  return ['$q', '$log', 'RockitConfigs', 'RockitService', 'RockitTranslateService', function (q, log, configs, service, translate) {

    var serviceUrl = configs.serverUrl + '/mixes';

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

            if (values.length == 1) {
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
      list: function () {
        return service.list(serviceUrl);
      },
      get: function (resource) {
        return service.get(resource);
      },
      getCriterias: function (resource) {
        var deferred = q.defer();

        service.get(resource).then(
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
    };
  }];
});
define(['angular'], function (angular) {
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

    var icons = {
      'when-alarm': 'fa-clock-o',
      'when-schedule': 'fa-calendar-o'
    };

    var _normalize = function (containers) {
      angular.forEach(containers, function (container) {
        angular.forEach(container, function (group) {

          angular.forEach(group.items, function (item) {
            item.parent = group;
            item.icon = icons.hasOwnProperty(item.identifier) ?
              icons[item.identifier] : 'icon-rockit';
          });
        });
      });

      return containers;
    };

    var normalizeCriterias = {
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
                if (normalizeCriterias.hasOwnProperty(criteria.type)) {
                  normalizeCriterias[criteria.type](criteria);
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
        var deferred = q.defer();

        resource(resourceUrl).get().$promise.then(
          function (data) {

            deferred.resolve(_normalize(data));

          },
          function (error) {
            deferred.reject(error);
          }
        );

        return deferred.promise;
      },
      save: function (data) {
        var Mix = resource(resourceUrl, {}, {}, { stripTrailingSlashes: false });

        return new Mix(data).$save();
      }
    };
  }];
});
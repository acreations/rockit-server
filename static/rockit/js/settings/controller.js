define([], function () {
  'use strict';

  return ['$scope', '$log', 'SettingsService', function (scope, log, settings) {

    scope.onSelectSettings = function (setting) {
      scope.selected = setting;

      // Settings has resource
      if (scope.selected.url) {
        settings.get(scope.selected.url).then(
          function (data) {
            log.debug('Successful got selected settings', data);

            scope.selected.items = data.items;
          }
        );
      }
    };

    scope.loadAvailableSettings = function (preselect) {
      log.debug('Load rockit settings');

      settings.list().then(
        function (data) {
          log.debug('Successful got settings', data);

          scope.settings = data;

          var _preselect = data[0];

          if (preselect) {
            log.debug('Trying to preselect', preselect);

            angular.forEach(data, function (setting) {
              if (setting.name === preselect) {
                _preselect = setting;
              }
            });
          }

          scope.onSelectSettings(_preselect);
        },
        function () {
          log.error('Exception when trying to load services');
        }
      );
    };
  }];
});
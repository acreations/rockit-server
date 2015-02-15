define([], function () {
  'use strict';

  return ['$scope', '$log', 'RockitNotifyService', 'RockitTranslateService', 'SettingsService',
    function (scope, log, notify, translation, settings) {

      translation.addPart('settings');

      scope.onSelectSettings = function (setting) {
        scope.selected = setting;
        scope.selected.snippet = '';

        // Settings has resource
        if (scope.selected.url) {
          settings.get(scope.selected.url).then(
            function (data) {
              log.debug('Successful got selected settings', data);

              scope.selected.items = data.items;
              scope.selected.snippet = '/partials/' + scope.selected.entry + '/settings';
            }
          );
        }
      };

      scope.toggleSettingAvailabilty = function (setting) {
        log.debug('Toggle settings', setting);

        if (setting.enabled) {
          notify.info("Successfully activated plugin <strong>" + setting.name + "</strong>");
        } else {
          notify.info("Successfully deactivated plugin <strong>" + setting.name + "</strong>");
        }
      }

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
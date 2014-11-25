define(['angular', 'settings/service'], function (angular) {
  'use strict';

  return angular.module('rockit.settings', ['rockit.settings.service'])

    .controller('SettingsCtrl', ['$scope', '$log', 'SettingsService', function (scope, log, settings) {

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

      scope.loadSettings = function () {
        log.debug('Load rockit settings');

        settings.list().then(
          function (data) {
            log.debug('Successful got settings', data);

            scope.settings = data;
            scope.onSelectSettings(data[0]);
          },
          function () {
            log.error('Exception when trying to load services');
          }
        );
      };
    }]);
});
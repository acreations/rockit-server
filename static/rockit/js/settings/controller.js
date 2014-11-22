define(['angular', 'settings/service'], function (angular) {
  'use strict';

  return angular.module('rockit.controllers.settings', ['rockit.services', 'rockit.services.settings'])

    .controller('SettingsCtrl', ['$scope', '$log', 'RockitService', 'SettingsService', function (scope, log, resource, settings) {

      scope.onSelectSettings = function (setting) {
        scope.selected = setting;

        // Settings has resource
        if (scope.selected.url) {
          resource.get(scope.selected.url).then(
            function (data) {
              log.debug('Successful got resource', data);
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
define([], function () {
  'use strict';

  return ['$scope', '$location', '$log', 'ActionsService', function (scope, location, log, service) {

    scope.criteria = {};

    var onCreate = function () {
      scope.getActions();
    };

    scope.getActions = function () {
      service.list().then(
        function (data) {
          log.debug('Successful retrieved actions', data);

          scope.actions = data;
        },
        function () {
          log.error('Exception when trying to get actions');
        }
      );
    };

    scope.onSelectedAction = function (action) {
      if (action) {
        location.path('/actions/' + 1);
      } else {
        log.error('No node is selected');
      }
    };

    onCreate();
  }];
});
define([], function () {
  'use strict';

  return ['$scope', '$location', '$routeParams', '$log', 'ActionsService',
    function (scope, location, routeParams, log, service) {

      scope.getSelectedAction = function () {
        log.debug('Trying to get selected action', routeParams.url);

        if(routeParams.url) {
          service.get(routeParams.url).then(
            function (data) {
              log.debug('Successful retrieved action', data);

              scope.selected = data;
            },
            function () {
              log.error('Exception when trying to get action');
            }
          );
        } else {
          log.error('None action url provided');
          scope.exception = true;
        }
      };

      scope.listActions = function () {
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
        location.path('/actions/' + action.url);
      };

    }];
});
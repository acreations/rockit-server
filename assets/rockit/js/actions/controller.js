(function() {
define([], function () {
  'use strict';

  return ['$scope', '$window', '$location', '$routeParams', '$log', 'ActionResource',
    function (scope, window, location, routeParams, log, Action) {

      // Holder for removing action
      scope.showConfirmRemoveModal = false;

      scope.confirmRemove = function (confirmName) {
        if (confirmName === scope.removeAction.name) {
          log.debug('Trying to remove action', scope.removeAction);

          Action.delete(scope.removeAction.url).then(
            function (data) {
              log.debug('Successful delete action', data);

              window.location.reload();
            },
            function () {
              log.error('Exception when trying to delete action');
            }
          );
        } else {
          log.error('Could not confirm removal', confirmName);
        }
      };

      scope.getSelectedAction = function () {
        log.debug('Trying to get selected action');

        Action.get(routeParams.url).then(
          function (data) {
            log.debug('Successful retrieved action', data);

            scope.selected = data;
          },
          function () {
            log.error('Exception when trying to get action');
          }
        );
      };

      scope.listActions = function () {
        Action.query().then(
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

      scope.remove = function (action) {
        scope.removeAction = action;
        scope.showConfirmRemoveModal = true;
      };

      scope.run = function (action) {
        log.debug('Trying to run action', action);
        Action.run(action.url).then(
          function (data) {
            log.debug('Successful run action', data);
          },
          function () {
            log.error('Exception when trying to run action');
          }
        );
      };
    }];
});
})();

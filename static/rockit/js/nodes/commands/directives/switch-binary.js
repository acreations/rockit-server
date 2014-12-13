define([], function () {
  'use strict';

  return ['NodeService', function (service) {
    return {
      restricted: 'E',
      scope: {
        model: '=ngModel',
      },
      template: '<input type="checkbox" data-ng-model="state" data-ng-change="onChangedState()"><span class="handle"></span>',
      controller: function ($scope, $log) {

        var ongoingRequest = false;
        var futureState = $scope.state;

        $scope.onChangedState = function () {

          if (!ongoingRequest) {
            $log.debug('Trying to change state', $scope.model);
            ongoingRequest = true;
            futureState = $scope.state;

            var command = futureState ? $scope.model.urls.on : $scope.model.urls.off;

            service.get(command).then(
              function () {
                // Callback
              },
              function () {
                $log.error('Failed to change state ... reverting');
                $scope.state = !futureState;
              }
            ).finally(function () {
              ongoingRequest = false;
            });

          } else {
            $log.debug('Already processing request ... skipping');
            $scope.state = futureState;
          }
        };

      },
      link: function (scope) {
        scope.state = scope.model.values.current;
      }
    };
  }];
});
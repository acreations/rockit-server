define([], function () {
  'use strict';

  return ['RockitNotifyService', 'NodeService', function (notify, service) {
    return {
      restricted: 'E',
      scope: {
        model: '=ngModel',
      },
      template: '<input type="checkbox" data-ng-model="state" data-ng-change="onChangedState()"><span class="handle selectable"></span></input>',
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
                if ($scope.state) {
                  notify.info("Successfully <strong>turned on</strong> device");
                } else {
                  notify.info("Successfully <strong>turned off</strong> device");
                }
              },
              function () {
                $log.error('Failed to change state ... reverting');
                $scope.state = !futureState;

                notify.error("Exception when trying to set device")
              }
            ).finally(function () {
              ongoingRequest = false;
            });

          } else {
            $log.debug('Already processing request ... skipping');
            $scope.state = futureState;

            notify.warning("Already an ongoing request");
          }
        };
      },
      link: function (scope) {
        scope.state = scope.model.values.current;
      }
    };
  }];
});
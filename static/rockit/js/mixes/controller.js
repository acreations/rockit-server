define([], function () {
  'use strict';

  return ['$scope', '$log', 'MixesService', function (scope, log, service) {

    scope.criteria = {};

    var onCreate = function () {
      scope.getCriterias();
    };

    scope.onSelectWhen = function (item) {
      scope.criteria.when = item;
    };

    scope.toggle = function (container, item) {
      container.selected = container.selected === item ? null : item;
    };

    scope.getCriterias = function () {
      service.list().then(
        function (data) {
          log.debug('Successful retrieved mixes criteria', data);

          scope.when = {
            data: data.when
          };
        },
        function () {
          log.error('Exception when trying to get associations');
        }
      );
    };

    onCreate();
  }];
});
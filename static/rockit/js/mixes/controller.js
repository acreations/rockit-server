define([], function () {
  'use strict';

  return ['$scope', '$log', 'MixesService', function (scope, log, service) {

    var criteria;

    var onCreate = function () {
      scope.getCriterias();
    };

    scope.getCriterias =  function () {
      service.list().then(
        function (data) {
          log.debug('Successful retrieved mixes criteria', data);

          criteria = data;
        },
        function () {
          log.error('Exception when trying to get associations');
        }
      );
    };

    onCreate();
  }];
});
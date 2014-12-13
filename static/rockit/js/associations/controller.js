define([], function () {
  'use strict';

  return ['$scope', '$log', 'AssociationsService', function (scope, log, service) {

    scope.loadAssociations =  function () {
      service.list().then(
        function (data) {
          log.debug('Successful retrieved associations', data);

          scope.associations = data;
        },
        function () {
          log.error('Exception when trying to get associations');
        }
      );
    };
  }];
});